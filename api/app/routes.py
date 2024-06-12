from flask import request, jsonify, redirect, url_for, session
from authlib.common.security import generate_token
from app import app, db, logger, bcrypt_app, oauth, stripe
from app.models.user import User, UserApiKeys, UserType
from app.utils.decorators import validate_jwt
from app.utils.emails import confirmation_email, welcome_email, reset_password_email, password_change_email, payment_complete_email
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
            logger.info(f"Existing user was navigated to login page - {email}")
            return jsonify({'is_user': True}), 200
        else:
            logger.info(f"New user was navigated to login page - {email}")
            return jsonify({'is_user': False}), 200
    except Exception as e:
        logger.error(f"Issue with checking user email {email}: {e}")
        return jsonify({'status': 'error', 'message': f'Issue with checking user email {e}'}), 500


@app.route("/api/v1/sign", methods=['POST']) # Signup new user
def signup_api():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            if existing_user.email_is_verify:
                logger.info(f"Signup attempt for existing user - {email}")
                return jsonify({'status': 'error', 'message': f'User with email {email} already exists.'}), 400
            else:
                db.session.delete(existing_user)
                db.session.commit()
                logger.info(f"User with unverified email was removed - {email}")
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
        verification_link = f"{os.environ.get('API_PROTOCOL')}://{request.host}/api/v1/verify-email/{confirmation_token}"
        user_name = email.split('@')[0]
        Thread(target=confirmation_email, args=(email, user_name, verification_link)).start()
        logger.info(f"New user was added successfully - {email}")
        return jsonify({'status': 'success', 'message': 'New user saved successfully'}), 200
    except Exception as e:
        logger.error(f"Failed to add new user - {email} - {e}")
        return jsonify({'status': 'error', 'message': f'Issue with adding a new user - {e}'}), 500
    

