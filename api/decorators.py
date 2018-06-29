from functools import wraps
from flask import request
from .models import Ride, Request, User
from .db_tables import connect_to_db

conn=connect_to_db()
cur=conn.cursor()

def user_token_required(func):
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        try:
            header = request.headers.get('Authorization')
            if header:
                token = header.split(' ')[1]
            if token:
                username = User.decode_token(token)
                cur.execute("SELECT * FROM users WHERE username='{0}';".format(username))
                user=cur.fetchone()
                if user:
                    return func(*args, **kwargs)
                return{'You are not a user'}
            return {'message':"If a user, make sure you login to get token."}, 401
        except Exception as e:
            return {'message':"An error occured", 'error':str(e)},400
    return decorated