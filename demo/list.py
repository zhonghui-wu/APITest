import requests
from lib.host import HOST

headers = {"Content-Type" : "application/json"}
payload = {"action":"list_course","pagenum":"1","pagesize":"20"}
response = requests.get(f'{HOST}/api/mgr/sq_mgr/',headers=headers,params=payload)
# response.encoding = 'utf-8'

print(response.json())