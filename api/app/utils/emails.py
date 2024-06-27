from flask import render_template
from app import app, mail, logger
from flask_mail import Message
import os

APP_NAME = os.environ.get("APP_NAME")
LOGO_URL = os.environ.get("PROD_APP_LOGO_URL")
APP_SUPPORT_EMAIL = os.environ.get("APP_SUPPORT_EMAIL")
PROD_APP_URL = os.environ.get("PROD_APP_URL")
PROD_APP_RESET_PASSWORD_URL = os.environ.get('PROD_APP_RESET_PASSWORD_URL')

def confirmation_email(email, user_name, verification_link_app):
    with app.app_context():
        try:
            print(verification_link_app)
            subject = f'Hi {user_name}, please verify your {APP_NAME} account'
            html_body = render_template('verification_email.html', user_name=user_name, verification_link=verification_link_app,
                                        logo=LOGO_URL, support_email=APP_SUPPORT_EMAIL, app_name=APP_NAME)
            msg = Message(subject, recipients=[email], html=html_body)
            mail.send(msg)
            logger.info(f"Verification email sent successfully - {email}")
        except Exception as e:
            mail.send(e)
            logger.error(f'Error sending verification email: {e}')


def welcome_email(email, user_name):
    with app.app_context():
        try:
            subject = f'Welcome to {APP_NAME}!'
            html_body = render_template('welcome_email.html', user_name=user_name, app_link=PROD_APP_URL,
                                        logo=LOGO_URL, support_email=APP_SUPPORT_EMAIL, app_name=APP_NAME)
            msg = Message(subject, recipients=[email], html=html_body)
            mail.send(msg)
            logger.info(f"Welcome email sent successfully - {email}")
        except Exception as e:
            logger.error(f'Error sending welcome email: {e}')


def payment_complete_email(email, user_name, credits):
    with app.app_context():
        try:
            subject = 'Thanks for your payment'
            html_body = render_template('payment_complete.html', user_name=user_name,
                                        logo=LOGO_URL, app_link=PROD_APP_URL, added_credit=credits,
                                        app_name=APP_NAME, support_email=APP_SUPPORT_EMAIL)
            msg = Message(subject, recipients=[email], html=html_body)
            mail.send(msg)
            logger.info(f"Payment complete email sent successfully - {email}")
        except Exception as e:
            logger.error(f'Error sending payment complete email: {e}')


def reset_password_email(email, user_name, reset_token):
    with app.app_context():
        try:
            subject = f'{APP_NAME} Password Reset'
            html_body = render_template('reset_password_email.html', user_name=user_name, reset_token=reset_token,
                                        logo=LOGO_URL, app_name=APP_NAME)
            msg = Message(subject, recipients=[email], html=html_body)
            mail.send(msg)
            logger.info(f"Reset password email sent successfully - {email}")
        except Exception as e:
            logger.error(f'Error sending email: {e}')


def password_change_email(email, user_name):
    with app.app_context():
        try:
            subject = f'Your {APP_NAME} Password Was Reset'
            html_body = render_template('password_changed_email.html', user_name=user_name,
                                        logo=LOGO_URL, change_password_url=PROD_APP_RESET_PASSWORD_URL, app_name=APP_NAME)
            msg = Message(subject, recipients=[email], html=html_body)
            mail.send(msg)
            logger.info(f"Password changed email sent successfully - {email}")
        except Exception as e:
            logger.error(f'Error sending email: {e}')