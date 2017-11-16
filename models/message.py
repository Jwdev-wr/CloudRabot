#import the SQLAlchemy db
from db import db

class MessageModel(db.Model):
    # Set table name
    __tablename__ = 'messages'

    #Define the columns
    id = db.Column(db.Integer, primary_key=True)
    message_id = db.Column(db.String(140))
    message = db.Column(db.String(80))
    created_at = db.Column(db.Float)
    created_by_user = db.Column(db.String(20))


    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'))
    #Create a relationship between the classes
    team = db.relationship('TeamModel')

    #Initialize
    def __init__(self, message_id, message, team_id, created_at, created_by_user):
        self.message_id = message_id
        self.message = message
        self.team_id = team_id
        self.created_at = created_at
        self.created_by_user = created_by_user

    #Formats into json
    def json(self):
        return {'message_id': self.message_id, 'team_id': self.team_id, 'message':self.message, 'created at': self.created_at, 'creator':self.created_by_user}
    
    # Eliminates creating an instance first
    @classmethod
    def find_by_id(cls, team_id):
        return cls.query.filter_by(team_id=team_id)
    
    #Saves to db
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    #Deletes from db
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
