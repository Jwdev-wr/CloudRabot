''' This is an example of how to make a request using python to the 
API. Specifically this will register you as a new user'''

import requests

url = "http://127.0.0.1:5000/register"

payload = "{\n\t\"username\":\"Name\",\n\t\"password\": \"password\",\n\t\"team_id\": 1,\n\t\"email\": \"email@email.com\"\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "df11343c-c75e-1a9b-ae54-a96351ff2b8b"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)