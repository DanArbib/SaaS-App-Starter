from flask import Flask, request
from .extensions import db
from dotenv import load_dotenv
import pika
import stripe
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from authlib.integrations.flask_client import OAuth
from pythonjsonlogger import jsonlogger
from .models.user import User
from flask_bcrypt import Bcrypt
from prometheus_flask_exporter import PrometheusMetrics
from flask_mail import Mail
from flask_cors import CORS

load_dotenv()

# Flask
FLASK_SECRET_KEY = os.environ.get('FLASK_SECRET_KEY')
APP_NAME = os.environ.get('APP_NAME')

# Postgres
POSTGRES_DB = os.environ.get('POSTGRES_DB')
PG_HOST = os.environ.get('PG_HOST')
POSTGRES_USER = os.environ.get('POSTGRES_USER')
POSTGRES_PASSWORD = os.environ.get('POSTGRES_PASSWORD')
PG_PORT = os.environ.get('PG_PORT', 5432)

# Mail
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
MAIL_SENDER_NAME = os.environ.get('MAIL_SENDER_NAME')

# APP
PROD_APP_URL = os.environ.get('PROD_APP_URL')

# RabbitMQ
RABBITMQ_HOST = os.environ.get('RABBITMQ_HOST')
RABBITMQ_PORT = int(os.environ.get('RABBITMQ_PORT'))
RABBITMQ_DEFAULT_USER = os.environ.get('RABBITMQ_DEFAULT_USER')
RABBITMQ_DEFAULT_PASS = os.environ.get('RABBITMQ_DEFAULT_PASS')

# Google Auth
GOOGLE_CLIENT_ID = os.environ.get('GOOGLE_CLIENT_ID')
GOOGLE_CLIENT_SECRET = os.environ.get('GOOGLE_CLIENT_SECRET')

# Stripe
STRIPE_SECRET_KEY = os.environ.get('STRIPE_SECRET_KEY')

# Flask config
app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

# CORS config
CORS(app, resources={
    r"/*": {
        "origins": ["http://127.0.0.1:8080", "http://localhost:8080", "http://127.0.0.1", os.environ.get('PROD_APP_URL')],
        "methods": ["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

# Oauth config
oauth = OAuth()
oauth.register(
    name='google',
    client_id=GOOGLE_CLIENT_ID,
    client_secret=GOOGLE_CLIENT_SECRET,
    server_metadata_url='https://accounts.google.com/.well-known/openid-configuration',
    client_kwargs={
        'scope': 'openid email profile'
    }
)
oauth.init_app(app)

# Bcrypt config
bcrypt_app = Bcrypt(app)

# Logger config
logger = logging.getLogger(APP_NAME)
logger.setLevel(logging.INFO)
log_handler = TimedRotatingFileHandler("./app/logs/app.log", when="midnight", interval=1, backupCount=30)
formatter = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
logger.propagate = True

# Prometheus metrics config
metrics = PrometheusMetrics(app)
metrics.info('app', 'Application info', version='1.0.3')
metrics.register_default(
    metrics.counter(
        'by_path_counter', 'Request count by request paths',
        labels={'path': lambda: request.path}
    )
)

# Postgres URI config
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{PG_HOST}:{PG_PORT}/{POSTGRES_DB}"

# Email config
app.config['MAIL_SERVER'] = MAIL_SERVER
app.config['MAIL_PORT'] = MAIL_PORT
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
app.config['MAIL_USERNAME'] = MAIL_USERNAME
app.config['MAIL_PASSWORD'] = MAIL_PASSWORD
app.config['MAIL_DEFAULT_SENDER'] = (MAIL_SENDER_NAME, MAIL_DEFAULT_SENDER)
app.config['MAIL_SUPPRESS_SEND'] = False
app.config['MAIL_ASCII_ATTACHMENTS'] = False
mail = Mail(app)

# # RabbitMQ config
# credentials = pika.PlainCredentials(username=RABBITMQ_DEFAULT_USER, password=RABBITMQ_DEFAULT_PASS)
# rmq_connection = pika.BlockingConnection(
#     pika.ConnectionParameters(heartbeat=10, host=RABBITMQ_HOST, port=RABBITMQ_PORT, credentials=credentials))
# rabbitmq = rmq_connection.channel()

# Stripe
stripe.api_key = STRIPE_SECRET_KEY

# Database initialization
db.init_app(app)
with app.app_context():
    db.create_all()

# Import routes
from app import routes