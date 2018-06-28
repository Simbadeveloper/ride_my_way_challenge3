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
                token = header.split('')[1]
            if token:
                user_id = User.decode_token(token)
                cur.execute("SELECT * FROM users WHERE id='{0}';".format(user_id))
                user=cur.fetchone()
                return func(user=user, *args, **kwargs)
            return {'message':"You are not logged in"}, 401
        except Exception as e:
            return {'message':"An error occured", 'error':str(e)},400
    return decorated