from datetime import datetime
import time
import urllib
import werobot
from werobot import WeRoBot

robot = WeRoBot()
robot.config["APP_ID"] = "wxd69a49663e84d9dd"
robot.config["APP_SECRET"] = "701a42860f22ca4cb47549a702d1c727"
client = robot.client
token = client.grant_token()
print(token)

with open('/python_project/wechat_project/html/test1.html', 'r', encoding='utf-8') as f:
 	Soup = f.read()
content = Soup
#def upload_media_news(string_date,title,content):
articles = [{
    "title": "Live  Covid: Omicron ‘impact on society’",
    "thumb_media_id": 'V0DJbNT6Xc0LU91bSEBz9mqwTDAWrERl7jT-0N5WyqY',
    "author": "Louise小狗子",
    "digest": '',
    "show_cover_pic": 1,
    "content": content,
    "content_source_url": "https://www.theguardian.com/world/live/2021/dec/24/covid-news-live-new-york-scales-back-new-years-eve-celebrations-astrazeneca-booster-protects-against-omicron-study-finds"
    }
    ]

news_json = client.add_news(articles)
print(news_json)
media_id = news_json['media_id']
print('media_id',media_id)
#return news_json
"""
def run(string_date):
    title = 'Lovlov小狗子'
    content ='<p>Lovlov小狗子Lovlov小狗子Lovlov小狗子Lovlov小狗子哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈哈</p>'
    news_json = upload_media_news(string_date,title,content) 
    print('successful')

if __name__ == "__main__":
    start_time = time.time() 
    today = datetime.today()
    string_date = today.strftime('%Y%m%d')
    run(string_date)
    end_time = time.time() 
    print("程序耗时%f秒：" % (end_time - start_time))
"""