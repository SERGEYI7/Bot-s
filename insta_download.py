import requests
import re

print(requests.get('https://www.instagram.com/p/CQoB3Y4oVg_wdLg60l34_dA7WYIppmooHpzkEc0/').text.find('"'))

with open(file='jpg_test1.jpg', mode='wb') as write_file:
    url = r"https://scontent-arn2-1.cdninstagram.com/v/t51.2885-15/e35/23417293_124729088205514_5255754684160802816_n.jpg?tp=1\u0026_nc_ht=scontent-arn2-1.cdninstagram.com\u0026_nc_cat=110\u0026_nc_ohc=vva5qr8QmtgAX9oEDoq\u0026edm=AABBvjUBAAAA\u0026ccb=7-4\u0026oh=d0935f3f0e688edb11c61e71bb44e27b\u0026oe=60DEACBE\u0026_nc_sid=83d603".replace(r'\u0026', '&')
    source_file = requests.get(url=url)
    print(source_file)
    write_file.write(source_file.content)
