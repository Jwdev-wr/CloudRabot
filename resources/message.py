# Imports 
from flask_restful import Resource, reqparse
from flask_jwt import jwt_required, current_identity
from models.message import MessageModel
from flask import request

import random, string
import time


## Message classe /message
class Message(Resource):
    #Pares and set arguments for message
    parser = reqparse.RequestParser()
    parser.add_argument('message',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )
    # Set arguments for team_id
    parser.add_argument('team_id',
        type=int,
        required=True,
        help="Every team needs a team_id."
    )

    ## This Generates a random ID for the message being stored in the DB
    def random_id(self,length):
        return ''.join(random.choice(string.ascii_uppercase) for i in range(length))

    #@jwt_required()
    def get(self, team_id):
        #Get messages based on team_id
        messages = MessageModel.find_by_id(team_id)
        
        if messages.first():
            return {'messages': list(map(lambda x: x.json(), messages))}
        return {'message': 'No messages found'}, 404
    
    # Require Authentication 
    @jwt_required()
    def post(self, team_id):
        # Set data for the message before it gets placed into the database
        data = Message.parser.parse_args()
        created_at = time.time()
        created_by_user = current_identity.username
        msg_to_save = MessageModel( self.random_id(13),data['message'], data['team_id'], created_at, created_by_user)
        try:
            msg_to_save.save_to_db()
        except Exception as e:
            print e
            return {"message": "An error occurred inserting the message."}, 500
        #Will desplay message
        return msg_to_save.json(), 201


class MessageList(Resource):
    # Disabled for testing and Demonstration purposes
    #@jwt_required()
    def get(self):
        # Here I am using a lambda expression but list comprehension can be used as well
        #Ex. [x.json() for x in MessageModel.query.all()]
        return {'messages': list(map(lambda x: x.json(), MessageModel.query.all()))}
