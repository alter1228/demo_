# 临时查看数据采集情况
date
mariadb -uroot -p1228 -e 'select create_time from weibohs.hotsearch group by 1 order by 1 desc limit 10'

