#!/usr/bin/python
from pyzabbix import ZabbixAPI
import array

URL_ZABBIX=""
USER_ZABBIX=""
PASSWORD_ZABBIX=""

# Fazendo login
zapi = ZabbixAPI(URL_ZABBIX)
zapi.login(USER_ZABBIX, PASSWORD_ZABBIX)

# Coletando todos hosts e seus respectivos status
hosts_dis = zapi.host.get(output=["name", "status"])

# For nos hosts e verifica o status (disable = 1)
for host in hosts_dis:
    status = int(host['status'])
    if (status == 1):
        print host['name']
