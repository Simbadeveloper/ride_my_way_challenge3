import psycopg2
from flask import request, jsonify
from flask_restful import Resource
from .models import User, Ride, Request
from .db_tables import conn
from .decorators import user_token_required

cur=conn.cursor()
#pylint: disable=E1305

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
            return {'message': "Username is required."},400 #bad request
        elif password == " ":
            return {'message': "Please provide a password!"},400
        elif email == " ":
            return {'message': "email field cannot be empty."},400
        elif confirmpwd == " ":
            return {'message':'please confirm the given password first'},400
        elif password != confirmpwd:
            return {'message':"Passwords do not match!"},409 #conflict
                
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
            return {'message': "Username is required."},400
        elif new_password == " ":
            return {'message': "password field cannot be empty."},400

        cur.execute("SELECT * FROM users WHERE username='{0}';".format(username))
        user=cur.fetchone()
        #get password
        user_password=user[5]
        user_email=user[4]
        user_id=user[0]
        if username == user[1]:
            userd = User(username=username, 
                firstname=user[1], 
                lastname=user[2], 
                email=user_email, 
                password=user_password)
            if userd.password_verify(new_password):
                token=userd.generate_token(user_id)
                if token:
                    result = {
                        'username':userd.username,
						'message':'Successfully logged in',
						'user_token':token.decode()
                        }
                    return{'result':result}, 200 #ok
                return{'message':"OOpsy!!Failed to generate token."},401 #unauthorized            
            return{'message':"Wrong password!"},401
        return{'msg':"You are not registered!"},401

class Logout(Resource):
    """  Class for logging out a user.  """

    def post(self):
        """  Method for signing out a user.  """

        pass
        
class Rides(Resource):
    """  Class for Ride offers.  """

    def get(self, ride_id=None):
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
                        },200
            return{'message':'Ride does not exist!'},404

    def post(self, ride_id): 
        """  Method for posting requests to a ride.  """ 

        data=request.get_json()
        username=data['username']
        status=data['status']
        cur.execute("SELECT * FROM users WHERE username='{0}';".format(username))
        user=cur.fetchone()
        if user:
            new_request=Request(username=username,ride_id=ride_id, status=status)
            new_request.add_request()

            return{'message':"The request has been made. Please wait for feedback from the driver."},201
        return{'message':"Invalid Username"},404


class GetAllRides(Resource):
    """  Class for getting all rides.  """

    def get(self):
        """  Method for getting all rides.  """

        cur.execute("SELECT * FROM rides ;")
        rides=cur.fetchall()
        if rides:
            return{'rides':rides},200 
        return{'message':"There are no rides at the moment"},404


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
            return {'message': "field cannot be empty"},400
        elif destination == " ":
            return {'message':"provide the destination point"},400
        elif departure_time == " ":
            return {'message':"please provide the departure time"},400
        elif route == " ":
            return{'message':"What route will we be taking?"},400
        elif extras == " ":
            return {'message':"Are you sure you have nothing else to add?"},400
        
        cur.execute("SELECT * FROM rides WHERE route='{0}';".format(route))
        rd = cur.fetchone()
        if rd:
            if rd[4]==route and rd[3]==departure_time:
                return{'message':"You have a ride going that way at that time."},409
            return{'message':"No overlaps for you"},200

        if new_ride.ride_exists() == True:
            return{'message':'ride exists!'},409


        new_ride.add_ride()

        return{'message':"Ride offer successfully created"},201

    def get(self,ride_id):
        """  Get ride requests created by him/her.  """

        cur.execute("SELECT * FROM requests WHERE ride_id='{0}';".format(ride_id))
        rqs = cur.fetchall()
        return {'requests':rqs},200
        

    def put(self, ride_id, rqt_id):
        """  Method for a user to respond to requests made to their ride offers.  """

        data=request.get_json()
        status=data['status']

        # #get rides first
        # cur.execute("SELECT * FROM requests WHERE ride_id='{0}';".format(ride_id))
        # rqs = cur.fetchall()

        # #choose the request that you you want to respond to using the id 
        # cur.execute("SELECT * FROM requests id='{0}';".format(rqt_id))
        # rqs = cur.fetchone()

        cur.execute("UPDATE requests SET status='{0}' WHERE id='{0}';".format(status,rqt_id))
        # conn.commit()

        #View updated
        cur.execute("SELECT * FROM requests id='{0}';".format(rqt_id))
        rqs = cur.fetchone()
        
        return {'msg':"updated", 'request_status':rqs[3]},200








        