@app.route("/api/v1/login", methods=['POST']) # Login user
def login_api():
    try:
        email = request.json.get('email')
        password = request.json.get('password')
        user = User.query.filter_by(email=email).first()
        if user:
            if not user.email_is_verify:
                logger.info(f"Unverified user attemet to logged in - {email}")
                return jsonify({'status': 'error', 'message': 'User is not verified'}), 403
            if bcrypt_app.check_password_hash(user.password, password):
                data = {
                    'user_id': user.id,
                }
                access_token = jwt.encode(data, os.environ.get('JWT_SECRET_KEY'), algorithm='HS256')
                logger.info(f"User logged in successfully - {email}")
                return jsonify({'access_token': access_token}), 200
        logger.warning(f"Failed login attempt - {email}")    
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
            logger.info(f"Expired token used for email verification")
            return redirect(os.environ.get('PROD_APP_RESET_PASSWORD_URL'))
        user = User.query.filter_by(uid=data['uid']).first()
        if user and token == user.confirmation_token:
            user.email_is_verify = True
            user.confirmation_token = None
            db.session.commit()
            email = str(user.email)
            user_name = email.split('@')[0]
            Thread(target=welcome_email, args=(email, user_name)).start()
            logger.info(f"User email verified successfully - {email}")
            return redirect(os.environ.get('PROD_APP_LOGIN_URL'))
        logger.warning(f"Failed email verification attempt: User not found or token mismatch.")
        return redirect(os.environ.get('PROD_APP_LOGIN_URL'))
    except Exception as e:
        logger.error(f"Failed to verify user email: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to verify user email'}), 500



@app.route("/api/v1/reset-password-email", methods=['POST']) # Reset password
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
            reset_token = f"{os.environ.get('PROD_APP_RESET_PASSWORD_WITH_TOKEN_URL')}?t={confirmation_token}"
            user_name = email.split('@')[0]
            thread = Thread(target=reset_password_email, args=(email, user_name, reset_token))
            thread.start()
            logger.info(f"Reset password email was sent successfully - {email}")
            return jsonify({'status': 'success', 'message': "Reset password email was sent successfully"}), 200
        else:
            logger.warning(f"Attempted to reset password to non-existing user: {email}.")
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
            logger.info(f"Expired token used for reset password")
            return redirect(os.environ.get('PROD_APP_RESET_PASSWORD_URL'))
        user = User.query.filter_by(uid=data['uid']).first()
        if not user:
            logger.warning(f"User not found for uid: {data['uid']}.")
            return jsonify({'status': "User not found."}), 400
        if user and token == user.confirmation_token:
            hashed_password = bcrypt_app.generate_password_hash(password).decode('utf-8')
            user.password = hashed_password
            db.session.commit()
            email = str(user.email)
            user_name = email.split('@')[0]
            thread = Thread(target=password_change_email, args=(email, user_name))
            thread.start()
            logger.info(f"Password changed successfully - {email}.")
            return jsonify({'status': 'Password changed successfully..'}), 200
        else:
            logger.warning(f"Invalid confirmation token {user.email}.")
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
        logger.info("Initiating Google authentication process.")
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
            user_name = email.split('@')[0]
            Thread(target=welcome_email, args=(email, user_name)).start()

            logger.info(f"New user added successfully with Google auth - {email}")

        else:
            user_id = user.id
            logger.info(f"User logged in successfully with Google auth - {email}")
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
            'user': user.email.split('@')[0],
            'credits': user.credits,
            'subscription': user.subscription.value,
            'join_date': user.joined_date_formatted()
        }
        logger.info(f"User data retrieved successfully for user: {user.email}")
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
            logger.info(f"New API key generated successfully - {user.email}")
            return jsonify({'status': 'success', "New key was generated": ""}), 200
        else:
            logger.error(f"Couldn't find API key to generate a new one - {user.email}")
            return jsonify({'status': 'error', "message": "Couldn't find the api key"}), 400
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
            logger.info(f"API key deleted successfully - {user.email}")
            return jsonify({'status': 'success', "message": "New key was generated"}), 200
        else:
            return jsonify({'status': 'error', "message": "Couldn't find the api key"}), 400
    except Exception as e:
        logger.error(f"Failed to delete api key: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to delete api key'}), 500


##############################################################################
############################## STRIPE PAYMENT ################################
##############################################################################

@app.route('/v1/checkout-session', methods=['POST']) # Stripe checkout session
@validate_jwt
def create_checkout_session(user):
    try:
        credits = request.json.get('credits')
        product_id = request.json.get('productId')
        checkout_session = stripe.checkout.Session.create(
            line_items=[{
                        'price': product_id,
                        'quantity': 1,
                        },],
            mode='payment',
            success_url=os.getenv('PROD_APP_PAYMENT_COMPLETE_URL'),
            cancel_url=os.getenv('PROD_APP_PAYMENT_FAILD_URL'),
            metadata={'user_id': user.id, 'credits': credits})
        logger.info(f"Payment session created successfully - {user.email}")
        return jsonify({'checkout_session_url': checkout_session.url}), 200
    except Exception as e:
        logger.error(f"Failed to create payment session: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to create payment session'}), 500


@app.route('/stripe-callaback', methods=['POST']) # Stripe event callback
def webhook():
    try:
        endpoint_secret = os.getenv('STRIPE_ENDPOINT_SECRET', os.getenv('STRIPE_TESTING_KEY'))
        payload = request.data
        sig_header = request.headers['STRIPE_SIGNATURE']
        try:
            event = stripe.Webhook.construct_event(
                payload, sig_header, endpoint_secret
            )
        except ValueError as e:
            logger.info(f"Invalid payload. {e}")
            raise e
        except stripe.error.SignatureVerificationError as e:
            logger.info(f"Invalid signature. {e}")
            raise e
        if event['type'] == 'checkout.session.completed':
            user_id = event['data']['object']['metadata']['user_id']
            credits = event['data']['object']['metadata']['credits']
            logger.info(f"Checkout session completed. {user_id} - {credits}")
            user = User.query.filter_by(id=user_id).first()
            if user:
                user.credits += int(credits)
                user.subscription = UserType.SUBSCRIPTION
                db.session.commit()
                user_name = email.split('@')[0]
                Thread(target=payment_complete_email, args=(user.email, user_name, credits)).start()
                logger.info(f"Checkout session completed, Credit was added to user - {user.email}")
                return jsonify({'Credit update': True, 'message': 'Credits updated successfully'})
            logger.warning(f"Issue with finding user to complete checkout {event['data']} .")
            return jsonify({'error': 'User was not found'}), 500
    except Exception as e:
        logger.error(f"Failed to process stripe payment event: {str(e)}", exc_info=True)
        return jsonify({'status': 'error', 'message': 'Failed to process stripe payment event'}), 500