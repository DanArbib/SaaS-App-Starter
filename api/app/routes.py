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


##############################################################################
############################### AUTHENTICATION ###############################
##############################################################################

@app.route("/api/v1/email", methods=['POST']) # Check if user is registered
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


@app.route("/api/v1/sign", methods=['POST']) # Signup new user
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
        hashed_password = bcrypt_app.generate_password_hash(password).decode('utf-8')
        uid = str(uuid.uuid4())
        expiration_time = datetime.utcnow() + timedelta(days=1)
        data = {
            'uid': uid,
            'exp': int(expiration_time.timestamp()),
        }
        confirmation_token = jwt.encode(data, os.environ.get('JWT_SECRET_KEY'), algorithm='HS256')
        new_user = User(email=email, password=hashed_password, uid=uid, confirmation_token=confirmation_token)
        new_key = UserApiKeys(key=secrets.token_hex(16))
        new_user.api_keys.append(new_key)
        db.session.add(new_user)
        db.session.commit()
        verification_link = f"{os.environ.get('PROTOCOL')}://{request.host}/api/v1/verify-email/{confirmation_token}"
        user_name = email.split('@')[0]
        Thread(target=confirmation_email, args=(email, user_name, verification_link)).start()
        logger.info(f"New user with email - {email} saved successfully")
        return jsonify({'status': 'success', 'message': 'New user saved successfully'}), 200
    except Exception as e:
        logger.error(f"Failed to add new user with email - {email} to the database - {e}")
        return jsonify({'status': 'error', 'message': f'Issue with adding a new user - {e}'}), 500
    

@app.route("/api/v1/login", methods=['POST']) # Login user
def login_api():
    try:
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
    except Exception as e:
        logger.error(f"Failed to login user: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to login user'}), 500


@app.route('/api/v1/verify-email/<token>', methods=['GET']) # Verify user's email
def confirm_email(token):
    try:
        data = jwt.decode(token, os.environ.get('JWT_SECRET_KEY'), algorithms=['HS256'])
        exp_datetime = datetime.fromtimestamp(data.get('exp', None), tz=timezone.utc)
        if exp_datetime < datetime.now(timezone.utc):
            return redirect(os.environ.get('PROD_APP_RESET_PASSWORD_URL'))
        user = User.query.filter_by(uid=data['uid']).first()
        if user and token == user.confirmation_token:
            user.email_is_verify = True
            user.confirmation_token = None
            db.session.commit()
            app_link = os.environ.get("PROD_APP_URL")
            email = str(user.email)
            user_name = email.split('@')[0]
            Thread(target=welcome_email, args=(email, user_name, app_link)).start()
            return redirect(os.environ.get('PROD_APP_LOGIN_URL'))
        return redirect(os.environ.get('PROD_APP_LOGIN_URL'))
    except Exception as e:
        logger.error(f"Failed to verify user email: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to verify user email'}), 500



@app.route("/api/v1/resend-verification", methods=['POST']) # Resend verification email
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
            verification_link = f"{os.environ.get('PROTOCOL')}://{request.host}/api/v1/verify-email/{confirmation_token}"
            user_name = email.split('@')[0]
            thread = Thread(target=confirmation_email, args=(email, user_name, verification_link))
            thread.start()
            return jsonify({'status': 'Signed up successfully, confirmation email was sent.'}), 200
        else:
            return jsonify({'status': 'error', f"User with email {email} not exists": ""}), 400
    except Exception as e:
        logger.error(f"Failed to resend verification: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to resend verification'}), 500


@app.route("/api/v1/reset-password", methods=['POST']) # Reset new password
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
        if user and token == user.confirmation_token:
            hashed_password = bcrypt_app.generate_password_hash(password).decode('utf-8')
            user.password = hashed_password
            db.session.commit()
            change_password_url = os.environ.get('PROD_APP_RESET_PASSWORD_URL')
            email = str(user.email)
            user_name = email.split('@')[0]
            thread = Thread(target=password_change_email, args=(email, user_name, change_password_url))
            thread.start()
            return jsonify({'status': 'Password changed successfully..'}), 200
        else:
            return jsonify({'status': "Non valid confirmation token."}), 400
    except Exception as e:
        logger.error(f"Failed to reset user password: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to reset user password'}), 500


##############################################################################
################################ GOOGLE AUTH #################################
##############################################################################

@app.route('/api/v1/google-login/') # Google auth request
def google():
    try:
        nonce = generate_token()
        session['nonce'] = generate_token()
        return oauth.google.authorize_redirect(url_for('google_auth', _external=True), nonce=nonce)
    except Exception as e:
        logger.error(f"Failed to redirect to google auth {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to redirect to google auth'}), 500

@app.route('/api/v1/google-auth/') # Google auth callback route
def google_auth():
    try:
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
            Thread(target=welcome_email, args=(email, user_name, app_link)).start()

        else:
            user_id = user.id
            logger.info(f"Existing user: {user_id}")
        data = {
            'user_id': user_id,
        }
        access_token = jwt.encode(data, os.environ.get('JWT_SECRET_KEY'), algorithm='HS256')
        redirect_url = f"{os.environ.get('PROD_APP_GOOGLE_REDIRECT')}?access_token={access_token}"
        return redirect(redirect_url)
    except Exception as e:
        logger.error(f"Failed to get google auth callaback {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to get google auth callaback'}), 500

##############################################################################
################################## USER DATA #################################
##############################################################################

@app.route("/api/v1/user", methods=['GET']) # Get user information
@validate_jwt
def user(user):
    try:
        data = {
            'email': user.email.split('@')[0],
            'credits': user.credits,
            'subscription': user.subscription,
            'join_date': user.joined_date_formatted()
        }
        return jsonify(data)
    except Exception as e:
        logger.error(f"Failed to retrieve user data: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to retrieve user data'}), 500


##############################################################################
################################## API KEYS ##################################
##############################################################################

@app.route('/api-keys', methods=['GET']) # Get api keys
@validate_jwt
def api_keys(user):
    try:
        return jsonify({'api_keys': [key.key for key in user.api_keys]})
    except Exception as e:
        logger.error(f"Failed to retrieve user api keys: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to retrieve user api keys'}), 500


@app.route('/generate-api-key', methods=['POST']) # Generate api key
@validate_jwt
def generate_api_key(user):
    try:
        user_key = UserApiKeys.query.filter_by(user=user, key=request.json.get('key')).first()
        if user_key:
            db.session.delete(user_key)
            new_key_value = str(secrets.token_hex(16))
            new_key = UserApiKeys(user=user, key=new_key_value)
            db.session.add(new_key)
            db.session.commit()
            return jsonify({'status': 'success', "New key was generated": ""}), 200
        else:
            return jsonify({'status': 'error', "Couldn't find the api key": ""}), 400
    except Exception as e:
        logger.error(f"Failed to generate api key: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to generate api key'}), 500


@app.route('/delete-api-key', methods=['DELETE']) # Delete api key
@validate_jwt
def delete_api_key(user):
    try:
        user_key = UserApiKeys.query.filter_by(user=user, key=request.json.get('key')).first()
        if user_key:
            db.session.delete(user_key)
            db.session.commit()
            return jsonify({'status': 'success', "New key was generated": ""}), 200
        else:
            return jsonify({'status': 'error', "Couldn't find the api key": ""}), 400
    except Exception as e:
        logger.error(f"Failed to delete api key: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to delete api key'}), 500
