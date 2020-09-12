from lib.readExcels import redExcel,getNewExcel
from lib.sendCourseLib import sendCourse
import json
from lib.deleteAllCourse import deleteCourse

path = r'/Users/wuzhonghui/PycharmProjects/APIStudyTest/data/教管系统-测试用例V1.2.xls'
newPath = r'/Users/wuzhonghui/PycharmProjects/APIStudyTest/report/教管系统-测试结果.xls'

# print(redExcel(path,0))
workBookNew = getNewExcel(path)
workSheetNew = workBookNew.get_sheet(0)

#读取工作表中的测试用例
retList = redExcel(path,0)
for i in range(0,len(retList)):
    row = retList[i]#这里是每一条测试用例
    ret = sendCourse(row)#这里是将每条用例传入sendCourse函数中并返回结果
    column7 = json.loads(row[6])#读取第7列的值
    if ret['retcode'] == column7['code']:
        print(row[0] + '测试通过')
        workSheetNew.write(i+1,7,'测试通过')#write（行，列，写入数据）
    else:
        print(row[0] + '测试不通过')
        workSheetNew.write(i+1,7,'测试不通过')
        if 'reason' in ret.keys():
            workSheetNew.write(i+1,8,ret['reason'])


workBookNew.save(newPath)
deleteCourse()