# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import time
# 加载 settings 文件
from scrapy.utils.project import get_project_settings
# 导入pymysql
import pymysql
class WeibohotsPipeline:
    def open_spider(self,spider):
        settings = get_project_settings()
        self.host = settings['DB_HOST']
        self.port = settings['DB_PORT']
        self.user = settings['DB_USER']
        self.password = settings['DB_PASSWORD']
        self.name = settings['DB_NAME']
        self.charset = settings['DB_CHARSET']
        self.connect()
    def connect(self):
        self.conn = pymysql.connect(
            host = self.host,
            port = self.port,
            user = self.user,
            password = self.password,
            db = self.name,
            charset = self.charset
        )

        self.cursor = self.conn.cursor()

    def process_item(self, item, spider):
        cur_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        sql = 'insert into hotsearch(category,subject_label,word,create_time) values("{}","{}","{}","{}")'.format(item['category'],item['subject_label'],item['word'],cur_time)
        self.cursor.execute(sql)
        self.conn.commit()
        return item
    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()
