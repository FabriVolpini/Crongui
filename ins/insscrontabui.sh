#!/bin/bash
# -*- ENCODING: UTF-8 -*-

echo "Instalando..."
sleep 1s
sudo cp -r cronui /etc
cd /etc
chmod 664 crontab
sudo sed -n 15p crontab >> /etc/cronui/cache/line15
sudo python /etc/cronui/cache/line.py
echo "Listo!"
sleep 2s
clear
exit
