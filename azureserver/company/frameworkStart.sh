#!/bin/bash
$HOME/.AmantyaEnvs/FrameworkEnvs/bin/python /srv/company/djangoServer/manage.py runserver 0.0.0.0:8005 > /var/log/companylogs 2>&1 &
#$HOME/.AmantyaEnvs/FrameworkEnvs/bin/python /srv/company/djangoServer/manage.py runserver 8005 
