#!/bin/bash -e

j2 supervisord.php.j2 > ./application/config/supervisor.php
j2 welcome.php.j2 > ./application/views/welcome.php

cd ./public_html
php -S 0.0.0.0:80
