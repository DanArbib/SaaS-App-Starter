from functools import wraps
from flask import jsonify, request
from app.models.user import User
# from app import metrics, logger
import jwt, os
from prometheus_client import Counter

user_access_counter = Counter('user_access', 'Count of user accesses', ['user'])

def validate_jwt(f):
    @wraps(f)
    def _verify(*args, **kwargs):
        invalid_msg = {
            'message': 'Invalid token. Registration or authentication required',
            'authenticated': False
        }
        expired_msg = {
            'message': 'Expired token.',
            'authenticated': False
        }
        auth_headers = request.headers.get('Authorization', '').split()
        if len(auth_headers) != 2:
            return jsonify(invalid_msg), 401

        try:
            token = auth_headers[1]
            data = jwt.decode(token, os.environ.get('JWT_SECRET_KEY'), algorithms=['HS256'])
            user = User.query.filter_by(id=data['user_id']).first()

            if not user:
                raise RuntimeError('User not found')
            
            # logger.info(f"User {user.email} is accessing {request.path}")
            user_access_counter.labels(user=user.email).inc()

            return f(user, *args, **kwargs)
        except jwt.ExpiredSignatureError:
            return jsonify(expired_msg), 401
        except (jwt.InvalidTokenError, Exception) as e:
            print(e)
            return jsonify(invalid_msg), 401

    return _verify
