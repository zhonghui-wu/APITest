from lib.courseLib import add,list


oldList = list(1,100)
ret = add('大学英语','大学英语课程','4')
newList = list(1,100)

if len(oldList['retlist']) == len(newList['retlist']):
    print('没有刚刚新增的课程')
else:
    print('刚刚有新增成功课程')