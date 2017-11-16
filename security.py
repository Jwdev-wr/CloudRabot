from werkzeug.security import safe_str_cmp
from models.user import UserModel

## Authenticate the user
def authenticate(username, password):
    #Get user from database
    user = UserModel.find_by_username(username)
    #If user exists, and password matches return user
    if user and safe_str_cmp(user.password, password):
        return user

## Identifies user
def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)
