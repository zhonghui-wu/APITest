import unittest
from other.demo_unittest import DemoUnittest
from other.demo_unittest2 import DemoUnittest2
from ClassicHTMLTestRunner import HTMLTestRunner

#构建测试套件test_suite

#方法1
# suite = unittest.TestSuite()
# suite.addTest(DemoUnittest('test001'))#添加每一个测试用例
# suite.addTest(DemoUnittest('test002'))
# suite.addTest(DemoUnittest('test003'))
# suite.addTest(DemoUnittest2('test021'))
# suite.addTest(DemoUnittest2('test023'))

#方法二
# list = {
#     DemoUnittest('test001'),
#     DemoUnittest('test002'),
#     DemoUnittest('test003'),
#     DemoUnittest2('test021'),
#     DemoUnittest2('test022'),
#     DemoUnittest2('test023')
# }
# suite = unittest.TestSuite()
# suite.addTests(list)

#方法三

suite = unittest.defaultTestLoader.discover('other',pattern='demo_unittest*.py')#文件夹中的测试用例的py文件名，*是匹配所有


#测试运行器
#自带的
# runner = unittest.TextTestRunner()
# runner.run(suite)

#使用插件HTMLTestRunner，可生成html报告
path = r'/Users/wuzhonghui/PycharmProjects/APIStudyTest/report/htmlReport.html'
report = open(path,'wb')
runner = HTMLTestRunner(stream=report,verbosity=2,description='用例执行结果详情',title='xx项目测试报告',tester='此处填写作者')
runner.run(suite)