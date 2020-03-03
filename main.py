#!/usr/bin/python
import urllib
from urllib.request import Request
import json

UCMDB_ENDPOINT = "https://cmdb-hostname:port/api"
headers = {
    "Content-Type": "application/json"
}
auth_params = {
    'username': '',
    'password': '',
    'clientContext': 1
}

auth_call = Request(UCMDB_ENDPOINT, json.dumps(auth_params).encode('ascii'), headers, method='POST')
json_auth_output = json.load(auth_call)
print(json_auth_output)