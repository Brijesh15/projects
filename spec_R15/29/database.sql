-- MySQL dump 10.13  Distrib 5.7.28, for Linux (x86_64)
--
-- Host: localhost    Database: 5g
-- ------------------------------------------------------
-- Server version	5.7.28-0ubuntu0.16.04.2

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `accessAndMobilitySubscriptionData`
--

DROP TABLE IF EXISTS `accessAndMobilitySubscriptionData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `accessAndMobilitySubscriptionData` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ueid` varchar(500) DEFAULT NULL,
  `plmn` varchar(6) DEFAULT NULL,
  `supportedFeaturesID` int(11) DEFAULT NULL,
  `gpsis` varchar(500) DEFAULT NULL,
  `internalGroupIds` varchar(500) DEFAULT NULL,
  `subscribedUeAmbr` json DEFAULT NULL,
  `nssaiID` int(11) DEFAULT NULL,
  `ratRestrictions` varchar(500) DEFAULT NULL,
  `coreNetworkTypeRestrictions` varchar(500) DEFAULT NULL,
  `rfspIndex` int(11) DEFAULT NULL,
  `subsRegTimer` int(11) DEFAULT NULL,
  `ueUsageType` int(11) DEFAULT NULL,
  `mpsPriority` tinyint(1) DEFAULT NULL,
  `mcsPriority` tinyint(1) DEFAULT NULL,
  `activeTime` int(11) DEFAULT NULL,
  `dlPacketCount` int(11) DEFAULT NULL,
  `sorInfoID` int(11) DEFAULT NULL,
  `upuInfoID` int(11) DEFAULT NULL,
  `micoAllowed` tinyint(1) DEFAULT NULL,
  `sharedAmDataIds` varchar(500) DEFAULT NULL,
  `odbPacketServices` varchar(500) DEFAULT NULL,
  `subscribedDnnListID` int(11) DEFAULT NULL,
  `nssaiInclusionAllowed` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `nssai` (`nssaiID`),
  KEY `sorInfo` (`sorInfoID`),
  KEY `upuInfo` (`upuInfoID`),
  KEY `subscribedDnnList` (`subscribedDnnListID`),
  KEY `supportedFeaturesID` (`supportedFeaturesID`),
  CONSTRAINT `accessAndMobilitySubscriptionData_ibfk_1` FOREIGN KEY (`nssaiID`) REFERENCES `nssai` (`id`),
  CONSTRAINT `accessAndMobilitySubscriptionData_ibfk_3` FOREIGN KEY (`sorInfoID`) REFERENCES `sorInfo` (`id`),
  CONSTRAINT `accessAndMobilitySubscriptionData_ibfk_4` FOREIGN KEY (`upuInfoID`) REFERENCES `upuInfo` (`id`),
  CONSTRAINT `accessAndMobilitySubscriptionData_ibfk_5` FOREIGN KEY (`subscribedDnnListID`) REFERENCES `subscribedDnnList` (`id`),
  CONSTRAINT `accessAndMobilitySubscriptionData_ibfk_6` FOREIGN KEY (`supportedFeaturesID`) REFERENCES `supportedFeatures` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `accessAndMobilitySubscriptionData`
--

