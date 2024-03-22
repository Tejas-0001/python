import requests
import base64
from bs4 import BeautifulSoup
import json

client_id = "15d59d547b9442939cfac65b5b32aeeb"
client_secret = "461d70e455714e59a848fbc8351d79f7"
user_id = "31wf3p6jycgozuq7v3n6jcpr37k4"

"""get authorization for oauth_v.2.0 spotify to get user to have permission to access user account"""
def get_auth():
    global client_id
    p = {
        "response_type": "code",
        "client_id":client_id,
        "scope": "playlist-modify-private",
        "redirect_uri":"http://localhost:8888/callback"
    }
    response = requests.get(url="https://accounts.spotify.com/authorize",params=p)
    if response.history:
        print("Request was redirected")     # we are doing this because we have to go to the redirected website and agree to terms
        for resp in response.history:
            print(resp.status_code, resp.url)
        print("Final destination:")         # from here we will get the code in the url
        print(response.status_code, response.url)
    else:
        print("Request was not redirected")

#get_auth()
""" used when starting new app"""
# this was extracted from previous step

code="AQB6smKEVIF5v35IEfIY6akI30PQ_ojHkwdWQBFCqZEs4XX5oSgyGcV-f7oEiWIhUSduPEKtUqwbt3BItE_-5KVHITFQvncucgzQzeoerwzhHj8qbfuMurYLEOX9_T_DzR3KACThr2Y4ytveuiLRhDHcMoguHrQZ4gbMDBpaD47j7mPQQGVzzhuSg9RKloV5LSa9uxos-3OFfHc"


def get_access_token():
    global client_id,client_secret,code
    encodedData = base64.b64encode(bytes(f"{client_id}:{client_secret}", "ISO-8859-1")).decode("ascii")
    h = {
        "Authorization": f"Basic {encodedData}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    d = {
        "grant_type":"authorization_code",
        "code":code,
        "redirect_uri":"http://localhost:8888/callback"
    }
    """use this to get new access token since it's only available for 1 hour"""
    r = requests.post(url="https://accounts.spotify.com/api/token",headers=h,params=d)
    print(r.json())
    with open("access_token.json","w") as f:
        f.write(r.json())
# get_access_token()

"""above thing is only done for first time after that refresh token is used"""


refresh_tok = 'AQD4JwbybmNeVSAgdJ_DIlYOzbKPoPHS2ALH9PoA7aTCyt2QROWL19ygeCOiALqvL2pa_nJ1EEfQB6VeAIvRDKKlAB163fjOT4wofUmBUF6PmFiPBPDjDXnP16UyreXal98'
def refresh_token():
    global refresh_tok
    global client_id, client_secret, code
    encodedData = base64.b64encode(bytes(f"{client_id}:{client_secret}", "ISO-8859-1")).decode("ascii")
    h = {
        "Authorization": f"Basic {encodedData}",
        "Content-Type": "application/x-www-form-urlencoded"
    }

    d = {
        "grant_type":"refresh_token",
        "refresh_token": refresh_tok
    }

    r = requests.post(url="https://accounts.spotify.com/api/token",headers=h,params=d)
    print(r.json())
    with open("access_token.json","w") as f:
        t = json.dumps(r.json(),indent=4)
        f.write(t)
# refresh_token()

"""below is access token"""
token = "BQC-XOFXormEEPdwr0wJDluQN_6jcAsmk6M_XfD7edEsr4HoHenJoEb13O4DK7ngxj7yjfT3Tu9nX7Umw6nKsg9-TW2-OxXUM9XQh00gn159P0580web5Q7GYktyxdnIgW8blZHYPWq9ahjdXhXP5HfQmgA-vWR7VdZf1IFfnvSFhcC-Xo4mE1qpE_bhiQ39Pnqds61CAJP6S3Z-vWcBttPBLwcJg4AC4d05jA"
def create_new_playlist(name,desc):
    global token,user_id
    h = {
        'Authorization': f'Bearer  {token}',
        'Content-Type': 'application/json'
    }

    p = {
        "name": name,
        "description": desc,
        "public": False
    }

    r = requests.post(url=f"https://api.spotify.com/v1/users/{user_id}/playlists",headers=h,json=p)
    with open("playlist","w") as f:
        f.write(r.json())


# create_new_playlist("learning","wowoowowow")

year = input("enter which date top 100 billboard songs you wanna listen in format YYYY-MM-DD\n")
r = requests.get(url=f"https://www.billboard.com/charts/hot-100/{year}/")
content = r.text
# with open("songs.html","r") as f:
#     content = f.read()
soup = BeautifulSoup(content, "html.parser")
titles = soup.find_all(class_="o-chart-results-list__item")
songs = []
for item in titles:
    t = item.find(class_="c-title")
    if t is not None:
        temp = t.string.split()
        songs.append(' '.join(temp))
print(songs)
playlist_id = "4r3YQ5qthehivTZ6SGYmk2"          # this is seen in response when playlist was created

spotify_uri = []


def search(song):
    global token
    p = {
        "q": song,
        "type": "track",
        "limit": 1
    }
    h = {
        'Authorization': f'Bearer  {token}'
    }

    r = requests.get(url="https://api.spotify.com/v1/search",headers=h, params=p)
    print(r.json())
    try:
        z = r.json()["tracks"]["items"][0]["href"].split("/")[-1]
    except KeyError:
        return
    spotify_uri.append(f"spotify:track:{z}")


for item in songs[:10]:
    search(item)


def add_songs():
    print("adding")
    print(spotify_uri)
    global playlist_id
    p = {"uris": spotify_uri}
    h = {
        'Authorization': f'Bearer  {token}',
        'Content-Type': 'application/json'
    }
    r = requests.post(url=f"https://api.spotify.com/v1/playlists/{playlist_id}/tracks",headers=h, json=p)
    print(r.text)


add_songs()




