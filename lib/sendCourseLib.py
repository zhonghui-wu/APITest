from lib.readExcels import redExcel
from lib.courseLib import add,list,delete
import json,time

#['10001', '增加课程', '所有字段正常填写', '正确，返回成功', 'add', '{\n  "name":"大学英语",\n  "desc":"大学英语课程",\n  "display_idx":"4"\n}\n', '{"code":0}', '', '']
#课程管理函数

def sendCourse(row):
    column5 = row[4]#这里是取第5列的值
    # print(column5)
    column6 = json.loads(row[5])#这里是取第6列的值,json.loads是str格式换成dict格式
    # print(column6)
    ret = None#先定义一个为空返回值
    if column5 == 'add':
        courseName = column6['name']  # 吧获取课程名称
        courseName = courseName.replace('{{courseName}}', str(int(time.time() * 100)))  # 把课程名称替换成时间戳，防止重名
        ret = add(courseName,column6['desc'],column6['display_idx'])
    elif column5 == 'delete':
        ret = delete(column6['id'])
    elif column5 == 'list':
        ret = list(column6['pagenum'],column6['pagesize'])

    return ret

# msg = redExcel('/Users/wuzhonghui/Downloads/教管系统-测试用例V1.2.xls',0)
# sendCourse(msg[0])