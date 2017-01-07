#-*- coding:utf-8 -*-
import re
import urllib
import requests
import json
from bs4 import BeautifulSoup

payload = {'p':'分母'}
response = requests.get("https://tw.dictionary.yahoo.com", params=payload)
print response.url
result_1 = response.text.encode('utf8')
soup = BeautifulSoup(result_1, "html.parser")

def line():
    print "+ - - - - - - - - - - - - - - - - +"


BLOCK = {}
list_category = []
list_translate = []
list_en = []
list_ch = []


pick = soup.select('div div .explain ')
for each in pick:
    allCategory = each.select('.title')
    list_ul = each.select('ul')
    for eachCategory in allCategory:
        categoryName = eachCategory.string.encode('utf8')
        list_category.append(categoryName)
for i in range(0, len(list_ul)):
    BLOCK[list_category[i]] = list_ul[i]


for c in range(0, len(list_category)):

    line()
    li = []
    print list_category[c]

    pick = BLOCK[list_category[c]].select('li')
    for each in pick:
        li.append(each)

    for i in range(0, len(li)):
        print "\t", li[i].select('h4')[0].string.encode('utf8')

        en = li[i].select('.example')
        ch = li[i].select('.example_translation')
        for j in range(0, len(ch)):
            original = en[j].text.encode("utf8")
            pattern = "([\w, ]+[\.\?])"
            renew = re.findall(pattern,original)
            print "\t\t", renew[0]
            print "\t\t", ch[j].string.encode('utf8')