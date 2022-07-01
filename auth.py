from flask import jsonify, request
from app import app, bcrypt
from functools import wraps
from services import *
from jwtUtil import *
from utils import *

def get_jwt_claims():
    token = request.headers['Authorization'][7:]
    return jwtDecode(token, app.config['SECRET_KEY'], algorithms=["HS256"])


# decorator for verifying the JWT
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        # jwt is passed in the request header
        if 'Authorization' in request.headers:
            token = request.headers['Authorization'][7:] # remove 'Bearer '

        if not token:
            return jsonify({MESSAGE : NO_ACCESS_TOKEN}), UNAUTHORIZED

        try:
            # try decode
            jwtDecode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
            
        except jwt.ExpiredSignatureError:
            return jsonify({MESSAGE : TOKEN_EXPIRED}), UNAUTHORIZED
        except jwt.JWTClaimsError:
            return jsonify({MESSAGE : TOKEN_CLAIMS_ERROR}), UNAUTHORIZED
        except:
            return jsonify({MESSAGE : INVALID_ACCESS_TOKEN}), UNAUTHORIZED
        return f(*args, **kwargs)
  
    return decorated


# decorator for verifying role
def manager_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        claims = get_jwt_claims()
        if claims[ROLE] == MANAGER:
            return f(*args, **kwargs)
        else:
            return jsonify({MESSAGE : NO_PERMISSION}), UNAUTHORIZED

    return decorated


def authenticate(pwd_hash, password):
    return bcrypt.check_password_hash(pwd_hash, password) # returns True
        
def generatePWDHash(password):
    return bcrypt.generate_password_hash(password) # return bcrypt hash