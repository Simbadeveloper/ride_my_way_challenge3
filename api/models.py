import psycopg2
from passlib.apps import custom_app_context as pwd
from .db_tables import connect_to_db, users

conn=connect_to_db()
cur=conn.cursor()

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

    def register(self):
        """" Method for adding a verified user into the database.  """
        user = """INSERT INTO
                users  (username, firstname, lastname, email, password)
                VALUES ('%s','%s','%s','%s','%s')""" % (self.username, self.firstname, self.lastname, self.email,self.password)
        cur.execute(user)
        conn.commit()

    def get_user_by_username(self):
        """  Method for checking whether a user is in the database using username.  """
        cur.execute("SELECT * FROM users WHERE username='{0}';".format(self.username))
        self.user = cur.fetchone()

    def user_exists(self):
        cur.execute("SELECT * FROM users WHERE email='{0}';".format(self.email))
        return_data = cur.fetchone()
        if return_data:
            return True
        return False

    def view(self):
        return {
            'username':self.username,
            'email':self.email
        }

              

class Ride(object):
    """  Class for ride model.  """

    def __init__(self, driver, destination, departure_time, route, extras):
        """  Initialising the ride model objects.  """

        self.driver = driver
        self.destination = destination
        self.departure_time = departure_time
        self.route = route
        self.extras = extras

    def add_ride(self):
        """" Method for adding a ride to the database.  """
        ride = """INSERT INTO
                rides  (driver, destination, departure_time, route, extras)
                VALUES ('%s','%s','%s','%s','%s')""" % (self.driver, self.destination, self.departure_time, self.route,self.extras)
        cur.execute(ride)
        conn.commit()
        
    def ride_exists(self):
        cur.execute("SELECT * FROM rides WHERE route='{0}';".format(self.route))
        return_data = cur.fetchone()
        if return_data:
            return True
        return False


class Request(object):
    """  Class for request object.  """
    
    def __init__(self, user_id, ride_id):
        """  Initialising the request model objects.  """

        self.user_id = user_id
        self.ride_id = ride_id

