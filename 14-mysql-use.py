import pymysql

# 使用pymysql.connect方法连接数据库
db = pymysql.connect(host='localhost', port=3306, user='root', password='byack89HKC', database='crawler')
# 如果要操作具体的数据库，还需要获取db上的cursor对象
cursor = db.cursor()
# 使用cursor来执行sql语句
# cursor.execute('select * from temp')
# result = cursor.fetchone()
# print(result)

# # 插入一条数据的sql语句
# sql = "insert into temp(id,title,context) VALUES (null,'one','第一次插入')"
# # 执行sql语句
# cursor.execute(sql)
# 第二种数据变换的插入方法
# sql = "insert into temp(id,title,context) VALUES (null,%s,%s)"
# cursor.execute(sql, ('567', '一个不合格的刺客'))
# # 提交我们的操作
# db.commit()

# 查询语句
# sql = "select id, title from temp where id>3"
# cursor.execute(sql)
# 每次获取一条数据
# result1 = cursor.fetchone()
# result2 = cursor.fetchone()
# print(result1, result2)
# 接收全部的返回结果
# result = cursor.fetchall()
# print(result)
# 可以获取指定条数的数据，如果指定的大小超过结果的数量，也会返回所有的结果
# result = cursor.fetchmany(3)
# print(result)

# 删除语句
# sql = "delete from temp where title='xxx'"
# cursor.execute(sql)
# db.commit()

# 更新语句
sql = "update temp set title='更新后的title' where id=1"
cursor.execute(sql)
db.commit()

# 关闭数据库
db.close()
