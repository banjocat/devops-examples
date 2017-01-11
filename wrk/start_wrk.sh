#!/bin/bash

CONFIG_FILE=/tmp/wrk/wrk.lua
touch $CONFIG_FILE
truncate --size 0 $CONFIG_FILE
WRK_METHOD=${WRK_METHOD:-GET}
WRK_BODY=${WRK_BODY:-''}
WRK_CONTENT_TYPE=${WRK_CONTENT_TYPE:-/txt/plain}

echo "wrk.method = \"$WRK_METHOD\"" >> $CONFIG_FILE
echo "wrk.body = '$WRK_BODY'" >> $CONFIG_FILE
echo "wrk.headers[\"Content-Type\"] = \"$WRK_CONTENT_TYPE\"" >> $CONFIG_FILE

/tmp/wrk/wrk -s $CONFIG_FILE -d $WRK_DURATION -t $WRK_THREADS -c $WRK_CONNECTIONS http://${WRK_URL}
    
