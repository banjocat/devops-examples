## Nagios
Nagios objects are defined as environmental variables

### Syntax

All configs are defined as
```
(config_name)_#="key1=value;key2=value"
```

#### Examples

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

