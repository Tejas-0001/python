from bs4 import BeautifulSoup

with open("website.html") as f:
    content = f.read()

soup = BeautifulSoup(content,"html.parser")
# print(soup.prettify())      indent the html
# print(soup.title)  print complete title tag line
# print(soup.title.name)    print tag name    title
# print(soup.title.string)      print what's inside the tag title
# print(soup.a)     print first a tag in html

"""all tags"""
all_anchor_tags = soup.find_all(name="a")
# print(all_anchor_tags)      #this gives list of all anchor tags

for tag in all_anchor_tags:
    # print(tag.getText())        #this gives all the text
    # print(tag.get("href"))          #this gives all link
    """all attribute can be selected like this"""

"""if you want to find something by attribute"""
heading = soup.find(name="h1",id="name")
# print(heading)

"""since class is keyword we have to write class_  with underscore at end"""
section = soup.find(name="h3",class_="heading")   # finding 1 element
# print(section.get("class"))     #used to find value of attribute
# print(section)

"""we can use selector like css"""
url = soup.select_one(selector="p a")       #this find the first a tag which was in the p tag
url_all = soup.select(selector="p a")       #this will findall a which are under p
# print(url)                                  #selector attribute work just like css
name = soup.select_one(selector="#name")    #select only 1
headings = soup.select(selector=".heading") #select all

import requests

r = requests.get(url="https://news.ycombinator.com/")
data = r.text
data = BeautifulSoup(data,"html.parser")
links = data.find_all(class_="titleline")
title = []
for item in links:
    t = item.find("a")
    title.append((t.string,t.get("href")))

score = []
scores = data.find_all(class_="score")
for i in scores:
    score.append(int(i.string.split()[0]))

m = max(score)
for i in range(len(score)):
    if score[i] == m:
        print(title[i],score[i])
