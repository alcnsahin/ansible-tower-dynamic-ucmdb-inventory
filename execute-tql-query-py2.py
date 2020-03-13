#!/usr/bin/env python

import json
import urllib2
import argparse
import sys
import ssl

UCMDB_ENDPOINT = "https://cmdb-hostname:port/rest-api"
UCMDB_USERNAME = 'username'
UCMDB_PASSWORD = 'password'
UCMDB_CLIENT_CONTEXT = 1

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


class UcmdbDynamicInventory(object):

    def parse_options(self):
        parser = argparse.ArgumentParser()
        parser.add_argument('--host', nargs=1)
        parser.add_argument('--list', action='store_true')
        parser.add_argument('--pretty', action='store_true')
        self.options = parser.parse_args()

    def authenticate(self):
        auth_params = {
            'username': UCMDB_USERNAME,
            'password': UCMDB_PASSWORD,
            'clientContext': UCMDB_CLIENT_CONTEXT
        }
        auth_call = urllib2.Request(UCMDB_ENDPOINT + "/authenticate")
        auth_call.add_header("Content-Type", "application/json")
        response = urllib2.urlopen(auth_call, data=json.dumps(auth_params), context=ctx)
        self.token = json.loads(response.read())['token']

    def execute_tql_query(self):
        execute_tql = urllib2.Request(UCMDB_ENDPOINT + "/topology")
        execute_tql.add_header("Authorization", "Bearer " + self.token)
        execute_tql.add_header("Content-Type", "application/json")
        tql_response = urllib2.urlopen(execute_tql, data="Redhat_Servers", context=ctx)
        j_out_dict = json.loads(tql_response.read())
        self.cis = json.loads(j_out_dict)["cis"]
        self.relations = json.loads(j_out_dict)["relations"]

    def get_relations(self, ucmdbId):
        for r in self.relations:
            return r['end2Id'] if r['end1Id'] == ucmdbId else r['end2Id']

    def get_ip_address(self, ucmdbId):
        for c in self.cis:
            if c['ucmdbId'] == ucmdbId:
                return c['properties']['display_label']

    def __init__(self):

        self.defaultgroup = 'group_all'
        self.options = None

        self.token = None
        self.cis = None
        self.relations = None

        self.result = {}
        self.result['_meta'] = {}
        self.result['_meta']['hostvars'] = {}
        self.result['all'] = {}
        self.result['all']['children'] = ["unix"]
        self.result['unix'] = {}
        self.result['unix']['children'] = []
        self.result['unix']['hosts'] = []

        self.parse_options()
        self.authenticate()
        self.execute_tql_query()

        self.json_indent = None
        if self.options.pretty:
            self.json_indent = 2

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
                self.result['unix']['hosts'] = hostname

        if self.options.host:
            print(json.dumps(self.result['_meta']['hostvars'][self.options.host[0]], indent=self.json_indent))
        elif self.options.list:
            print(json.dumps(self.result, indent=self.json_indent))
        else:
            sys.exit("usage: --list or --host HOSTNAME [--pretty]")


UcmdbDynamicInventory()
