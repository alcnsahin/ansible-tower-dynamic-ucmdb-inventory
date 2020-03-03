#!/usr/bin/python
import urllib
from urllib.request import Request
import json

UCMDB_ENDPOINT = "https://cmdb-hostname:port/api"
UCMDB_USERNAME = 'username'
UCMDB_PASSWORD = 'password'
UCMDB_CLIENT_CONTEXT = 1
headers = {
    "Content-Type": "application/json"
}
auth_params = {
    'username': UCMDB_USERNAME,
    'password': UCMDB_PASSWORD,
    'clientContext': UCMDB_CLIENT_CONTEXT
}

auth_call = Request(UCMDB_ENDPOINT, json.dumps(auth_params).encode('ascii'), headers, method='POST')
json_auth_output = json.load(auth_call)
print(json_auth_output)
