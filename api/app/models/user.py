from app.extensions import db
from datetime import datetime
from enum import Enum as UserEnum

class UserType(UserEnum):
    FREE_TRAIL = 'Free'
    SUBSCRIPTION = 'Subscribed'

class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    uid = db.Column(db.String(36), unique=True, nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=True)
    joined_date = db.Column(db.DateTime, default=datetime.utcnow)
    email_is_verify = db.Column(db.Boolean, default=False)
    phone_number = db.Column(db.String(20), unique=True, nullable=True)
    credits = db.Column(db.Integer, default=10)
    confirmation_token = db.Column(db.String(1000))
    subscription = db.Column(db.Enum(UserType), default=UserType.FREE_TRAIL)
    given_name = db.Column(db.String(20), unique=False, nullable=True)
    family_name =db.Column(db.String(20), unique=False, nullable=True)
    
    # Joined date formatted
    def joined_date_formatted(self):
        return self.user_joined_date.strftime('%Y-%m-%d')
    
    # UserApiKeys
    api_keys = db.relationship('UserApiKeys', backref='user', lazy=True, cascade="all, delete-orphan")

    def __repr__(self):
        return f'<User {self.user_email}>'
    
class UserApiKeys(db.Model):
    __tablename__ = 'keys'

    id = db.Column(db.Integer, primary_key=True)
    key = db.Column(db.String(80), nullable=True)

    # ForeignKey user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id', ondelete="CASCADE"))

    def __repr__(self):
        return f"Keys(id={self.id}')"
    


