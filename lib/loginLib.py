import requests
from lib.host import HOST
def login(username,password):
    header = {"Content-Type":"application/x-www-form-urlencoded"}
    payload = {"username":username,"password":password}
    response =requests.post(f'{HOST}/api/mgr/loginReq',headers = header,data=payload)
    try:
        return response.cookies['sessionid']
    except:
        return {'retcode': 777, 'reason': '项目异常'}


# print(login('auto','sdfsdfsdf'))

# def list(pagenum,pagesize,c):
#     headers = {"Content-Type": "application/json"}
#     payload = {"action": "list_course", "pagenum": pagenum, "pagesize": pagesize}
#     cookie = {"sessionid":c}
#     response = requests.get(f'{HOST}/api/mgr/sq_mgr/', headers=headers, params=payload,cookies=cookie)
#     try:
#         return response.json()
#     except:
#         return {'retcode': 777, 'reason': '项目异常'}
# coo = login("auto", "sdfsdfsdf")
# # print(coo)
# print(list(1,10,coo))