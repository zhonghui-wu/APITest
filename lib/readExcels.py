import xlrd

#设计一个读取Excel的函数
def redExcel(path,sheet_num):

#打开Excel，获取工作簿的对象
    workBook = xlrd.open_workbook(path)
    # print(workBook.nsheets)#查看Excel中有几个工作表

#从工作簿中获取工作表对象
    workSheet = workBook.sheet_by_index(sheet_num)
    # print(workSheet.nrows)#查看Excel中有几行

#循环读取Excel中的数据并放入列表中
    retList = []
    for num in range(1,workSheet.nrows):
        oneRow = workSheet.row_values(num)#返回list,得到的是第几行数据
        retList.append(oneRow)
# 返回数据列表
    return retList

# ShowRetlist = redExcel('/Users/wuzhonghui/Downloads/教管系统-测试用例V1.2.xls',0)
# print(ShowRetlist)

#设计工作簿复制函数

from xlutils.copy import copy

def getNewExcel(path):
    workBook = xlrd.open_workbook(path,formatting_info=True)#formatting_info=True是为了保证复制到原来到格式
    newWorkBook = copy(workBook)
    return newWorkBook



getNewExcel('/Users/wuzhonghui/PycharmProjects/APIStudyTest/data/教管系统-测试用例V1.2.xls')

