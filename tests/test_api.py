import json

import sys  # handle imports
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from base import Base

class TestRegistration(Base):
    """  Class for testing user registration.  """

    def test_successful_user_registration(self):         
        """  Method for testing that registration of a user goes through successfully.  """

        response = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_user_already_exists(self): 
        """  Method for testing that registration of a user is only once.  """

        response1 = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user_data), content_type='application/json') 
        response2 = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user_data), content_type='application/json')
        result = json.loads(response2.data)
        self.assertEqual(result['message'],"already registered, please login to continue.")
    
    def test_username_field_not_empty(self):
        """  Method for testing that a user provides a username before proceeding.  """

        self.user_data={"username":" ", "firstname":"Snyder", "lastname":"Mbishai", "email":"mbish@gmail.com", "password":"123456", "confirm_pwd":"123456"}
        response = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user_data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'],"Username is required.")
    
    def test_password_field_not_empty(self):
        """   Method for testing that a user provides a provides a password before proceeding.  """
        self.user_data={"username":"Mbish", "firstname":"Snyder", "lastname":"Mbishai", "email":"mbish@gmail.com", "password":" ", "confirm_pwd":"123456"}
        response = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user_data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'],"Please provide a password!")

class TestLogin(Base):
    """  Class for testing user login.  """

    def test_successful_user_login(self):         
        """  Method for testing that login of a user goes through successfully.  """

        response = self.client.post('/api/v2/auth/login',data=json.dumps(self.login_data), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_username_field_not_empty(self):
        """  Method for testing a user does not leave the username field empty.  """

        response1 = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user1_data), content_type='application/json')
        self.login_data={"username":" ", "password":"123456"}
        response = self.client.post('/api/v2/auth/login',data=json.dumps(self.login_data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'],"Username is required.")
    
    def test_password_field_not_empty(self):
        """  Method for testing that a user provides a password for login.  """

        response1 = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user1_data), content_type='application/json')
        self.login_data={"username":"Mbish", "password":" "}
        response = self.client.post('/api/v2/auth/login',data=json.dumps(self.login_data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(result['message'],"password field cannot be empty.")

    def test_wrong_password(self):
        """  Method for testing whether the provided password is wrong.  """
        
        response1 = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user1_data), content_type='application/json')
        self.login_data = {"username":"Mbish", "password":"mmmmmmm"}
        response2 = self.client.post('/api/v2/auth/login',data=json.dumps(self.login_data), content_type='application/json')
        result = json.loads(response2.data)
        self.assertEqual(result['message'],"Wrong password!")

class TestRide(Base):
    """  Class for testing ride offers.  """



    def test_fetch_single_ride_offer(self):
        """  Method for testing a single ride offer is fetched.  """

        response1 = self.client.post('/api/v2/rides', data=json.dumps(self.ride_data), content_type='application/json')
        response2 = self.client.get('/api/v2/rides/1', content_type='application/json')
        self.assertEqual(response2.status_code,200)

    def test_fetch_all_ride_offers(self):
        """  Method for testing all ride offers can be fetched.  """

        response1 = self.client.post('/api/v2/rides', data=json.dumps(self.ride_data), content_type='application/json')
        response2 = self.client.get('/api/v2/rides', content_type='application/json')
        self.assertEqual(response2.status_code,200)  

    def test_delete_ride_offer(self):
        """  Method for deleting a ride offer.  """
        response1 = self.client.post('/api/v2/rides', data=json.dumps(self.ride_data), content_type='application/json')
        response2 = self.client.delete('/api/v2/rides/1', content_type='application/json')
        result = json.loads(response2.data)
        self.assertEqual(result['message'],"Successfully deleted ride!")

    def test_request_to_join_a_ride(self):
        """  Method for testing a ride request is successfully placed.  """

        response1 = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user1_data), content_type='application/json')        
        response = self.client.post('api/v2/rides/1/requests', data=json.dumps(self.request_data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code,201) 
        self.assertEqual(result['message'],"The request has been made. Please wait for feedback from the driver.")


class TestUser(Base):
    """  Class for testing user workings. """

    def test_successful_ride_creation(self):
        """  Method for testing that a ride is created successfully.  """

        response = self.client.post('/api/v2/users/rides', data=json.dumps(self.ride_data), content_type='application/json')
        result = json.loads(response.data)
        self.assertEqual(response.status_code,201)
        self.assertEqual(result['message'],"Ride offer successfully created!")

    def test_user_can_get_requests_to_their_rides(self):
        """  Method for testing that a user can get rides that they have created.  """

        response1 = self.client.post('/api/v2/users/rides', data=json.dumps(self.ride_data), content_type='application/json')
        response2 = self.client.post('api/v2/rides/1/requests', data=json.dumps(self.request_data), content_type='application/json')
        response3 = self.client.get('/api/v2/users/1/requests')
        result = json.loads(response3.data)
        self.assertEqual(result.status_code, 200)

    def test_users_can_respond_to_requests_their_rides(self):
        """  Method for testing that a user can edit their own rides.  """
        response1 = self.client.post('/api/v2/users/rides', data=json.dumps(self.ride_data), content_type='application/json')
        response2 = self.client.post('api/v2/rides/1/requests', data=json.dumps(self.request_data), content_type='application/json')
        response3 = self.client.post('/api/v2/users/rides/1/requests/1', data=json.dumps(self.request_action_data), content_type='application/json')
        self.assertEqual(response3.status_code,200)
        pass

class TestLogout(Base):
    """  Class for testing logout.  """

    def test_logout(self):
        """  Method for testing that a user is successfully logged out.  """

        response1 = self.client.post('/api/v2/auth/signup',data=json.dumps(self.user1_data), content_type='application/json')
        response2 = self.client.post('/api/v2/auth/login',data=json.dumps(self.login_data), content_type='application/json')
        response3 = self.client.post('/api/v2/auth/logout',data=json.dumps(self.logout_data), content_type='application/json')
        result = json.loads(response3.data)
        self.assertEqual(result['message'],"Successfully logged out!")

