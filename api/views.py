from flask import request, jsonify
from flask_restful import Resource
from models import User

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
        user=new_user.get_username()
        if user:
            return{'message':"user exists!"}
        new_user.register

        return{'message':"registered!"},201


         

class Login(Resource):
    """  Class for signing in"""

    def post(self):
        """ Method for signing in a user.  """

        pass

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