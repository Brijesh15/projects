#!/bin/bash

#if (( $# != 2))
# then
#  user=root
#  pass=root@123
#else
#	user=$1
#	pass=$2
#fi

user=root
pass=root@123
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
sudo mysql -u $user -p$pass -e "grant all privileges ON * . * TO 'root'@'localhost' with grant option;"
sudo mysql -u $user -p$pass -e "flush privileges;"
sudo mysql -u $user -p$pass 5g < 5gDatabase.sql

#sudo mysql -u root -p$pass -e "CREATE DATABASE 5g;"
#sudo mysql -u root -p$pass -e "show databases;"
#sudo mysql -u root -p$pass -e "use 5g;"
#sudo mysql -u root -p$pass -e "drop user 'root'@'localhost';"
#sudo mysql -u root -p$pass -e "set global validate_password_number_count=3;"
#sudo mysql -u root -p$pass -e "set global validate_password_mixed_case_count=0;"
#sudo mysql -u root -p$pass -e "create user 'root'@'localhost' identified by 'root@123';"
#sudo mysql -u root -p$pass -e "grant all privileges ON * . * TO 'root'@'localhost' with grant option;"
#sudo mysql -u root -p$pass -e "flush privileges;"
