# Import SQLAlchemy Database
from db import db

# TeamModel Class
class TeamModel(db.Model):
    #Set database name
    __tablename__ = 'teams'

    #Define Columns
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80))

    # Establish Relationship between models
    messages = db.relationship('MessageModel', lazy='dynamic')

    # Initilize
    def __init__(self, name):
        self.name = name

    #Format data into JSON
    def json(self):
        return {'name': self.name, 'messages': [message.json() for message in self.messages.all()]}
    
    # Eliminates creating an instance first
    @classmethod
    def find_by_name(cls, name):
        return cls.query.filter_by(name=name).first()

    # Save to database
    def save_to_db(self):
        db.session.add(self)
        db.session.commit()

    # Deletes from database
    def delete_from_db(self):
        db.session.delete(self)
        db.session.commit()
