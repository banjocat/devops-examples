## Nagios
Everything but service checks can be defined as an environmental variable

### Hosts
```
HOST_0="host_name=www.jackmuratore.com;alias=jack;address=www.jackmuratore.com"
```
Hosts must be defined sequentiall. So `HOST_0` and `HOST_1`.. but then don't jump to `HOST_10`. It will map any config for nagios hosts via `key=value` with semicolons seperating the next key.

### Groups.. work in progress
