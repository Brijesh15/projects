#!/bin/bash

pass=root@123
sudo apt-get update
sudo apt-get install mysql-server
sudo mysql_secure_installation
sudo mysql -u root -p$pass -e "grant all privileges ON * . * TO 'root'@'localhost' with grant option;"
sudo mysql -u root -p$pass -e "flush privileges;"
sudo mysql -u root -p$pass -e "CREATE DATABASE company;"
sudo mysql -u root -p$pass -e "show databases;"
#sudo mysql -u root -p$pass -e "use company;"
sudo mysql -u root -p$pass company -e "CREATE TABLE company_list (company_id int NOT NULL AUTO_INCREMENT, company_name VARCHAR(200), PRIMARY KEY (company_id));"
#sudo mysql -u root -p$pass company -e "CREATE TABLE company_qrcode (id INT(11) NOT NULL AUTO_INCREMENT, company_id int, scanned_result varchar(50) , qrcode VARCHAR(500), created_at int(11), updated_at int(11), PRIMARY KEY (id));"
#sudo mysql -u root -p$pass -e "drop user 'root'@'localhost';"
#sudo mysql -u root -p$pass -e "set global validate_password_number_count=3;"
#sudo mysql -u root -p$pass -e "set global validate_password_mixed_case_count=0;"
#sudo mysql -u root -p$pass -e "create user 'root'@'localhost' identified by 'root@123';"
#sudo mysql -u root -p$pass -e "grant all privileges ON * . * TO 'root'@'localhost' with grant option;"
#sudo mysql -u root -p$pass -e "flush privileges;"
