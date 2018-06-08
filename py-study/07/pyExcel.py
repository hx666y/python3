import xlrd
import xlwt
from xlrd import open_workbook  #导入xlrd模块中打开excel模块
from xlutils.copy import copy   #导入xlutils模块的复制excel模块

# # 打开Excel
# file = xlrd.open_workbook('test.xlsx')
# # 获取所以sheet页的名字
# print(file.sheet_names())
#
# #sheet1 = file.sheet_by_name('sheet1')      #根据sheet页的名字获取sheet页
# sheet = file.sheet_by_index(0)          #根据sheet页的索引获取sheet页
# # 打印行数和列数
# print(sheet.nrows)
# print(sheet.ncols)
#
# # 打印每行信息
# for rownum in range(sheet.nrows):
#     print(sheet.row_values(rownum))
#
# # A2 和 C2 的值
# cell_A2=sheet.cell(1,0).value
# cell_C2=sheet.cell(1,2).value
# print(cell_A2)
# print(cell_C2)

# # 新增Excel
# title = ['姓名','年龄','性别','分数']
# stus = [['mary',20,'女',89.9],['mary',20,'女',89.9],['mary',20,'女',89.9],['mary',20,'女',89.9]]
# #新建一个excel对象
# wbk = xlwt.Workbook()
# #添加一个sheet页
# sheet = wbk.add_sheet("stu")
# for i in range(len(title)):
#     sheet.write(0,i,title[i])
# for i in range(len(stus)):
#     if i !=0:
#         for j in range(4):
#             sheet.write(i,j,stus[i][j])
# wbk.save('szz.xls')

# 修改excel
rb = open_workbook('szz.xls')
rs = rb.sheet_by_index(0)
wb = copy(rb)
ws = wb.get_sheet(0)
ws.write(1,0,'Lily')
wb.save('szz_copy.xls')