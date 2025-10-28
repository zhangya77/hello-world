import mysql.connector

mydb = mysql.connector.connect(
    host="185.119.40.28",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd=",HCCws/2W0!PROD",  # 数据库密码
    port=63751
)

print(mydb)