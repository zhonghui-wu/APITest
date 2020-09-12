import requests
from lib.host import HOST

header = {"Content-Type":"application/x-www-form-urlencoded"}
payload = {"username":"auto","password":"sdfsdfsdf"}
response =requests.post(f'{HOST}/api/mgr/loginReq',headers = header,data=payload)
print(response.json())