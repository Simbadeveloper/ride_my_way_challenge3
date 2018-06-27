from passlib.apps import custom_app_context as pwd

import sys  # handle imports
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import con

cur = con.cursor()

class User(object):
    """  Class for user model.  """

    def __init__(self, username, firstname, lastname, email, password):
        """  Initialising the user model objects.  """

        self.username = username
        self.firstname = firstname
        self.lastname = lastname
        self.email = email
        self.password = password

    def password_hash(self, password):
        self.password = pwd.encrypt(password)
    
    def password_verify(self, password):
        return pwd.verify(password, self.password)

    def get_username(self):
        cur.execute("SELECT * FROM users WHERE email='{0}';".format(self.email))
        self.user = cur.fetchone()

    def register(self):
        """  Adding a user into the db. """
        user = """ INSERT INTO users (username, firstname, lastname, email, password)
            VALUES (%s,%s,%s,%s,%s)""" % (self.username, self.firstname, self.lastname, self.email,self.password)
        #create the user in the db
        cur.execute(user)
        #commit the changes: makes them persistent
        con.commit()
        

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

