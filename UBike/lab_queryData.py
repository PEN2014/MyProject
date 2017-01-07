#-*- coding:utf-8 -*-
import urllib
import requests
import json

"""
# new taipei
url = "http://data.ntpc.gov.tw/od/data/api/54DDDC93-589C-4858-9C95-18B2046CC1FC?$format=json"
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}
response = requests.get(url, headers=headers)
readable = response.text#.code('utf8')
jsonData = json.loads(readable)

print len(jsonData)
print jsonData[0].keys()
for each in iter(jsonData):
    print "{0}\t{1}, {2}\t{3}/{4}\t{5}".format(each['sno'], each['lat'], each['lng'], each['sbi'], each['bemp'], each['sna'].encode('utf8'))
"""
# http://tycg.youbike.com.tw/cht/f12.php