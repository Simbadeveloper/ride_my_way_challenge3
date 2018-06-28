import psycopg2
from flask import request, jsonify
from flask_restful import Resource
from .models import User, Ride, Request
from .db_tables import conn

cur=conn.cursor()

class Signup(Resource):
    """  Class for registration.  """

    def post(self):
        """  Method for user registration. """
        
        data=request.get_json()
        username = data['username']
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        password = data['password']
        confirmpwd = data['confirm_pwd']

        if username == " ":
            return {'message': "Username is required."}
        elif password == " ":
            return {'message': "Please provide a password!"}
        elif email == " ":
            return {'message': "email field cannot be empty."}
        elif confirmpwd == " ":
            return {'message':'please confirm the given password first'}
        elif password != confirmpwd:
            return {'message':"Passwords do not match!"}
                
        new_user = User(            
            username=username, 
            firstname=firstname, 
            lastname=lastname, 
            email=email, 
            password=password
            )

        new_user.get_user_by_username()
        if new_user.user:
            return {'message':"A user with that username exists!"},409
        if new_user.user_exists() == True:
            return{'message':'A user with that email already exists!'},409
        new_user.password_hash(password)
        new_user.register()
        usr_data = new_user.view()
        return{'message':"You have been successfully registered!", 'details':usr_data},201
    
     

class Login(Resource):
    """  Class for signing in"""

    def post(self):
        """ Method for signing in a user.  """

        data = request.get_json()
        username = data['username']
        new_password = data['password']

        if username == " ":
            return {'message': "Username is required."}
        elif new_password == " ":
            return {'message': "password field cannot be empty."}
        
        # user = User(username=username, 
        #         firstname="", 
        #         lastname="", 
        #         email="", 
        #         password="")
        # fetch users details
        cur.execute("SELECT * FROM users WHERE username='{0}';".format(username))
        user=cur.fetchone()
        #get password
        user_password=user[5]
        user_email=user[4]
        if username == user[1]:
            userd = User(username=username, 
                firstname=user[1], 
                lastname=user[2], 
                email=user_email, 
                password=user_password)
            if userd.password_verify(new_password):
                return {'message':"Successfully registered!",'email':user_email}
            return{'message':"Passwords do not match!"}
        return{'msg':"You are not registered!"}

        # user.get_user_by_username()
        # if user.user:
        #     if user.password_verify(new_password):
        #         return{'logged in'}
        #     return{'message':"wrong password"}
        # return{'mgs':"not registered"}


class Logout(Resource):
    """  Class for logging out a user.  """

    def post(self):
        """  Method for signing out a user.  """

        pass
        
class Rides(Resource):
    """  Class for Ride offers.  """

    def get(self, id=None):
        """  Method for getting ride/s"""
        pass

    def post(self, id): 
        """  Method for posting requests to a ride.  """ 

        pass


class Users(Resource):
    """  Class for handling specific user stuff.  """

    def post(self):
        """  Create ride offer.  """

        pass

    def get(self):
        """  Get ride requests created by him/her.  """
        pass

    def put(self):
        """  Method for a user to edit their ride.  """
        pass