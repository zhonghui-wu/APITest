import requests,json,time,xlrd
from lib.readExcels import redExcel,getNewExcel
from lib.deleteAllCourse import deleteCourse

def fiveHomework():
    path = r'/Users/wuzhonghui/PycharmProjects/APIStudyTest/data/教管系统-测试用例V1.2.xls'
    newPath = r'/Users/wuzhonghui/PycharmProjects/APIStudyTest/report/教管系统-测试结果2.xls'
    list = redExcel(path,2)#打印Excel中的第二个工作簿中的测试用例
    wookBookNew = getNewExcel(path)#复制测试用例
    wookSheetNew = wookBookNew.get_sheet(2)#复制工作簿

    for i in range(0,len(list)):
        row = list[i]
        headers = json.loads(row[11])
        payloads = json.loads(row[5])
        testcodes = json.loads(row[6])
        ret = None
        if row[10] == 'post':
            newName = str(int(time.time()*10000))
            data = row[5].replace('{{courseName}}',newName)
            payloads = {
                "action": "add_course",
                "data": data
            }
            ret = requests.post(row[9],headers = headers,data=payloads)
        elif row[10] == 'delete':
            ret = requests.delete(row[9],headers = headers,data = payloads)
        elif row[10] == 'get':
            ret = requests.get(row[9],headers=headers,params=payloads)

        try:
            #写回到Excel
            dict = ret.json()
            if dict['retcode'] == testcodes['code']:
                wookSheetNew.write(i+1,7,"pass")
            else:
                wookSheetNew.write(i+1,7,'fail')
                if 'reason' in dict.keys():
                    wookSheetNew.write(i+1,8,dict['reason'])
        except:
            wookSheetNew.write(i+1,7,'fail')
            wookSheetNew.write(i+1,8,'异常')

    wookBookNew.save(newPath)

fiveHomework()

deleteCourse()

