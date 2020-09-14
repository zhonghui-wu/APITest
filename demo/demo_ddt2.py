import unittest
from ddt import ddt,data,json
from lib.readExcels import redExcel
from lib.sendCourseLib import sendCourse
from lib.deleteAllCourse import deleteCourse

path = r'/Users/wuzhonghui/PycharmProjects/APIStudyTest/data/教管系统-测试用例V1.2.xls'
excelData = redExcel(path, 0)  # 打印Excel中的第二个工作簿中的测试用例

@ddt
class DemoDDT(unittest.TestCase):
    @classmethod
    def tearDownClass(cls):#类级别的环境清除，
        deleteCourse()

    @data(*excelData)#*是解包
    def test_001(self,row):
        # print(row)
        ret = sendCourse(row)  # 这里是将每条用例传入sendCourse函数中并返回结果
        column7 = json.loads(row[6])  # 读取第7列的值
        have_reason = ''
        if 'reason' in ret.keys():
            have_reason = ret['reason']
        self.assertEqual(ret['retcode'],column7['code'],have_reason)#断言
        print(row[0] + '测试成功')

    #     self.aaa('7','8')
    #
    #
    # def aaa(self,*args):#装包
    #     print(args)
