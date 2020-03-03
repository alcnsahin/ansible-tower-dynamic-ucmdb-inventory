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
auth_call = requests.post(UCMDB_ENDPOINT + "/authenticate", json=auth_params, headers=headers, verify=False)
print(auth_call.status_code)
print("---------------------------------")
print(auth_call.json()["token"])
print("---------------------------------")
# execute tql query
execute_tql_headers = {
    "Authorization": "Bearer " + auth_call.json()["token"],
    "Content-Type": "application/json"
}
execute_tql_params = {
    "tqlName": "Redhat_Computers"
}
execute_tql = requests.post(UCMDB_ENDPOINT + "/topology", json=execute_tql_params, headers=execute_tql_headers,
                            verify=False)
print(execute_tql.json())
