import unittest
import requests,json,time,xlrd
from lib.readExcels import redExcel,getNewExcel
from lib.deleteAllCourse import deleteCourse

class DemoUnittest(unittest.TestCase):#继承unittest的方法
    # @classmethod
    # def setUpClass(cls):
    #     print('类级别的setup调用了，初始化了')#只会开始的时候运行
    # @classmethod
    # def tearDownClass(cls):
    #     print('类级别的teardown调用了，环境清除了')#只会结束的时候运行


    def setUp(self):
        print('setup调用了，初始化了')#每个用例开始的时候都会运行

    def tearDown(self):
        print('teardown调用了，环境清除了')#每个用例结束的时候运行

    def test001(self):
        self.assertEqual('1','1','测试通过')#assertEqual是断言，是等于的意思
        print('1')


    def test003(self):
        # path = r'/Users/wuzhonghui/PycharmProjects/APIStudyTest/data/教管系统-测试用例V1.2.xls'
        # list = redExcel(path, 2)  # 打印Excel中的第二个工作簿中的测试用例
        # for i in range(0, len(list)):
        #     row = list[i]
        #     headers = json.loads(row[11])
        #     payloads = json.loads(row[5])
        #     testcodes = json.loads(row[6])
        #     ret = None
        #     if row[10] == 'post':
        #         newName = str(int(time.time() * 100))
        #         data = row[5].replace('{{courseName}}', newName)
        #         payloads = {
        #             "action": "add_course",
        #             "data": data
        #         }
        #         ret = requests.post(row[9], headers=headers, data=payloads)
        #     elif row[10] == 'delete':
        #         ret = requests.delete(row[9], headers=headers, data=payloads)
        #     elif row[10] == 'get':
        #         ret = requests.get(row[9], headers=headers, params=payloads)
        #     # 写回到Excel
        #     dict = ret.json()
        #     # if dict['retcode'] == testcodes['code']:
        #     #     print(row[0] + '测试通过')
        #     # else:
        #     #     print(row[0] + '测试不通过')
        #     self.assertEqual(dict['retcode'],testcodes['code'],'测试不通过')
        print('3')



    @unittest.skip('输入跳过该条测试用例的原因')#unittest.skip跳过测试用例的方法
    def test002(self):
        print('2')

    def test004(self):
        print('2')