# 测试连接
import pymysql.cursors
'''
connection1 = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "Dchopj0896,/0110",
                             db = "guardian",
                             charset= "utf8mb4")

cur = connection1.cursor() # 生成游标对象
cur.execute("SELECT VERSION()")

# 使用 fetchone() 方法获取单条数据.
data = cur.fetchone()

print("Database version : %s " % data)


#创建数据库guardian

connection2 = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "Dchopj0896,/0110",
                             charset= "utf8mb4")
cursor = connection2.cursor() #创建游标
cursor.execute("create database guardian")
'''

#创建表结构
connection3 = pymysql.connect(host = "localhost",
                             port = 3306,
                             user = "root",
                             password = "Dchopj0896,/0110",
                             database= "guardian",
                             charset= "utf8mb4")
cursor3 = connection3.cursor()
cursor3.execute("create table t1("
                "ID int auto_increment primary key,"
                "Date datetime,"
                "Title varchar(255),"
                "URL varchar(255),"
                "Cover_picture varchar(255))")
cursor3.execute("create table t2(ID int auto_increment primary key,"
                "Author varchar(255),"
                "Paragraph text,"
                "illustration_picture varchar(255))")






