## Nagios
Nagios objects are defined as environmental variables

### Examples
```
host_0="user=linux-server;host_name=jackmuratore.com;alias=jack;address=www.jackmuratore.com"
```
This will expand to
```
host {
    user linux-server
    host_name jackmuratore.com
    alias jack
    address www.jackmuratore.com
}
```

The parser uses the first part of the key to determine the object name. Another example would be
```
command_12="command_name=check_app;command_line=nmap -p 80 localhost"
```
This will expand to
```
command {
    command_name check_app
    command_line nmap -p 80 localhost
}
```

Current supported defines are
* host
* hostgroup
* service
* contact
* service
* contactgroup
* command

    
