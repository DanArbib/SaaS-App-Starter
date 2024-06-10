from flask import Flask
from .extensions import db
from dotenv import load_dotenv
import os
import logging
from logging.handlers import TimedRotatingFileHandler
from pythonjsonlogger import jsonlogger
from .models.user import User
from flask_bcrypt import Bcrypt
from prometheus_flask_exporter import PrometheusMetrics
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

# Flask config
app = Flask(__name__)
app.secret_key = FLASK_SECRET_KEY

# Configure logger
logger = logging.getLogger(APP_NAME)
logger.setLevel(logging.INFO)
log_handler = TimedRotatingFileHandler("./app/logs/app.log", when="midnight", interval=1, backupCount=30)
formatter = jsonlogger.JsonFormatter('%(asctime)s %(name)s %(levelname)s %(message)s')
log_handler.setFormatter(formatter)
logger.addHandler(log_handler)
logger.propagate = True

# Bcrypt config
bcrypt_app = Bcrypt(app)

# Prometheus metrics config
logger.info('Initializing Prometheus metrics')
metrics = PrometheusMetrics(app)
metrics.info('app', 'Application info', version='1.0.3')

# Postgres URI config
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql+psycopg2://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{PG_HOST}:{PG_PORT}/{POSTGRES_DB}"

# Database initialization
logger.info('Initializing database')
db.init_app(app)
with app.app_context():
    db.create_all()

# Import routes
logger.info('Importing routes')
from app import routes