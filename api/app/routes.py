from flask import request, jsonify, redirect, url_for, session
from authlib.common.security import generate_token
from app import app, db, logger, bcrypt_app, oauth
from app.models.user import User, UserApiKeys
from app.utils.decorators import validate_jwt
from app.utils.emails import confirmation_email, welcome_email, password_change_email
from datetime import datetime, timedelta, timezone
from threading import Thread
import secrets
import uuid
import jwt
import os


# API routes
@app.route("/api/v1/email", methods=['POST'])
def email():
    try:
        email = request.json.get('email')
        user = User.query.filter_by(email=email).first()
        if user:
            return jsonify({'is_user': True})
        else:
            return jsonify({'is_user': False})
    except Exception as e:
        return jsonify({'status': 'error', 'message': f'Issue with checking user email {e}'}), 500


@app.route("/api/v1/sign", methods=['POST'])
def signup_api():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            if existing_user.email_is_verify:
                logger.info(f"User with email - {email} tried to sign but already exists")
                return jsonify({'status': 'error', 'message': 'User already exists.'}), 400
            else:
                db.session.delete(existing_user)
                db.session.commit()
                logger.info(f"No verified email was removed - {email}")

        # Hashed password and unique user id
        hashed_password = bcrypt_app.generate_password_hash(password).decode('utf-8')
        uid = str(uuid.uuid4())

        # Confirmation token for email validation
        expiration_time = datetime.utcnow() + timedelta(days=1)
        exp_timestamp = int(expiration_time.timestamp())
        data = {
            'uid': uid,
            'exp': exp_timestamp,
        }

        confirmation_token = jwt.encode(data, os.environ.get('JWT_SECRET_KEY'), algorithm='HS256')

        # Add new user to db
        new_user = User(email=email, password=hashed_password, uid=uid, confirmation_token=confirmation_token)

        # Generate init API key
        new_key = UserApiKeys(key=secrets.token_hex(16))
        new_user.api_keys.append(new_key)

        db.session.add(new_user)
        db.session.commit()

        # Send confirmation email
        verification_link = f"{os.environ.get('PROTOCOL')}://{request.host}/api/v1/verify-email/{confirmation_token}"
        user_name = email.split('@')[0]
        thread = Thread(target=confirmation_email, args=(email, user_name, verification_link))
        thread.start()

        logger.info(f"New user with email - {email} saved successfully")
        return jsonify({'status': 'success', 'message': 'New user saved successfully'}), 200

    except Exception as e:
        logger.error(f"Failed to add new user with email - {email} to the database - {e}")
        print(e)
        return jsonify({'status': 'error', 'message': f'Issue with adding a new user - {e}'}), 500
    

@app.route("/api/v1/login", methods=['POST'])
def login_api():
    email = request.json.get('email')
    password = request.json.get('password')

    user = User.query.filter_by(email=email).first()

    if user:
        if bcrypt_app.check_password_hash(user.password, password):
            data = {
                'user_id': user.id,
            }
            access_token = jwt.encode(data, os.environ.get('JWT_SECRET_KEY'), algorithm='HS256')
            logger.info(f"User with email - {email} logged in successfully")
            return jsonify({'access_token': access_token}), 200
        
    logger.error(f"User with email - {email} tried to login")    
    return jsonify({'status': "Wrong email or password."}), 400


@app.route('/api/v1/verify-email/<token>', methods=['GET'])
def confirm_email(token):

    data = jwt.decode(token, os.environ.get('JWT_SECRET_KEY'), algorithms=['HS256'])
    exp_timestamp = data.get('exp', None)
    exp_datetime = datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)

    # Check if the token has expired
    if exp_datetime < datetime.now(timezone.utc):
        return redirect(os.environ.get('PROD_APP_RESET_PASSWORD_URL'))

    user = User.query.filter_by(uid=data['uid']).first()

    # Check if the user and token match for email verification
    if user and token == user.confirmation_token:

        user.email_is_verify = True
        user.confirmation_token = None
        db.session.commit()

        # Send confirmation email
        app_link = f'{os.environ.get("PROD_APP_URL")}'
        email = str(user.email)
        user_name = email.split('@')[0]
        thread = Thread(target=welcome_email, args=(email, user_name, app_link))
        thread.start()

        return redirect(os.environ.get('PROD_APP_LOGIN_URL'))

    return redirect(os.environ.get('PROD_APP_LOGIN_URL'))


@app.route("/api/v1/resend-verification", methods=['POST'])
def resend_email():
    try:
        email = request.json.get('email')
        existing_user = User.query.filter_by(email=email).first()

        if existing_user:

            uid = existing_user.uid
            expiration_time = datetime.utcnow() + timedelta(days=1)
            exp_timestamp = int(expiration_time.timestamp())
            data = {
                'uid': uid,
                'exp': exp_timestamp,
            }

            confirmation_token = jwt.encode(data, os.environ.get('JWT_SECRET_KEY'), algorithm='HS256')

            existing_user.confirmation_token = confirmation_token

            db.session.commit()

            # Send confirmation email
            verification_link = f"{os.environ.get('PROTOCOL')}://{request.host}/api/v1/verify-email/{confirmation_token}"
            user_name = email.split('@')[0]
            thread = Thread(target=confirmation_email, args=(email, user_name, verification_link))
            thread.start()

            return jsonify({'status': 'Signed up successfully, confirmation email was sent.'}), 200

        else:
            return jsonify({'status': 'error', f"User with email {email} not exists": ""}), 400

    except Exception as e:
        print(e)
        return jsonify({'status': "Issue with adding a new user."}), 400


