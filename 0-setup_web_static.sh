#!/usr/bin/env bash
# Prepare your web servers
apt-get update
apt-get install -y nginx
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
touch /data/web_static/releases/test/index.html
echo "THIS IS SOME SIMPLE TEST TEXT" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chgrp -R ubuntu /data/
chown -R ubuntu /data/
echo "server {
    listen 80;
    listen [::]:80 default_server;
    add_header X-Served-By $HOSTNAME;
    root   /etc/nginx/html;
    index  index.html;

    location /hbnb_static {
        alias /data/web_static/current/;
	index index.html;
    }

    location /redirect_me {
        return 301 https://www.instagram.com/rahofahazem/;
    }

    error_page 404 /404.html;
    location = /404.html{
	    root /etc/nginx/html;
	    internal;
    }
}" > /etc/nginx/sites-available/default
service nginx restart
