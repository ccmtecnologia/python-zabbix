#!/usr/bin/python
from pyzabbix import ZabbixAPI
import array

URL_ZABBIX=""
USER_ZABBIX=""
PASSWORD_ZABBIX=""

zapi = ZabbixAPI(URL_ZABBIX)
zapi.login(USER_ZABBIX, PASSWORD_ZABBIX)

# Coletando GroupID JEDISQUAD
find = zapi.hostgroup.get(output="name, groupid", filter={"name": ["CCM-JEDISQUAD"]})
JEDI_GROUPID = find[0]['groupid']

# Coletando GroupID CLOUDGUARDIANS
find = zapi.hostgroup.get(output="name, groupid", filter={"name": ["CCM-CLOUDGUARDIANS"]})
CLOUDGUARDIANS_GROUPID = find[0]['groupid']

HOSTS_WITHOUTGROUPS = []

# Coletando Hosts
find = zapi.host.get(output=["name"], selectGroups=[],monitored_hosts=1)
for host in find:
        groups = []
        for group in host['groups']:
            groups.append(group['groupid'])
        if (JEDI_GROUPID not in groups) and (CLOUDGUARDIANS_GROUPID not in groups):
            HOSTS_WITHOUTGROUPS.append(host['name'])
        # Limpa variavel para proximo for
        del groups[:]

for host in HOSTS_WITHOUTGROUPS:
    print host
