import requests
from bs4 import BeautifulSoup
year = input("enter which date top 100 billboard songs you wanna listen in format YYYY-MM-DD")
r =requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}/")
content = r.text
# with open("songs.html","r") as f:
#     content = f.read()
soup = BeautifulSoup(content,"html.parser")
titles = soup.find_all(class_="o-chart-results-list__item")
songs = []
for item in titles:
    t = item.find(class_="c-title")
    if t is not None:
        temp = t.string.split()
        songs.append(' '.join(temp))
print(songs)
playlist_id = "4r3YQ5qthehivTZ6SGYmk2"

spotify_uri = []

def search(song):
    global token
    p = {
        "q":song,
        "type":"track",
        "limit":1
    }
    h = {
        'Authorization': f'Bearer  {token}'
    }

    r = requests.get(url="https://api.spotify.com/v1/search",params=p)
    try:
        r = r.json()["tracks"]["items"][0]["href"].split()[-1]
    except KeyError:
        return
    spotify_uri.append(f"spotify:track:{r}")

for item in songs:
    search(item)

def add_songs():
    global playlist_id
    p = {"uris": spotify_uri}
    r = requests.post(url=f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks",params=p)

add_songs()