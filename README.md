# UCMDB Dynamic Inventory Plugin for Ansible Tower

These scripts are basic examples to get dynamic inventory from Microfocus UCMDB. I developed these scripts for a specific purpose. 

These scripts calls tql query named "Redhat_Servers" from ucmdb and returns some unix servers.

### execute-tql-query-py2.py

`tested on Python 2.7.5`

**usage:** 
    
    python execute-tql-query-py2.py --list
    python execute-tql-query-py2.py --list --pretty
    python execute-tql-query-py2.py --hostname <hostname>
    python execute-tql-query-py2.py --hostname <hostname> --pretty

### execute-tql-query-py3.py

`tested on Python 3.6.9`

**usage:** 
    
    python execute-tql-query-py3.py --list
    python execute-tql-query-py3.py --list --pretty
    python execute-tql-query-py3.py --hostname <hostname>
    python execute-tql-query-py3.py --hostname <hostname> --pretty
    


**Example Output:**
```json
{
   "all":{
      "children":[
         "unix"
      ]
   },
   "unix":{
      "hosts":[
         "test5",
         "test1",
         "test2",
         "test4",
         "test3"
      ],
      "children":[

      ]
   },
   "_meta":{
      "hostvars":{
         "test1":{
            "maintenance_interval":"10:00 - 17:00",
            "discovered_os_version":"7.4",
            "maintenance_date":"Cumartesi",
            "os_family":"unix",
            "ip_address":"192.168.1.1",
            "os_vendor":"red_hat_software"
         },
         "test2":{
            "maintenance_interval":"10:00 - 17:00",
            "discovered_os_version":"6.9",
            "maintenance_date":"Cumartesi",
            "os_family":"unix",
            "ip_address":"192.168.1.2",
            "os_vendor":"red_hat_software"
         },
         "test3":{
            "maintenance_interval":"10:00 - 17:00",
            "discovered_os_version":"7.4",
            "maintenance_date":"Cumartesi",
            "os_family":"unix",
            "ip_address":"192.168.1.3",
            "os_vendor":"red_hat_software"
         },
         "test4":{
            "maintenance_interval":"10:00 - 17:00",
            "discovered_os_version":"7.4",
            "maintenance_date":"Cumartesi",
            "os_family":"unix",
            "ip_address":"192.168.1.4",
            "os_vendor":"red_hat_software"
         },
         "test5":{
            "maintenance_interval":"10:00 - 17:00",
            "discovered_os_version":"7.4",
            "maintenance_date":"Cumartesi",
            "os_family":"unix",
            "ip_address":"192.168.1.5",
            "os_vendor":"red_hat_software"
         }
      }
   }
}
```