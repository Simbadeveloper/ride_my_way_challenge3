import json
import unittest 
from main import create_app



class Base(unittest.TestCase):
    """ Base class. """

    def setUp(self):
        """ Set up testing. """

        self.app = create_app('testing')
        self.client = self.app.test_client()
        self.user1_data={"username":"Mbish", "firstname":"Snyder", "lastname":"Mbishai", "email":"mbish@gmail.com", "password":"123456", "confirm_pwd":"123456"}
        self.user2_data={"username":"Maria", "firstname":"Mary", "lastname":"Maua", "email":"marymaua@gmail.com", "password":"1234567", "confirm_pwd":"1234567"}
        self.login_data={"username":"Mbish", "password":"123456"}
        self.ride_data={"driver":"Snyder", "destination":"Nakuru", "departure_time":"1800hrs","route":"NRB-NKR", "extras":"Be able to tolerate amazing music!! Just kidding!"}
        self.request_data={"username": "Mbish"}
        self.request_action_data={"state":"Rejected"}
        self.logout_data = {"action":"logout"}

    def tearDown(self):
        """ Clear anything that has been saved. """

        pass
    