LOCK TABLES `accessAndMobilitySubscriptionData` WRITE;
/*!40000 ALTER TABLE `accessAndMobilitySubscriptionData` DISABLE KEYS */;
INSERT INTO `accessAndMobilitySubscriptionData` VALUES (1,'imsi-311480012345674','311480',1,'01234567498765','abc123de-123-12-acd2ef5be9','{\"uplink\": 311.48, \"downlink\": 311.48}',1,'NR','5GC',1,10,1,0,0,1,1,1,1,0,'12314-.','ALL_PACKET_SERVICES',1,0);
/*!40000 ALTER TABLE `accessAndMobilitySubscriptionData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `amf3GppAccessRegistration`
--

DROP TABLE IF EXISTS `amf3GppAccessRegistration`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `amf3GppAccessRegistration` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ueid` varchar(500) DEFAULT NULL,
  `amfInstanceId` varchar(500) DEFAULT NULL,
  `supportedFeaturesID` int(11) DEFAULT NULL,
  `purgeFlag` tinyint(1) DEFAULT NULL,
  `pei` varchar(500) DEFAULT NULL,
  `imsVoPs` varchar(500) DEFAULT NULL,
  `deregCallbackUri` varchar(500) DEFAULT NULL,
  `amfServiceNameDeregID` int(11) DEFAULT NULL,
  `pcscfRestorationCallbackUri` varchar(500) DEFAULT NULL,
  `amfServiceNamePcscfRestID` int(11) DEFAULT NULL,
  `initialRegistrationInd` tinyint(1) DEFAULT NULL,
  `guamiID` int(11) DEFAULT NULL,
  `backupAmfInfoID` int(11) DEFAULT NULL,
  `drFlag` tinyint(1) DEFAULT NULL,
  `ratType` varchar(500) DEFAULT NULL,
  `urrpIndicator` tinyint(1) DEFAULT NULL,
  `amfEeSubscriptionId` varchar(500) DEFAULT NULL,
  `epsInterworkingInfo` varchar(500) DEFAULT NULL,
  `ueSrvccCapability` tinyint(1) DEFAULT NULL,
  `nid` varchar(500) DEFAULT NULL,
  `registrationTime` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `guami` (`guamiID`),
  KEY `backupAmfInfo` (`backupAmfInfoID`),
  KEY `amfServiceNameDereg` (`amfServiceNameDeregID`),
  KEY `amfServiceNamePcscfRest` (`amfServiceNamePcscfRestID`),
  KEY `supportedFeaturesID` (`supportedFeaturesID`),
  CONSTRAINT `amf3GppAccessRegistration_ibfk_1` FOREIGN KEY (`guamiID`) REFERENCES `guami` (`id`),
  CONSTRAINT `amf3GppAccessRegistration_ibfk_2` FOREIGN KEY (`backupAmfInfoID`) REFERENCES `backupAmfInfo` (`id`),
  CONSTRAINT `amf3GppAccessRegistration_ibfk_3` FOREIGN KEY (`amfServiceNameDeregID`) REFERENCES `serviceName` (`id`),
  CONSTRAINT `amf3GppAccessRegistration_ibfk_4` FOREIGN KEY (`amfServiceNamePcscfRestID`) REFERENCES `serviceName` (`id`),
  CONSTRAINT `amf3GppAccessRegistration_ibfk_5` FOREIGN KEY (`supportedFeaturesID`) REFERENCES `supportedFeatures` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `amf3GppAccessRegistration`
--

LOCK TABLES `amf3GppAccessRegistration` WRITE;
/*!40000 ALTER TABLE `amf3GppAccessRegistration` DISABLE KEYS */;
INSERT INTO `amf3GppAccessRegistration` VALUES (1,'imsi-311480012345674','a87460c6-5192-11ea-af09-b0c090b6cc6d',1,0,'imei-346145012345674','HOMOGENEOUS_SUPPORT','string',1,'string',1,0,1,1,0,'NR',0,'string','string',0,'string','string');
/*!40000 ALTER TABLE `amf3GppAccessRegistration` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authEvent`
--

DROP TABLE IF EXISTS `authEvent`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authEvent` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nfInstanceId` varchar(500) DEFAULT NULL,
  `success` tinyint(1) DEFAULT NULL,
  `timeStamp` varchar(500) DEFAULT NULL,
  `authType` varchar(500) DEFAULT NULL,
  `servingNetworkName` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authEvent`
--

LOCK TABLES `authEvent` WRITE;
/*!40000 ALTER TABLE `authEvent` DISABLE KEYS */;
INSERT INTO `authEvent` VALUES (1,'a87460c6-5192-11ea-af09-b0c090b6cc6d',0,'2020-02-17T14:41:59Z','5G_AKA','5G:mnc311.mcc480.3gppnetwork.org');
/*!40000 ALTER TABLE `authEvent` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authenticationSubscription`
--

DROP TABLE IF EXISTS `authenticationSubscription`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `authenticationSubscription` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ueId` varchar(500) NOT NULL,
  `supportedFeaturesID` int(11) DEFAULT NULL,
  `authenticationMethod` varchar(500) DEFAULT NULL,
  `encPermanentKey` varchar(500) DEFAULT NULL,
  `protectionParameterId` varchar(500) DEFAULT NULL,
  `authenticationManagementField` varchar(500) DEFAULT NULL,
  `algorithmId` varchar(500) DEFAULT NULL,
  `encOpcKey` varchar(500) DEFAULT NULL,
  `encTopcKey` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`,`ueId`),
  KEY `supportedFeaturesID` (`supportedFeaturesID`),
  CONSTRAINT `authenticationSubscription_ibfk_1` FOREIGN KEY (`supportedFeaturesID`) REFERENCES `supportedFeatures` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authenticationSubscription`
--

LOCK TABLES `authenticationSubscription` WRITE;
/*!40000 ALTER TABLE `authenticationSubscription` DISABLE KEYS */;
INSERT INTO `authenticationSubscription` VALUES (1,'imsi-311480012345674',1,'5G_AKA','string','string','8101','string','5f1d289c5d354d0a140c2548f5f3e3ba','465b5ce8b199b49faa5f0a2ee238a6bc');
/*!40000 ALTER TABLE `authenticationSubscription` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `backupAmfInfo`
--

DROP TABLE IF EXISTS `backupAmfInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `backupAmfInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `backupAmf` varchar(500) DEFAULT NULL,
  `guamiListID` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `guamiList` (`guamiListID`),
  CONSTRAINT `backupAmfInfo_ibfk_1` FOREIGN KEY (`guamiListID`) REFERENCES `guami` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `backupAmfInfo`
--

LOCK TABLES `backupAmfInfo` WRITE;
/*!40000 ALTER TABLE `backupAmfInfo` DISABLE KEYS */;
INSERT INTO `backupAmfInfo` VALUES (1,'amfName',1);
/*!40000 ALTER TABLE `backupAmfInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dnn`
--

DROP TABLE IF EXISTS `dnn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dnn` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dnn` varchar(500) DEFAULT NULL,
  `WildcardDnn` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dnn`
--

LOCK TABLES `dnn` WRITE;
/*!40000 ALTER TABLE `dnn` DISABLE KEYS */;
INSERT INTO `dnn` VALUES (1,'VZWIMS','VZWAPP');
/*!40000 ALTER TABLE `dnn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `dnnInfos`
--

DROP TABLE IF EXISTS `dnnInfos`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `dnnInfos` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dnn` int(11) DEFAULT NULL,
  `defaultDnnIndicator` tinyint(1) DEFAULT NULL,
  `lboRoamingAllowed` tinyint(1) DEFAULT NULL,
  `iwkEpsInd` tinyint(1) DEFAULT NULL,
  `dnnBarred` tinyint(1) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `dnn` (`dnn`),
  CONSTRAINT `dnnInfos_ibfk_1` FOREIGN KEY (`dnn`) REFERENCES `dnn` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `dnnInfos`
--

LOCK TABLES `dnnInfos` WRITE;
/*!40000 ALTER TABLE `dnnInfos` DISABLE KEYS */;
INSERT INTO `dnnInfos` VALUES (1,1,0,0,0,0);
/*!40000 ALTER TABLE `dnnInfos` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `forbiddenAreas`
--

DROP TABLE IF EXISTS `forbiddenAreas`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `forbiddenAreas` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ueid` varchar(500) DEFAULT NULL,
  `tacs` varchar(500) DEFAULT NULL,
  `areaCode` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `forbiddenAreas`
--

LOCK TABLES `forbiddenAreas` WRITE;
/*!40000 ALTER TABLE `forbiddenAreas` DISABLE KEYS */;
INSERT INTO `forbiddenAreas` VALUES (1,'imsi-311480012345674','2b4d','1');
/*!40000 ALTER TABLE `forbiddenAreas` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `guami`
--

DROP TABLE IF EXISTS `guami`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `guami` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plmn` varchar(6) DEFAULT NULL,
  `amfId` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `guami`
--

LOCK TABLES `guami` WRITE;
/*!40000 ALTER TABLE `guami` DISABLE KEYS */;
INSERT INTO `guami` VALUES (1,'311480','abf12c');
/*!40000 ALTER TABLE `guami` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `nssai`
--

DROP TABLE IF EXISTS `nssai`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `nssai` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `supportedFeaturesID` int(11) DEFAULT NULL,
  `defaultSingleNssais` json DEFAULT NULL,
  `singleNssais` json DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `supportedFeaturesID` (`supportedFeaturesID`),
  CONSTRAINT `nssai_ibfk_1` FOREIGN KEY (`supportedFeaturesID`) REFERENCES `supportedFeatures` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `nssai`
--

LOCK TABLES `nssai` WRITE;
/*!40000 ALTER TABLE `nssai` DISABLE KEYS */;
INSERT INTO `nssai` VALUES (1,1,'{\"sd\": \"a2b391\", \"sst\": 0}','{\"sd\": \"a2b391\", \"sst\": 0}');
/*!40000 ALTER TABLE `nssai` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `plmn`
--

DROP TABLE IF EXISTS `plmn`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `plmn` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `plmnId` varchar(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `plmn`
--

LOCK TABLES `plmn` WRITE;
/*!40000 ALTER TABLE `plmn` DISABLE KEYS */;
INSERT INTO `plmn` VALUES (1,NULL);
/*!40000 ALTER TABLE `plmn` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sequenceNumber`
--

DROP TABLE IF EXISTS `sequenceNumber`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sequenceNumber` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ueId` varchar(500) NOT NULL,
  `sqnScheme` varchar(500) DEFAULT NULL,
  `sqn` varchar(500) DEFAULT NULL,
  `lastIndexes` int(11) DEFAULT NULL,
  `indLength` int(11) DEFAULT NULL,
  `difSign` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`,`ueId`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sequenceNumber`
--

LOCK TABLES `sequenceNumber` WRITE;
/*!40000 ALTER TABLE `sequenceNumber` DISABLE KEYS */;
INSERT INTO `sequenceNumber` VALUES (1,'imsi-311480012345674','GENERAL','a12bf1234567',1,1,'POSITIVE');
/*!40000 ALTER TABLE `sequenceNumber` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `serviceAreaRestriction`
--

DROP TABLE IF EXISTS `serviceAreaRestriction`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `serviceAreaRestriction` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ueid` varchar(500) DEFAULT NULL,
  `restrictionType` varchar(500) DEFAULT NULL,
  `areas` json DEFAULT NULL,
  `maxNumOfTAs` int(11) DEFAULT NULL,
  `maxNumOfTAsForNotAllowedAreas` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `serviceAreaRestriction`
--

LOCK TABLES `serviceAreaRestriction` WRITE;
/*!40000 ALTER TABLE `serviceAreaRestriction` DISABLE KEYS */;
INSERT INTO `serviceAreaRestriction` VALUES (1,'imsi-311480012345674','ALLOWED_AREAS','{\"tacs\": \"2b4d\", \"areaCode\": \"1\"}',0,0);
/*!40000 ALTER TABLE `serviceAreaRestriction` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `serviceName`
--

DROP TABLE IF EXISTS `serviceName`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `serviceName` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `serviceName`
--

LOCK TABLES `serviceName` WRITE;
/*!40000 ALTER TABLE `serviceName` DISABLE KEYS */;
INSERT INTO `serviceName` VALUES (1,'nnrf-nfm'),(2,'nnrf-disc'),(3,'nudm-sdm'),(4,'nudm-uecm'),(5,'nudm-ueau'),(6,'nudm-ee'),(7,'nudm-pp'),(8,'nudm-niddau'),(9,'nudm-mt'),(10,'namf-comm'),(11,'namf-evts'),(12,'namf-mt'),(13,'namf-loc'),(14,'nsmf-pdusession'),(15,'nsmf-event-exposure'),(16,'nausf-auth');
/*!40000 ALTER TABLE `serviceName` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `smfSelectionSubscriptionData`
--

DROP TABLE IF EXISTS `smfSelectionSubscriptionData`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `smfSelectionSubscriptionData` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ueid` varchar(500) DEFAULT NULL,
  `plmn` varchar(500) DEFAULT NULL,
  `supportedFeaturesID` int(11) DEFAULT NULL,
  `subscribedSnssaiInfosID` int(11) DEFAULT NULL,
  `sharedSnssaiInfosId` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `subscribedSnssaiInfosId` (`subscribedSnssaiInfosID`),
  KEY `supportedFeaturesID` (`supportedFeaturesID`),
  CONSTRAINT `smfSelectionSubscriptionData_ibfk_1` FOREIGN KEY (`subscribedSnssaiInfosID`) REFERENCES `dnnInfos` (`id`),
  CONSTRAINT `smfSelectionSubscriptionData_ibfk_2` FOREIGN KEY (`supportedFeaturesID`) REFERENCES `supportedFeatures` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `smfSelectionSubscriptionData`
--

LOCK TABLES `smfSelectionSubscriptionData` WRITE;
/*!40000 ALTER TABLE `smfSelectionSubscriptionData` DISABLE KEYS */;
INSERT INTO `smfSelectionSubscriptionData` VALUES (1,'imsi-311480012345674','311480',1,1,'234156-.');
/*!40000 ALTER TABLE `smfSelectionSubscriptionData` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `sorInfo`
--

DROP TABLE IF EXISTS `sorInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `sorInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `steeringContainer` json DEFAULT NULL,
  `ackInd` tinyint(1) DEFAULT NULL,
  `sorMacIausf` varchar(500) DEFAULT NULL,
  `countersor` varchar(500) DEFAULT NULL,
  `provisioningTime` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `sorInfo`
--

LOCK TABLES `sorInfo` WRITE;
/*!40000 ALTER TABLE `sorInfo` DISABLE KEYS */;
INSERT INTO `sorInfo` VALUES (1,'{\"plmnId\": 311480, \"AccessTech\": \"NR\"}',0,'b0c090b6cc6d23abfe12bdef340569cd','ac32','string');
/*!40000 ALTER TABLE `sorInfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `subscribedDnnList`
--

DROP TABLE IF EXISTS `subscribedDnnList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `subscribedDnnList` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `ueid` varchar(500) DEFAULT NULL,
  `dnn` varchar(500) DEFAULT NULL,
  `WildcardDnn` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `subscribedDnnList`
--

LOCK TABLES `subscribedDnnList` WRITE;
/*!40000 ALTER TABLE `subscribedDnnList` DISABLE KEYS */;
INSERT INTO `subscribedDnnList` VALUES (1,'imsi-311480012345674','VZWIMS','VZWAPP');
/*!40000 ALTER TABLE `subscribedDnnList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `supportedFeatures`
--

DROP TABLE IF EXISTS `supportedFeatures`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `supportedFeatures` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `supportedFeaturesName` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `supportedFeatures`
--

LOCK TABLES `supportedFeatures` WRITE;
/*!40000 ALTER TABLE `supportedFeatures` DISABLE KEYS */;
INSERT INTO `supportedFeatures` VALUES (1,'7f0ffc80');
/*!40000 ALTER TABLE `supportedFeatures` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `upuDataList`
--

DROP TABLE IF EXISTS `upuDataList`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `upuDataList` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `secPacket` varchar(500) DEFAULT NULL,
  `defaultConfNssaiId` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `defaultConfNssaiId` (`defaultConfNssaiId`),
  CONSTRAINT `upuDataList_ibfk_1` FOREIGN KEY (`defaultConfNssaiId`) REFERENCES `nssai` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `upuDataList`
--

LOCK TABLES `upuDataList` WRITE;
/*!40000 ALTER TABLE `upuDataList` DISABLE KEYS */;
INSERT INTO `upuDataList` VALUES (1,'string',1);
/*!40000 ALTER TABLE `upuDataList` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `upuInfo`
--

DROP TABLE IF EXISTS `upuInfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `upuInfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `upuDataListID` int(11) DEFAULT NULL,
  `upuRegInd` tinyint(1) DEFAULT NULL,
  `upuAckInd` tinyint(1) DEFAULT NULL,
  `upuMacIausf` varchar(500) DEFAULT NULL,
  `counterUpu` varchar(500) DEFAULT NULL,
  `provisioningTime` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `upuDataListID` (`upuDataListID`),
  CONSTRAINT `upuInfo_ibfk_1` FOREIGN KEY (`upuDataListID`) REFERENCES `backupAmfInfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `upuInfo`
--

LOCK TABLES `upuInfo` WRITE;
/*!40000 ALTER TABLE `upuInfo` DISABLE KEYS */;
INSERT INTO `upuInfo` VALUES (1,1,0,0,'b0c090b6cc6d23abfe12bdef340569cd','ac32','string');
/*!40000 ALTER TABLE `upuInfo` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-02-19 16:46:27
