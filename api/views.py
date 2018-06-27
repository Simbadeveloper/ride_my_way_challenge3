from flask import request, jsonify
from flask_restful import Resource

class Signup(Resource):
    """  Class for registration.  """

    def post(self):
        """  Method for user registration. """

        pass 

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
        """  Get rides created by him/her.  """
        pass

    def put(self):
        pass