import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
url = "https://www.empireonline.com/movies/features/best-movies-2/"
# r = requests.get(url=url)
# r= r.text

with open("web","r") as f:
    content = f.read()

# Write your code below this line 👇
soup = BeautifulSoup(content,"html.parser")
l = soup.find_all(class_="listicle-item")
names = []
for item in l:
    try:
        t = item.find(class_="listicle-item-content").find_all("p")[1].find("a").string.split()[4:]
    except IndexError:
        t = item.find(class_="listicle-item-content").find("p").find_all("a")[2].string.split()[4:]
    names.append(' '.join(t))

with open("Top_100_movies.txt","a") as f:
    for i in range(len(names)):
        f.write(f"{i+1}: {names[i]}\n")