import json
import unittest 
from main import create_app
import psycopg2
from api.db_tables import connect_to_db, users, rides
conn=connect_to_db() 
cur=conn.cursor()

class Base(unittest.TestCase):
    """ Base class. """

    def setUp(self):
        """ Set up testing. """

        self.app = create_app('testing')
        self.client = self.app.test_client()        
        self.user1_data={"username":"Kyalo", "firstname":"NANA", "lastname":"Emoji", "email":"kyalo@gmail.com", "password":"123456444", "confirm_pwd":"123456444"}
        self.user2_data={"username":"Gloria", "firstname":"Mary", "lastname":"Maua", "email":"gloriaa@gmail.com", "password":"123456789", "confirm_pwd":"1234567789"}
        self.login_data={"username":"Mbish", "password":"123456"}
        self.ride_data={"driver":"Kyalo", "destination":"Mombasa", "departure_time":"1200hrs","route":"Mombasaroad", "extras":"Be able to tolerate amazing music!! Just kidding!"}
        self.request_data={"username": "Gloria", "status":"open"}
        self.request_action_data={"state":"Rejected"}
        self.logout_data = {"action":"logout"}

    def tearDown(self):
        """ Clear anything that has been saved. """
        
        # cur.execute("TRUNCATE TABLE users, rides, requests;")
    #     conn.commit()
    #     conn.close()
       

        pass
    