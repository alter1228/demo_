import scrapy
import json
from weibohots.items import WeibohotsItem

class WeibohotsearchSpider(scrapy.Spider):
    name = "weibohotsearch"
    allowed_domains = ["www.weibo.com"]
    start_urls = ["https://weibo.com/ajax/side/hotSearch"]

    def parse(self, response):
        # 处理json文件
        zy_index = response.text.index('"hotgov":')
        if zy_index < 30:
            data = response.text.replace('{"ok":1,"data":{','[').replace('"hotgov":','').replace('"realtime":[','')[ : -2]
        else:
            data = response.text.replace('{"ok":1,"data":{"realtime":','').replace('],"hotgov":',',')[ : -2]+"]"

        obj = json.loads(data)

        for value in obj:
            category = subject_label = word = 'None'
            category = value.get("category")
            subject_label = value.get("subject_label")
            word = value.get("word")
            if category is None:
                category='None'
            if subject_label is None:
                subject_label='None'
            msg = WeibohotsItem(category=category,subject_label=subject_label,word=word)
            yield msg
