#!/usr/bin/python
import requests

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
auth_call = requests.post(UCMDB_ENDPOINT + "/authenticate", data=auth_params, headers=headers)
print(auth_call.status_code)
print("---------------------------------")
print(auth_call.json())
# execute tql query
