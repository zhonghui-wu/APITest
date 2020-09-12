import requests,json
from lib.host import HOST

payload = {
    "action" : "add_course",
    "data" : '''{
        "name":"2",
        "desc":"2",
        "display_idx":"2"
}'''
}
header = {"Content-Type":"application/x-www-form-urlencoded"}

response = requests.post(f'{HOST}/api/mgr/sq_mgr/',headers=header,data=payload)

print(response.json())

# payload = {
#     "action" : "add_course_json",
#     "data" : {
#         "name":"2",
#         "desc":"2",
#         "display_idx":"2"
# }
# }
# header = {"Content-Type":"application/json"}
#
# response = requests.post(f'{HOST}/apijson/mgr/sq_mgr/',headers=header,data=json.dumps(payload))
#
# print(response)