''' This application was developed as a general purpose 
API to be used by White RaBot for testing and business purposes '''


__title__ = 'Cloud RaBot Api'
__author__ = 'Jacob Weeks'
__license__ = 'MIT'
__copyright__ = 'Copyright 2017, Jacob Weeks'


## Import all of our required libraries 
from flask import Flask, render_template, redirect, url_for, request
from flask_restful import Api
from flask_jwt import JWT
from db import db
from security import authenticate, identity
from resources.user import UserRegister
from resources.message import Message, MessageList
from resources.team import Team, TeamList

### Initilize App
application = Flask(__name__)
# Configure DB
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# Security Key
application.secret_key = 'ImMrMeeseeksLookAtMee'
# Connect to restful
api = Api(application)
# Connect to DB
db.init_app(application)


### Creates the table on first request if does not exist
@application.before_first_request
def create_tables():
    db.create_all()

#Create auth endpoint
jwt = JWT(application, authenticate, identity)  # /auth

# Team End Points
api.add_resource(Team, '/team/<string:name>')
api.add_resource(TeamList, '/teams')

## Messages Endpoint
api.add_resource(Message, '/message/<string:team_id>')
api.add_resource(MessageList, '/messages')

## Registration Endpoint    
api.add_resource(UserRegister, '/register')

#Index Route
@application.route("/")
def index():
    return render_template('index.html')

if __name__ == '__main__':
    #Run when app called
    application.run(debug=True)