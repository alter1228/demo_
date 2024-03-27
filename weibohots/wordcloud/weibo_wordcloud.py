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
sql = 'select e.id,e.create_time,e.splice_result from weibohs.eachwordsplice e where not exists (select create_time from weibohs.word w where w.create_time = e.create_time )'

# 执行sql
cursor.execute(sql)

# 结果
result = cursor.fetchall()
# print(result)

# 拆解每条记录并摘取前十条高频词汇
wcount = {}
strs = ''
for var in result:
    words = jieba.lcut(var[2],cut_all=True)
    # print(var[0])
    for word in words:
        if len(word) < 2:
            continue
        else:
            wcount[word] = wcount.get(word,0) + 1
    item = list(wcount.items())
    item.sort(key=lambda x:x[1],reverse=True)
    for i in range(10):
        word,cou = item[i]
        strs += "("+'"'+var[1]+'"'+','+'"'+word+'"'+','+str(cou)+'),'
        # print("{0}{1}{2}".format(i+1,word,cou))
    # print (strs[:-1]+';')
    # sql
    sql = 'insert into weibohs.word(create_time,word,wordcount) values '+ strs[:-1]+';'
    # 执行sql
    print(str(var[0])+' '+var[1]+ "insert···\t",end="")
    cursor.execute(sql)
    print(str(var[0])+" insert.OK")
    # 初始化键值对 strs
    strs = ''
    wcount = {}

# 关闭操作和会话
cursor.close()
mysql.commit()
mysql.close()


