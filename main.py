from flask import Flask
from flask_restful import Api
from api.views import Signup, Login, Rides, Users, Logout

from config import configurations

def create_app(configuration):
    """  Method for creating the flask app.  """

    app = Flask(__name__)

    app.config.from_object(configurations[configuration])
     
    api = Api(app)

    api.add_resource(Signup, '/api/v2/auth/signup')
    api.add_resource(Login, '/api/v2/auth/login')
    api.add_resource(Logout, '/api/v2/auth/logout')
    api.add_resource(Rides, '/api/v2/rides', 
                        '/api/v2/rides/<int:ride_id>', 
                        '/api/v2/rides/<int:ride_id>/requests')
    api.add_resource(Users, '/api/v2/users/rides',
                            '/api/v2/users/rides/<int:ride_id>/requests', 
                            '/api/v2/users/rides/<int:ride_id>requests/<int:request_id>')

        
    return app


app = create_app('development')

