import requests
from lib.host import HOST

header = {'Content-Type':'application/x-www-form-urlencoded'}
payload = {
    "action":"modify_course",
    "id":"1903",
    "newdata":'''{
        "name":"cecshi",
        "desc":"ceshi",
        "display_idx":"2"
}'''
}
response = requests.put(f'{HOST}/api/mgr/sq_mgr/',headers=header,data=payload )
print(response.json())