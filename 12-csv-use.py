import csv


# # 按行读取csv文件，每一行返回一个列表
# with open('快代理-ip.csv', 'r', encoding='utf-8') as f:
#     result = csv.reader(f)
#     for i in result:
#         print(i)
#
# # 按字典的形式读取，这种方法有索引，可以通过索引获取值
# with open('快代理-ip.csv', 'r', encoding='utf-8') as f:
#     res = csv.DictReader(f)
#     for i in res:
#         print(i['IP'])

headers = ['name', 'age']
stu_list = [
    ['wanger', 10],
    ['lisi', 15],
    ['lixiang', 20]
]
stu_dict = [
    {'name': 'wanger', 'age': 10},
    {'name': 'lisi', 'age': 15},
    {'name': 'lixiang', 'age': 20},
]

# writer就是一行一行的写入，指定newline=''去掉多余的换行
with open('students.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(headers)  # 先写入表头数据
    writer.writerows(stu_list)  # 学生信息多行写入

# DictWriter按字典形式写入
with open('students.csv', 'w', encoding='utf-8', newline='') as f:
    # 除了传入要写入的文件，还有表头信息
    writer = csv.DictWriter(f, headers)
    # 但以上表头数据仍未写入，需要调用以下方法才能正式写入表头数据
    writer.writeheader()
    writer.writerows(stu_dict)
