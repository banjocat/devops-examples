#!/bin/bash

cd /tmp
python ./create_config.py > /usr/local/nagios/etc/objects/docker/generated.cfg
        
supervisord -n -c /etc/supervisor/supervisord.conf