@app.route("/api/v1/reset-password", methods=['POST'])
def reset_password():
    try:
        password = request.json.get('password')
        token = request.json.get('token')

        data = jwt.decode(token, os.environ.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        exp_timestamp = data.get('exp', None)
        exp_datetime = datetime.fromtimestamp(exp_timestamp, tz=timezone.utc)

        if exp_datetime < datetime.now(timezone.utc):
            return redirect(os.environ.get('PROD_APP_RESET_PASSWORD_URL'))

        user = User.query.filter_by(uid=data['uid']).first()
        if not user:
            return jsonify({'status': "User not found."}), 400

        # Check if the user and token match for email verification
        if user and token == user.confirmation_token:

            hashed_password = bcrypt_app.generate_password_hash(password).decode('utf-8')
            user.password = hashed_password
            db.session.commit()

            # Use threading to send reset change email
            change_password_url = os.environ.get('PROD_APP_RESET_PASSWORD_URL')
            email = str(user.email)
            user_name = email.split('@')[0]
            thread = Thread(target=password_change_email, args=(email, user_name, change_password_url))
            thread.start()

            return jsonify({'status': 'Password changed successfully..'}), 200

        else:
            return jsonify({'status': "Non valid confirmation token."}), 400

    except Exception as e:
        print(e)
        return jsonify({'status': "Issue with changing the password."}), 400


@app.route('/api/v1/google-login/')
def google():

    GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
    GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')
    oauth.register(
        name='google',
        client_id=GOOGLE_CLIENT_ID,
        client_secret=GOOGLE_CLIENT_SECRET,
        server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
        client_kwargs={
            'scope': 'openid email profile'
        }
    )

    redirect_uri = url_for('google_auth', _external=True)

    nonce = generate_token()
    session['nonce'] = nonce
    return oauth.google.authorize_redirect(redirect_uri, nonce=nonce)


@app.route('/api/v1/google-auth/')
def google_auth():
    token = oauth.google.authorize_access_token()
    nonce = session['nonce']
    user = oauth.google.parse_id_token(token, nonce=nonce)

    email = user['email']
    given_name = user['given_name']
    family_name = user['family_name']

    user = User.query.filter_by(email=email).first()
    if not user:
        logger.info(f"new user: {email}")
        uid = str(uuid.uuid4())
        hashed_password = bcrypt_app.generate_password_hash(uid).decode('utf-8')
        new_user = User(email=email, password=hashed_password, uid=uid, given_name=given_name, family_name=family_name)
        
        # Generate init API key
        new_key = UserApiKeys(key=secrets.token_hex(16))
        new_user.api_keys.append(new_key)
        db.session.add(new_user)
        db.session.commit()
        user_id = new_user.id

        # Send confirmation email
        app_link = f'{os.environ.get("PROD_APP_URL")}'
        user_name = email.split('@')[0]
        thread = Thread(target=welcome_email, args=(email, user_name, app_link))
        thread.start()

    else:
        user_id = user.id
        logger.info(f"Existing user: {user_id}")
    data = {
        'user_id': user_id,
    }
    access_token = jwt.encode(data, os.environ.get('JWT_SECRET_KEY'), algorithm='HS256')
    redirect_url = f"{os.environ.get('PROD_APP_GOOGLE_REDIRECT')}?access_token={access_token}"
    return redirect(redirect_url)


@app.route("/api/v1/user", methods=['GET'])
@validate_jwt
def user(user):
    try:
        data = {
            'email': user.email.split('@')[0],
            'credits': user.credits,
        }
        return jsonify(data)
    except Exception as e:
        logger.error(f"Failed to retrieve user data: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to retrieve user data'}), 500


@app.route("/api/v1/expenses", methods=['POST'])
@validate_jwt
def add_expense(user):
    try:
        amount = request.json.get('amount')
        category = request.json.get('category')
        new_expense = Expense(amount=amount, category=category, user_id=user.id)
        db.session.add(new_expense)
        db.session.commit()
        logger.info(f"New expense was added successfully for user id - {user.id}")
        expense_additions_counter.labels(status='success').inc()
        return jsonify({'status': 'success', 'message': 'Expense added successfully'}), 200
    except Exception as e:
        logger.error(f"Error adding new expense for user id - {user.id}: {e}")
        expense_additions_counter.labels(status='failure').inc()
        return jsonify({'status': 'error', 'message': 'Failed to add expense'}), 500


@app.route("/api/v1/expenses", methods=['GET'])
@validate_jwt
def get_expenses(user):
    try:
        expenses = Expense.query.filter_by(user_id=user.id).all()
        logger.info(f"Expenses for user id - {user.id} retrieved successfully")
        return jsonify([{'amount': e.amount, 'category': e.category, 'date': e.date, 'id': e.id} for e in expenses]), 200
    except Exception as e:
        logger.error(f"Error retrieving expenses for user id - {user.id}: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to retrieve expenses'}), 500


@app.route("/api/v1/expenses/<int:expense_id>", methods=['DELETE'])
@validate_jwt
def delete_expense(user, expense_id):
    try:
        expense = Expense.query.filter_by(id=expense_id, user_id=user.id).first()
        if not expense:
            logger.error(f"Expense not found or you are not authorized to delete it for user id - {user.id}")
            return jsonify({'status': 'error', 'message': 'Expense not found or you are not authorized to delete it'}), 404

        db.session.delete(expense)
        db.session.commit()
        expense_deletions_counter.labels(status='not_found').inc()
        logger.info(f"Expense deleted successfully for user id - {user.id}")
        return jsonify({'status': 'success', 'message': 'Expense deleted successfully'}), 200
    except Exception as e:
        logger.error(f"Error deleting expense for user id - {user.id}, expense id - {expense_id}: {e}")
        expense_deletions_counter.labels(status='failure').inc()
        return jsonify({'status': 'error', 'message': 'Failed to delete expense'}), 500