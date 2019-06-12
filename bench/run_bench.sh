#!/bin/bash
set -ex

if [ -f /var/log/mysql/mysql-slow.sql ]; then
    sudo mv /var/log/mysql/mysql-slow.sql /var/log/mysql/mysql-slow.sql.$(date "+%Y%m%d_%H%M%S")
fi
if [ -f /var/log/nginx/access.log ]; then
    sudo mv /var/log/nginx/access.log /var/log/nginx/access.log.$(date "+%Y%m%d_%H%M%S")
fi
if [ -f /var/log/nginx/error.log ]; then
    sudo mv /var/log/nginx/error.log /var/log/nginx/error.log.$(date "+%Y%m%d_%H%M%S")
fi
sudo systemctl restart mysql
sudo service memcached restart
sudo systemctl restart isubata.python
sudo systemctl restart nginx

./bin/bench -remotes=127.0.0.1 -output result.json
