import hashlib,requests

str = 'zr111111hg'
md5 = hashlib.md5()
md5.update(str.encode('utf-8'))
pwd = md5.hexdigest()#md5加密
print(pwd)

payload = {"mobile":"13588000000","password":pwd}

response = requests.post("http://121.41.14.39:2001/token/token",data=payload)
response = response.json()
print(response)
print(response["data"])#提取返回的token