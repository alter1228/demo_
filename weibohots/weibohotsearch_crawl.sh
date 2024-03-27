#!/bin/bash
# 使用了scrapy 和 jieba 库 进行数据的采集和整理
# 定时采集微博热搜数据进行词云分析的数据
# 此脚本用来使用crontab命令进行定时运行
# crontab 
# 30 * * * * ~/weibohots/weibohotsearch_crawl.sh



# 爬虫采集数据到数据库
cd ~/weibohots/weibohots/spiders
python -m scrapy crawl weibohotsearch

echo "`date` spider run ok !" >> ~/weibohots/wordcloud/weibo_wordcloud.log
sleep 10
# 数据库存储过程整合数据
mariadb -ualter -p1228 -e 'call weibohs.pro_splice();'
echo "`date` procedure_splice run ok !" >> ~/weibohots/wordcloud/weibo_wordcloud.log

sleep 10 
# 热搜拆解
cd ~/weibohots/wordcloud
python weibo_wordcloud.py >> weibo_wordcloud.log
echo "`date` python_jieba_lcut run ok !" >> weibo_wordcloud.log

