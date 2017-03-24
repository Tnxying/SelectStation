# -*- coding:utf-8 -*-
import time
import urllib
from urllib import request
from urllib import parse
import json
from pprint import pprint
import csv

def getUrlData(url, data=None, header=None):
    if data is not None and header is not None:
        try:
            print(data);
            print(header);
            full_url = request.Request(url,data,headers)
            response = request.urlopen(full_url)
            html = response.read().decode()
            print(html)
            return html
        except Exception as e:
            print("Exception:", e)
    else:
        try:
            response = request.urlopen(url)
            print(type(response))
            response = response.read()
            print(type(response))
            html = bytes.decode(response)
            print(type(html))
            f = open('test.html', 'w', -1, 'utf-8')
            f.write(html)
            return html
        except (Exception, request.URLError) as e:
            print(e)

if __name__ == "__main__":

    time_t = int(time.time())
    url = "http://221.226.28.67:88/jsswxxSSI/water_selectWaterAndStStbprpBAndWaterWarJson.action"
    values = {'ajaxVal':2,
             'endTime':'2017-03-24 10:59:31',
             'id':0,
             'isTopic':'null',
             'startTime':'2017-03-22 08:00:00',
             'tId':'null',
             'timestamp':time_t,
             'type':0,
             'waterType':'1-2-3-4-5'}
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:52.0) Gecko/20100101 Firefox/52.0'
    headers = {'User-Agent' : user_agent}
    data = urllib.parse.urlencode(values).encode()
    html = getUrlData(url, data, headers)
    jsonData = json.loads(html)
    print(jsonData)
    content = jsonData['DATA']
    keys = content[0].keys()
    keylist = list(keys)
    subkeys = ['SITENAME','X', 'Y']
    f = open("site.csv", 'w')
    f.write("%s,%s,%s\n" %(subkeys[0], subkeys[1], subkeys[2]))
    for row in content:
       f.write("%s,%s,%s\n" %(row[subkeys[0]], row[subkeys[1]], row[subkeys[2]]))

    print(keys)
    # pprint(content)
    # for unit in content:
    #     print(unit)