import random

print(int(random.random()*100000000))#这个是取随机数
print(random.randint(100000,100000000000))#这个是直接取数值之间的随机数，这个直接出来的就是正整数

import time
print(int(time.time()*10000))#这个是时间戳取值


time1 = str(int(time.time()*100))

course = '大学英语{{name}}'

print(course.replace('{{name}}',time1))