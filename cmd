screen copy mode ctrl >a >esc
:w !sudo tee %
python manage.py migrate --fake scanQRcode zero

set python 3.6 as default on linux 16:

sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
update-alternatives --config python3

upgrade pip3:
sudo -H pip3 install --upgrade pip

install mysqlclient:
sudo apt-get install python3.6-dev libmysqlclient-dev
pip3 install mysqlclient

resolve issue After upgrading python 3.5 to 3.6
open tty1 terminal
cd /usr/lib/python3/dist-packages/gi/ 
sudo cp _gi.cpython-35m-x86_64-linux-gnu.so _gi.cpython-36m-x86_64-linux-gnu.so 
sudo cp _gi_cairo.cpython-35m-x86_64-linux-gnu.so _gi_cairo.cpython-36m-x86_64-linux-gnu.s

install Mysql database:
sudo apt-get update
sudo apt-get install mysql-server
Securing MySQL:
sudo mysql_secure_installation
Creating MySQL Users:
mysql -u root -p
CREATE USER 'mynewuser'@'localhost' IDENTIFIED BY 'goodPassword';
GRANT ALL PRIVILEGES ON * . * TO 'mynewuser'@'localhost';
FLUSH PRIVILEGES;
New User Connection:
mysql -u mynewuser -p
Create database:
CREATE DATABASE fullstackpython;
use fullstackpython;
CREATE TABLE pages (name VARCHAR(50), url VARCHAR(1024));
get user list:
SELECT User FROM mysql.user;
delete user:
DROP USER 'jeffrey'@'localhost';


insert into table:
insert into company_qrcode (flag) values(False) where id=2;
update data in table
update company_qrcode set flag=False where company_id=1;
modify column in table:
ALTER TABLE table_name MODIFY column_name column_definition [ FIRST | AFTER column_name ];
Drop column in table:
ALTER TABLE table_name DROP COLUMN column_name;
Rename column in table:
ALTER TABLE table_name CHANGE COLUMN old_name new_name column_definition [ FIRST | AFTER column_name ]
Rename table:
ALTER TABLE table_name RENAME TO new_table_name;
Add column in table:
ALTER TABLE table_name ADD new_column_name column_definition [ FIRST | AFTER column_name ];
verify validate password policy
SHOW VARIABLES LIKE 'validate_password%';
SET GLOBAL validate_password_policy=LOW;
drop forgein key:
alter table guami drop foreign key guami_ibfk_1;
show forgien key constraint:
show create table table_name;
if redis is not connecting to localhost 111 error code:
sudo apt-get install redis-server
add another primary key
ALTER TABLE amf3GppAccessRegistration DROP PRIMARY KEY, ADD PRIMARY KEY(id, ueid);
github link of 5GC_APIs:
https://github.com/jdegre/5GC_APIs/blob/master/README.md 



5gdatabase:-
create sequenceNumber:-
create table sequenceNumber (id INT NOT NULL AUTO_INCREMENT, ueId varchar(500), sqnScheme varchar(500), sqn varchar(500), lastIndexes int, indLength int, difSign varchar(500), PRIMARY KEY (id, ueId));

create authenticationSubscription:-
create table authenticationSubscription (id INT NOT NULL AUTO_INCREMENT, ueId varchar(500), supportedFeaturesID int, authenticationMethod varchar(500), encPermanentKey varchar(500), protectionParameterId varchar(500),authenticationManagementField varchar(500), algorithmId varchar(500), encOpcKey varchar(500), encTopcKey varchar(500), PRIMARY KEY (id, ueId), FOREIGN KEY (supportedFeaturesId) REFERENCES supportedFeatures (id));
create plmn table:
create table plmn (id int not null auto_increment primary key, plmnId json);
create guami table:
create table guami (id int not null auto_increment primary key, plmnId varchar(6), amfId varchar(500));
create serviceName table:
create table serviceName (id int not null auto_increment primary key, name varchar(500));
create backamfInfo Table:
create table backupAmfInfo (id int not null auto_increment primary key, backupAmf varchar(500), guamiListID int, foreign key (guamiListID) references guami(id));

create table AuthEvent (id INT NOT NULL AUTO_INCREMENT, nfInstanceId varchar(500), success boolean, timeStamp varchar(500), authType varchar(500), servingNetworkName varchar(500), PRIMARY KEY (id));

