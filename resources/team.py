#Imports
from flask_restful import Resource, reqparse
from models.team import TeamModel

#Create Team class which inherits from Resource 
class Team(Resource):
    # Get team
    def get(self, name):
        team = TeamModel.find_by_name(name)
        if team:
            return team.json()
        return {'message': 'Store not found'}, 404
    
    #Create Team
    def post(self, name):
        if TeamModel.find_by_name(name):
            return {'message': "A team with name '{}' already exists.".format(name)}, 400

        team = TeamModel(name)
        try:
            team.save_to_db()
        except:
            return {"message": "An error occurred creating the team."}, 500

        return team.json(), 201
    #Delete team    
    def delete(self, name):
        team = TeamModel.find_by_name(name)
        if team:
            team.delete_from_db()

        return {'message': 'Team deleted'}

#This returns a list of teams
class TeamList(Resource):
    def get(self):
        # Here I am using a lambda expression but list comprehension can be used as well
        #Ex. [x.json() for x in TeamModel.query.all()]
        return {'teams': list(map(lambda x: x.json(), TeamModel.query.all()))}
