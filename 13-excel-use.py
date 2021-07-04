import xlrd

# workbook = xlrd.open_workbook("学生表.xls")
#
# # 获取所有sheet名字
# print(workbook.sheet_names())
#
# # 根据索引获取指定的sheet对象
# sheet1 = workbook.sheet_by_index(0)
# print(sheet1.name)
#
# # 根据名字获取指定的sheel对象
# sheet2 = workbook.sheet_by_name('1班')
# print(sheet2.name)
#
# # 获取所有的sheet对象
# sheet_list = workbook.sheets()
# for i in sheet_list:
#     print(i.name)
#
# # 获取指定sheet的行数和列数
# sheet3 = workbook.sheet_by_index(0)
# print("行数：{}  列数：{}".format(sheet3.nrows, sheet3.ncols))

# workbook = xlrd.open_workbook("学生表.xls")
# sheet = workbook.sheet_by_index(0)
#
# # 获取指定行和列的cell对象
# cell1 = sheet.cell(0, 0)
# print(cell1.value)
#
# # 获取指定行的某几列对象
# cell2_list = sheet.row_slice(1, 0, 3)
# for i in cell2_list:
#     print(i.value)
#
# # 获取指定列的某几行对象
# cell3_list = sheet.col_slice(0, 0, 6)
# for i in cell3_list:
#     print(i.value)
#
# # 获取指定行列的值
# cell4 = sheet.cell_value(1, 0)
# print(cell4)
#
# # 获取指定行某几列的值
# cell5 = sheet.row_values(0, 0, 3)
# for i in cell5:
#     print(i)
#
# # 获取指定列某几行的值
# cell6 = sheet.col_values(0, 0, 6)
# for i in cell6:
#     print(i)

# print(xlrd.XL_CELL_EMPTY)

import xlwt

workbook = xlwt.Workbook()
sheet = workbook.add_sheet('sheet1')

# 写入表头数据
headers = ['姓名', '年龄']
for index, header in enumerate(headers):
    sheet.write(0, index, header)

# 写入第一列
names = ['张三', '王五']
for index, name in enumerate(names):
    sheet.write(index+1, 0, name)

# 写入年龄
sheet.write(1, 1, 10)
sheet.write(2, 1, 15)

# 保存
workbook.save("excel-write.xls")
