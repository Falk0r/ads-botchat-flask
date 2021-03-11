import jwt
from datetime import datetime, timedelta
from models.users import findUser
from keys import keys

def toLog(user):
    """
    Try to log user with email and password
    """
    register = findUser(user["email"])
    if register:
        if user["password"] == register["password"]:
            return encode_auth_token(register)
        else:
            return False

def encode_auth_token(user):
    """
    Encode and return token for a login user
    """
    try:
        payload = {
            'exp' : datetime.utcnow() + timedelta(hours=1),
            'iat' : datetime.utcnow(),
            'userName' : user['name'],
            'userEmail' : user['email']
        }
        return jwt.encode(
            payload,
            keys.secret,
            algorithm='HS256'
        )
    except Exception as e:
        return e

def decode_auth_token(token):
    """
    Decode and return payload from token
    """
    print(token)
    try:
        return jwt.decode(
            token,
            keys.secret,
            algorithms='HS256'
        )
    except Exception as e:
        return e