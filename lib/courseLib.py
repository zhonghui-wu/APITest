import requests
from lib.host import HOST

def add(name,desc,display_idx):
    payload = {
        "action": "add_course",
        "data": f'''{{
            "name":"{name}",
            "desc":"{desc}",
            "display_idx":"{display_idx}"
    }}'''
    }
    header = {"Content-Type": "application/x-www-form-urlencoded"}

    response = requests.post(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
    try:
        return response.json()
    except:
        return {'retcode': 777, 'reason': '项目异常'}
# add('令晓','前端','66')
# add('鸿楷','前端','67')


def list(pagenum,pagesize):
    headers = {"Content-Type": "application/json"}
    payload = {"action": "list_course", "pagenum": pagenum, "pagesize": pagesize}
    response = requests.get(f'{HOST}/api/mgr/sq_mgr/', headers=headers, params=payload)
    try:
        return response.json()
    except:
        return {'retcode': 777, 'reason': '项目异常'}
# print(list(1,10))

def delete(id):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {"action": "delete_course", "id": id}
    response = requests.delete(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
    try:
        return response.json()
    except:
        return {'retcode': 777, 'reason': '项目异常'}
# delete(1902)


def alter(id,name,desc,display_idx):
    header = {'Content-Type': 'application/x-www-form-urlencoded'}
    payload = {
        "action": "modify_course",
        "id": id,
        "newdata": f'''{{
            "name":"{name}",
            "desc":"{desc}",
            "display_idx":"{display_idx}"
    }}'''
    }
    response = requests.put(f'{HOST}/api/mgr/sq_mgr/', headers=header, data=payload)
    try:
        return response.json()
    except:
        return {'retcode': 777, 'reason': '项目异常'}
# alter(1901,'小学化学','小学化学课程',4)