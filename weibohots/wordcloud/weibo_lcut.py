import pymysql
import jieba
# 数据库信息
host = '192.168.0.156'
user = 'alter'
password = '1228'
port = 3306
mysql = pymysql.connect ( host = host , user = user ,password = password , port = port )

# 查询

cursor = mysql.cursor()

# sql
sql = 'select * from weibohs.eachwordsplice'

# 执行sql
cursor.execute(sql)

# 结果
result = cursor.fetchall()
# print(result)
for tup in result:
    print(tup[0],jieba.lcut(tup[2],cut_all=True))
# 关闭查询
cursor.close()
mysql.close()
