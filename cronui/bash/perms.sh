#!/bin/bash
# -*- ENCODING: UTF-8 -*-

sudo head actualcron.txt >> /etc/cronui/cache/fullcron
sudo head actualcron.txt >> /etc/crontab
