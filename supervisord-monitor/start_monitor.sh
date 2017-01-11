#!/bin/bash -e

j2 supervisord.php.j2 > ./application/config/supervisord.php

cd ./application
php -S 0.0.0.0:80
