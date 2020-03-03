#!/usr/bin/python
import urllib
from urllib.request import urlopen
import json

UCMDB_ENDPOINT = "https://cmdb-hostname:port/rest-api"
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

# authentication
auth_call = urlopen(UCMDB_ENDPOINT + "/authenticate", json.dumps(auth_params).encode('ascii'), headers, method='POST')
json_auth_output = json.load(auth_call.read())
print(json_auth_output)

# execute tql query
