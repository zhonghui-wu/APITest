import hashlib

str = '1111111'

md5 = hashlib.md5()#实例化一个md5对象

md5.update(str.encode('utf-8'))#加密

print(md5.hexdigest())#获取加密结果