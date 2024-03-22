"""Basic auth with username and password"""


import requests
from requests.auth import HTTPBasicAuth
basic = HTTPBasicAuth('user', 'pass')
requests.get('https://httpbin.org/basic-auth/user/pass', auth=basic)


"""or"""

requests.get('https://httpbin.org/basic-auth/user/pass', auth=('user', 'pass'))


"""https://requests.readthedocs.io/en/latest/user/authentication/#basic-authentication"""


headersAPI = {
    'accept': 'application/json',
    'Authorization': 'Bearer '+'access_token',   #or
    "Authorization": "Basic your-encoded-base64['token']"





}


response = requests.get('https://somedomain.test.com/api/Users/Year/2020/Workers', headers=headersAPI, params=params, verify=True)
api_response = response.json()