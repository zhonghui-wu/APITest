import unittest
from lib.courseLib import add, list
from lib.deleteAllCourse import deleteCourse

class DemoUnittest2(unittest.TestCase):#继承unittest的方法
    # @classmethod
    # def setUpClass(cls):
    #     print('类级别的setup调用了，初始化了')#只会开始的时候运行
    # @classmethod
    # def tearDownClass(cls):
    #     print('类级别的teardown调用了，环境清除了')#只会结束的时候运行

    @classmethod
    def setUpClass(cls):
        pass
        # print('setup调用了，初始化了')#每个用例开始的时候都会运行
    @classmethod
    def tearDownClass(cls):
        deleteCourse()
        # print('teardown调用了，环境清除了')#每个用例结束的时候运行

    def test021(self):
        # self.assertEqual('1','1','测试通过')#assertEqual是断言，是等于的意思
        print('21')

    @unittest.skip('输入跳过该条测试用例的原因')  # unittest.skip跳过测试用例的方法
    def test023(self):
        print('23')

    def test022(self):
        oldList = list(1, 100)
        add('大学英语', '大学英语课程', '4')
        newList = list(1, 100)
        self.assertEqual(len(oldList['retlist']) + 1,len(newList['retlist']),'新增失败')
        print('22新增成功')

        # if len(oldList['retlist']) + 1 == len(newList['retlist']):
        #     print('没有刚刚新增的课程')
        # else:
        #     print('刚刚有新增成功课程')
