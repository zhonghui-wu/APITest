import rsa

str = '111111'
#公钥和私钥
(publicKey,privateKey) = rsa.newkeys(2048)#实例化加密对象

#加密
pwd1 = rsa.encrypt(str.encode('utf-8'),publicKey)
print('加密后结果1为：',pwd1.hex())

pwd2 = rsa.encrypt(str.encode('utf-8'),publicKey)
print('加密后的结果2为：',pwd2.hex())

#解密
depwd1 = rsa.decrypt(pwd1,privateKey)
print('解密的结果1为：',depwd1.decode())

depwd2 = rsa.decrypt(pwd2,privateKey)
print('解密的结果2为:',depwd2.decode())
