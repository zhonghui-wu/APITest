from lib.courseLib import add,list
import time

courseName = '大学物理'+str(int(time.time()*1000))
ret = add(courseName,'大学物理',0)
returnList = list(1,1000)
have = False
for msg in returnList['retlist']:
    # print(msg)
    if ret['id'] == msg['id']:
        print('新增课程测试成功')
        have = True
        break

if have == False:
    print('新增课程失败')
