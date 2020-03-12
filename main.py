#!/usr/bin/python

'''
Example Output:
inventories_json = {
    "_meta": {
        "hostvars": {
            "host001": {
                "var001": "value"
            }
        }
    }
}
'''

import requests
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


class UcmdbDynamicInventory(object):

    def authenticate(self):
        auth_call = requests.post(UCMDB_ENDPOINT + "/authenticate", json=auth_params, headers=headers, verify=False)
        # print(auth_call.status_code)
        self.token = auth_call.json()["token"]

    def execute_tql_query(self):
        tql_headers = {
            "Authorization": "Bearer " + self.token,
            "Content-Type": "application/json"
        }
        execute_tql = requests.post(UCMDB_ENDPOINT + "/topology", data="Redhat_Servers", headers=tql_headers,
                                    verify=False)
        j_out_dict = json.loads(execute_tql.text)
        self.cis = j_out_dict["cis"]
        self.relations = j_out_dict["relations"]

    def get_relations(self, ucmdbId):
        for r in self.relations:
            return r['end2Id'] if r['end1Id'] == ucmdbId else r['end2Id']

    def get_ip_address(self, ucmdbId):
        for c in self.cis:
            if c['ucmdbId'] == ucmdbId:
                return c['properties']['display_label']

    def __init__(self):

        self.result = {}
        self.result['_meta'] = {}
        self.result['_meta']['hostvars'] = {}

        self.authenticate()
        self.execute_tql_query()

        for ci in self.cis:
            if ci['type'] == "unix":
                ip_address = self.get_ip_address(self.get_relations(ci['ucmdbId']))
                properties = ci['properties']
                hostname = ci['properties']['display_label']
                os_vendor = ci['properties']['os_vendor']
                os_family = ci['properties']['os_family']
                discovered_os_version = ci['properties']['discovered_os_version']
                maintenance_interval = ci['properties']['maintenance_interval']
                maintenance_date = ci['properties']['maintenance_date']
                self.result['_meta']['hostvars'][hostname] = {}
                self.result['_meta']['hostvars'][hostname]['ip_address'] = ip_address
                self.result['_meta']['hostvars'][hostname]['os_vendor'] = os_vendor
                self.result['_meta']['hostvars'][hostname]['os_family'] = os_family
                self.result['_meta']['hostvars'][hostname]['discovered_os_version'] = discovered_os_version
                self.result['_meta']['hostvars'][hostname]['maintenance_interval'] = maintenance_interval
                self.result['_meta']['hostvars'][hostname]['maintenance_date'] = maintenance_date
                print(json.dumps(self.result))


UcmdbDynamicInventory()
