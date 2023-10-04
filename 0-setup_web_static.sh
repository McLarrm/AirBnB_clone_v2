#!/usr/bin/env bash
# This script sets up web servers for the deployment of web_static.

if ! command -v nginx &>/dev/null; then
    sudo apt-get update
    sudo apt-get -y install nginx
fi

sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/
sudo chown -R ubuntu:ubuntu /data/

echo "<html><head></head><body>Hello, web_static!</body></html>" | sudo tee /data/web_static/releases/test/index.html

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

config_file="/etc/nginx/sites-available/default"
config_block="location /hbnb_static/ {\n\talias /data/web_static/current/;\n}"
sudo sed -i "/location \/ {/a $config_block" $config_file

sudo service nginx restart

exit 0
