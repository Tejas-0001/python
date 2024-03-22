import requests
import base64

client_id = "8667aac8bcf74857a317cdc4d2a0cec1"
client_secret = "ef52f06cd49a4cb48c7819e952d08c86"
user_id = "31wf3p6jycgozuq7v3n6jcpr37k4"

"""get authorization for oauth_v.2.0 spotify to get user to have permission to access user account"""
def get_auth():
    p = {
        "response_type": "code",
        "client_id":"8667aac8bcf74857a317cdc4d2a0cec1",
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

get_auth()
""" used when starting new app"""
code="AQCQA-zswktvixKvxRYHAoyAjiQNeTWJpLkEn18nIJaMnejmaiGjW3FkBMbRQVLti1FyYFzyERmbmuF0xD4yUXnOt32Dq81iz4Yus2O2_39nG2ycBAT6Kz0SWgpAR7eqpf0vdaVOwuezlkFZ1WT1Ryu3Yvah9_hpM2VvVmpw7cUj4H6eyDEwqwYwlhQA3Gf7-juQK47P7aBqEXc"
# this was extracted from previous step