create amf3GppAccessRegistration:
create table amf3GppAccessRegistration (id int not null auto_increment primary key, amfInstanceId varchar(500), supportedFeaturesID int, purgeFlag varchar(500), pei varchar(500), imsVoPs varchar(500), deregCallbackUri varchar(500), amfServiceNameDeregID int, pcscfRestorationCallbackUri varchar(500), amfServiceNamePcscfRestID int, initialRegistrationInd boolean, guami int, backupAmfInfoID int, drFlag varchar(500), ratType varchar(500), urrpIndicator varchar(500), amfEeSubscriptionId varchar(500), epsInterworkingInfo varchar(500), foreign key (guami) references guami(id));
alter table Amf3GppAccessRegistration ADD FOREIGN KEY (backupAmfInfoID) REFERENCES backupAmfInfo(id);
alter table Amf3GppAccessRegistration ADD FOREIGN KEY (amfServiceNameDeregID) REFERENCES serviceName(id);
alter table Amf3GppAccessRegistration ADD FOREIGN KEY (amfServiceNamePcscfRestID) REFERENCES serviceName(id);
alter table Amf3GppAccessRegistration ADD FOREIGN KEY (supportedFeaturesID) REFERENCES supportedFeatures(id);

create table forbiddenAreas: 
create table forbiddenAreas (id int not null auto_increment primary key, ueid varchar(500), tacs varchar(500), areaCode varchar(500));
create sorInfo:
create table sorInfo (id int not null auto_increment primary key, ackInd boolean, sorMacIausf varchar(500), countersor varchar(500), provisioningTime varchar(500));
create nssai:
create table nssai (id int not null auto_increment primary key, supportedFeaturesID int, defaultSingleNssais json, singleNssais json, foreign key (supportedFeaturesID) references supportedFeatures(id));
create survicearearestriction:
create table serviceAreaRestriction (id int not null auto_increment primary key, ueid varchar(500), restrictionType varchar(500), areas json, maxNumOfTAs int, maxNumOfTAsForNotAllowedAreas int);
create upudatalist:
create table upuDataList (id int not null auto_increment primary key, secPacket varchar(500), defaultConfNssaiId int, foreign key (defaultConfNssaiId) references nssai(id));
create upuInfo:
create table upuInfo (id int not null auto_increment primary key, upuDataList int, upuRegInd boolean, upuAckInd boolean, upuMacIausf varchar(500), counterUpu varchar(500), provisioningTime varchar(500));
create subscribedDnnList:
create table subscribedDnnList (id int not null auto_increment primary key, ueid varchar(500), dnn varchar(500), WildcardDnn varchar(500));
create AccessAndMobilitySubscriptionData:

create table accessAndMobilitySubscriptionData (id int not null auto_increment primary key,ueid varchar(500), plmn int, supportedFeaturesID int ,gpsis varchar(500),internalGroupIds varchar(500),subscribedUeAmbr json,nssaiID int, ratRestrictions varch(500),coreNetworkTypeRestrictions varchar(500),rfspIndex int, subsRegTimer int, ueUsageType int, mpsPriority boolean, mcsPriority boolean, activeTime int, dlPacketCount int, sorInfoID int, upuInfoID int, micoAllowed boolean, sharedAmDataIds varchar(500), odbPacketServices varchar(500), subscribedDnnListID int, nssaiInclusionAllowed boolean, foreign key (nssaiID) references nssai(id));
alter table AccessAndMobilitySubscriptionData ADD FOREIGN KEY (supportedFeaturesID) REFERENCES supportedFeatures(id);
alter table AccessAndMobilitySubscriptionData ADD FOREIGN KEY (sorInfoID) REFERENCES sorInfo(id);
alter table AccessAndMobilitySubscriptionData ADD FOREIGN KEY (upuInfoID) REFERENCES upuInfo(id);
alter table AccessAndMobilitySubscriptionData ADD FOREIGN KEY (subscribedDnnListID) REFERENCES subscribedDnnList(id);

create dnn table:
create table dnn (id int not null auto_increment primary key, dnn varchar(500), WildcardDnn varchar(500));
create dnn info:
create table dnnInfos (id int not null auto_increment primary key, dnn int, defaultDnnIndicator boolean, lboRoamingAllowed boolean, iwkEpsInd boolean, dnnBarred boolean, foreign key (dnn) references dnn(id));

create table smfSelectionSubscriptionData:
create table smfSelectionSubscriptionData (id int not null auto_increment primary key, ueid varchar(500), plmn varchar(6), supportedFeaturesID int, subscribedSnssaiInfosID int,sharedSnssaiInfosId varchar(500),foreign key (subscribedSnssaiInfosID) references dnnInfos(id));
alter table SmfSelectionSubscriptionData ADD FOREIGN KEY (supportedFeaturesID) REFERENCES supportedFeatures(id);











