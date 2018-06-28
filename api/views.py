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

class Logout(Resource):
    """  Class for logging out a user.  """

    def post(self):
        """  Method for signing out a user.  """

        pass
        
class Rides(Resource):
    """  Class for Ride offers.  """

    def getone(self, ride_id=None):
        """  Method for getting ride/s"""

        #get a single offer
        if id:
            cur.execute("SELECT * FROM rides WHERE id='{0}';".format(ride_id))
            ride=cur.fetchone()
            if ride:
                return{'ride_id':ride[0],
                        'driver':ride[1],
                        'destination':ride[2],
                        'departure_time':ride[3],
                        'route':ride[4],
                        'extra':ride[5]
                        }
            return{'message':'Ride does not exist!'}

    def post(self, ride_id): 
        """  Method for posting requests to a ride.  """ 

        data=request.get_json()
        username=data['username']
        status=data['status']
        cur.execute("SELECT * FROM users WHERE username='{0}';".format(username))
        user=cur.fetchone()
        user_id=user[0]
        ride_id=ride_id

        new_request=Request( user_id=user_id,ride_id=ride_id, status=status)

        new_request.add_request()

        return{'message':"Request has been placed successfully!"}


class GetAllRides(Resource):

        def get(self):
            #get all
            cur.execute("SELECT * FROM rides ;")
            rides=cur.fetchall()
            return{'rides':rides} 


class Users(Resource):
    """  Class for handling specific user stuff.  """

    def post(self):
        """  Create ride offer.  """

        data = request.get_json()
        driver = data['driver'] 
        destination = data['destination']
        departure_time = data['destination']
        route = data['route']
        extras = data['extras']

        new_ride=Ride(
            driver=driver, 
            destination=destination, 
            departure_time=departure_time, 
            route=route, 
            extras=extras)

        if driver == " ":
            return {'message': "field cannot be empty"}
        elif destination == " ":
            return {'message':"provide the destination point"}
        elif departure_time == " ":
            return {'message':"please provide the departure time"}
        elif route == " ":
            return{'message':"What route will we be taking?"}
        elif extras == " ":
            return {'message':"Are you sure you have nothing else to add?"}
        
        cur.execute("SELECT * FROM rides WHERE route='{0}';".format(route))
        rd = cur.fetchone()
        if rd:
            if rd[4]==route and rd[3]==departure_time:
                return{'message':"You hare a ride going that way at that time."}
            return{'message':"No overlaps for you"}

        if new_ride.ride_exists() == True:
            return{'message':'ride exists!'},409


        new_ride.add_ride()

        return{'message':"Ride offer successfully created"},201

    def get(self):
        """  Get ride requests created by him/her.  """
        pass

    def put(self):
        """  Method for a user to edit their ride.  """
        pass