# -*- coding:utf-8 -*-
from urllib import request

# url = 'http://221.226.28.67:88/jsswxxSSI/water_selectWaterAndStStbprpBAndWaterWarJson.action'
url = "http://www.baidu.com"
try:
    response = request.urlopen(url)
    html = bytes.decode(response.read())
    print(response)
    print(html)
    f=open('test.html', 'w', -1,'utf-8')
    f.write(html)
except (Exception, request.URLError) as e:
    print(e)