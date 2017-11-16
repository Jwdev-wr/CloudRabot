# Cloud Rabot Api  
This a general purpose API to be used with White RaBot products. It utilizes Flask, and the Flask-Restful framework and JWT authentication.

This application requires Python 2.7


#Instructions:

Out of the box there are 6 built endpoints for demonstration

1. /auth for authenticating 
2. /register for registering
3. /message/<team_id> and /messages for adding, and viewing messages
4. /team and /teamList 

Please take a look at exRequest.py to see how you can make a request using python to this API

You will need to pass the parameters in for authentication in the headers of the requests. (PostMan is an excellent application for this.) 
