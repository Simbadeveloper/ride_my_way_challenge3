[![Build Status](https://travis-ci.org/SnyderMbishai/ride_my_way_challenge3.svg?branch=develop)](https://travis-ci.org/SnyderMbishai/ride_my_way_challenge3)
[![Coverage Status](https://coveralls.io/repos/github/SnyderMbishai/ride_my_way_challenge3/badge.svg)](https://coveralls.io/github/SnyderMbishai/ride_my_way_challenge3)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintainability](https://api.codeclimate.com/v1/badges/2c227c39c50557014ffa/maintainability)](https://codeclimate.com/github/SnyderMbishai/ride_my_way_challenge3/maintainability)

# ride_my_way_challenge3

This repository is for the RideMyWay carpooling application APIs and testing with database integration.

RideMyWay is a carpooling application.

## Functionality

1. Signup
2. Login
3. Create ride offers
4. Get ride/s
5. Edit rides
6. Delete ride
6. Place ride requests
7. view requests that have been placed on one's ride offers
8. Respond to the requests

___________________________________________________________________________________________________

## Technologies
Ensure you have the following installed and running
1. Python ()
2. Postgresql
2. Flask framework
3. Pytest
4. Postman

#### Installations

Ensure all the above are installed

## Setting up 
* create a virtual environment

        $ virtualenv venv

* git clone this repo into the virtual environment

       $ cd venv
       $ git clone https://github.com/SnyderMbishai/ride_my_way_challenge3.git

* cd to the app

       $ cd ride_my_way_challenge3
       $ source env/bin/activate
       $ git install -r requirements.txt
       $ set FLASK_APP=run.py
       $ set APP_SECRET_KEY=anythingunique
       
### Running the APP and testing
* To run the app:

       $ flask run

* copy the given url(http://127.0.0.1:5000/) and post it on postman

### Endpoints

* To test the endpoints, from the table bellow, copy the endpoint and add it to the url.

Endpoint                          | description         | Method
----------------------------------|---------------------|--------
/api/v2/users/rides               | Ride creation       | POST
/api/v2/rides                     | get all rides       | GET
/api/v2/rides/<int:id>            | get a specific ride | GET
/api/v2/rides/<int:id>/request    | post a reuest       | POST
/api/v2/auth/signup               | registration        | POST
/api/v2/auth/login                | login               | POST
/api/v2/users/rides/
<int:ride_id>/requests            | view requests       | GET
/api/v2/users/rides/
<int:ride_id>requests/<int:rqt_id>| respond to request  | PUT

#### Example
* To register:

    - select POST on the dropdown option before the url.

    - add /api/v2/auth/signup to the url

    - on headers, 

            key: Content-Type
            value: application/json

    - on body, select raw and add your details. example:

            {
            "username":"SnyderMbishai",
            "firstname":"snyder",
            "lastname": "Mbishai",
            "email":"csmbishai@gmail.com",
            "password":"123456789",
            "confirm_pwd":"123456789"
            }

    - click send. You get 201 status code and a message that says:

            {
            "Message": "Successfully registered."
            }

## Tests and coverage

* Follow the steps above to before **Endpoints**
* If the app is already running:

         * ctrl + c to stop the app on the terminal

* To test the tests and see coverage as well, run:

         $ py.test --cov tests

## Author

        Snyder Mbishai

## Licensing

The project is licensed with MIT license, view the licence.txt in the app.

### Contributions

Feel free to contribute by forking the repo and creating a PR.