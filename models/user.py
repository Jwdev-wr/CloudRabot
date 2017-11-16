# Import SQLAlchemy Database
from db import db

#Create User class
class UserModel(db.Model):
    # Set table name for db
    __tablename__ = 'users'

    #Define columbs
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80))
    password = db.Column(db.String(80))
    team_id = db.Column(db.Integer)

    #Initialize 
    def __init__(self, username, password, team_id):
        self.username = username
        self.password = password
        self.team_id = team_id

    #Save to database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    #Find user by username
    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()
    
    #Find user by id
    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()
