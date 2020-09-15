import base64

str = '231313'

pwd = base64.b64encode(str.encode('UTF-8'))#base64编码

print(pwd)

bstr = base64.b64decode(pwd)#解码

print(bstr.decode('UTF-8'))