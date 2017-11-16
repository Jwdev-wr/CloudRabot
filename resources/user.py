#Imports
from flask_restful import Resource, reqparse
from models.user import UserModel

#Create register user class
class UserRegister(Resource):
    #Parse and set argument requirements
    parser = reqparse.RequestParser()
    parser.add_argument('username',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    #Password parse and arguments
    parser.add_argument('password',
        type=str,
        required=True,
        help="This field cannot be blank."
    )
    #Team_id parse and arguments
    parser.add_argument('team_id',
        type=int,
        required=True,
        help="This field cannot be blank."
    )

    #Register a new user    
    def post(self):
        data = UserRegister.parser.parse_args()

        if UserModel.find_by_username(data['username']):
            return {"message": "A user with that username already exists"}, 400

        user = UserModel(data['username'], data['password'], data['team_id'])
        user.save_to_db()

        return {"message": "User created successfully."}, 201
