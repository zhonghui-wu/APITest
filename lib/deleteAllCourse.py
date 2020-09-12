from lib.courseLib import delete,list

def deleteCourse():
    retLists = list(1,100)
    num = 0
    for msg in retLists['retlist']:
        delete(msg['id'])
        num = num + 1
    print('本次共删除了',num,'条数据')
    return
deleteCourse()