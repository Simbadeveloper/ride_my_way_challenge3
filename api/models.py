import os
import psycopg2

conn = psycopg2.connect(os.environ['DEV_DB_URI'])
cur = conn.cursor()

class User(object):
    """  Class for user model.  """

    def __init__(self,user_id, username, firstname, lastname, email, password):
        """  Initialising the user model objects.  """

        self.user_id = user_id
        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password
        

class Ride(object):
    """  Class for ride model.  """

    def __init__(self, ride_id, driver, destination, departure_time, route, extras):
        """  Initialising the ride model objects.  """

        self.ride_id = ride_id
        self.driver = driver
        self.destination = destination
        self.departure_time = departure_time
        self.route = route
        self.extras = extras



class Request(object):
    """  Class for request object.  """
    
    def __init__(self, user_id, ride_id):
        """  Initialising the request model objects.  """

        self.user_id = user_id
        self.ride_id = ride_id

