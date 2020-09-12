import requests
from lib.host import HOST

header = {'Content-Type':'application/x-www-form-urlencoded'}
payload = {"action":"delete_course","id":"1903"}
response = requests.delete(f'{HOST}/api/mgr/sq_mgr/',headers = header ,data = payload)
print(response.json())