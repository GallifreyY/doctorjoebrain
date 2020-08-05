-- MySQL dump 10.13  Distrib 8.0.19, for Win64 (x86_64)
--
-- Host: localhost    Database: doctorjoe
-- ------------------------------------------------------
-- Server version	8.0.19

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `device`
--
DROP TABLE IF EXISTS `device`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `device` (
  `device_name` varchar(255) DEFAULT 'Unrecorded Device',
  `vendor_id` varchar(255) DEFAULT NULL,
  `description` varchar(999) DEFAULT NULL,
  `picture` varchar(255) DEFAULT NULL,
  `product_id` varchar(255) NOT NULL,
  `model` varchar(255) DEFAULT NULL,
  `category` int DEFAULT '-1'
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `device`
--

LOCK TABLES `device` WRITE;
/*!40000 ALTER TABLE `device` DISABLE KEYS */;
INSERT INTO `device` VALUES ('Nuance Power MIC III','0554','Designed to enhance productivity and provide ergonomic control of both standard dictation and speech recognition functions.','mic.jpg','1001',NULL,4),('Samsung USB Device','090C','Compatible USB storage device','090C-1000.jpg','1000',NULL,0),('Chipsbrand USB disk','1E3D','The USB disk device ',NULL,'2096',NULL,0),('Nuance PowerMic II','0554',NULL,NULL,'1001','PowerMic II',4),('Nuance PowerMic III','0554',NULL,NULL,'1001','PowerMic III',4),('Philips SpeechMike 3200','0911',NULL,NULL,'0c1c','3200',4),('Philips SpeechMike 3500','0911',NULL,NULL,'0c1c','3500',4),('Wacom STU-520A','056a',NULL,NULL,'00a3','STU-520A',-1),('Brother Label Printer QL-720NW','04f9','Professional, high-speed label printer with built-in the ethernet and wireless networking','Brother-QL.png','2044','QL-720NW',1),('HP Laserjet P2055','03f0',NULL,NULL,'5c17','P2055',1),('Epson scanner DS-570W','04b8',NULL,NULL,'0157','DS-570W',2),('Fijitsu scanner fi-7160 ','04c5 ',NULL,NULL,'132e ','fi-7160 ',2);
/*!40000 ALTER TABLE `device` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `driver`
--

DROP TABLE IF EXISTS `driver`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `driver` (
  `os_name` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `product_id` varchar(255) DEFAULT NULL,
  `vendor_id` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  `driver` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=50 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `driver`
--

LOCK TABLES `driver` WRITE;
/*!40000 ALTER TABLE `driver` DISABLE KEYS */;
INSERT INTO `driver` VALUES ('Windows',0,'2044','04F9',NULL,'1.2.1'),('Windows',3,'2044','04F9',NULL,'1.2.5'),('Windows 2016',4,'1212','1212',NULL,'driver'),('Windows 2019',5,'1212','1212',NULL,'driver'),('Windows 10',6,'1212','1212',NULL,'driver'),('Windows 7',7,'1212','1212',NULL,'driver'),('Windows 10',8,'4509','3084','0','ddd'),('Windows 2016',9,'4509','3084','0','ddd'),('Windows 7',10,'1001','0554','PowerMic II',''),('Windows 10',11,'1001','0554','PowerMic II',''),('Windows 2016',12,'1001','0554','PowerMic II',''),('Windows 2019',13,'1001','0554','PowerMic II',''),('Windows 10',14,'1001','0554','PowerMic III',''),('Windows 7',15,'1001','0554','PowerMic III',''),('Windows 2016',16,'1001','0554','PowerMic III',''),('Windows 2019',17,'1001','0554','PowerMic III',''),('Windows 7',18,'0c1c','0911','3200',''),('Windows 10',19,'0c1c','0911','3200',''),('Windows 2016',20,'0c1c','0911','3200',''),('Windows 2019',21,'0c1c','0911','3200',''),('Windows 7',22,'0c1c','0911','3500',''),('Windows 10',23,'0c1c','0911','3500',''),('Windows 2016',24,'0c1c','0911','3500',''),('Windows 2019',25,'0c1c','0911','3500',''),('Windows 7',26,'00a3','056a','STU-520A',''),('Windows 10',27,'00a3','056a','STU-520A',''),('Windows 2016',28,'00a3','056a','STU-520A',''),('Windows 2019',29,'00a3','056a','STU-520A',''),('Windows 7',30,'2044','04f9','QL-720NW',''),('Windows 10',31,'2044','04f9','QL-720NW',''),('Windows 2016',32,'2044','04f9','QL-720NW',''),('Windows 2019',33,'2044','04f9','QL-720NW',''),('Windows 7',34,'5c17','03f0','P2055',''),('Windows 10',35,'5c17','03f0','P2055',''),('Windows 2016',36,'5c17','03f0','P2055',''),('Windows 2019',37,'5c17','03f0','P2055',''),('Windows 7',38,'0157','04b8','DS-570W',''),('Windows 10',39,'0157','04b8','DS-570W',''),('Windows 2016',40,'0157','04b8','DS-570W',''),('Windows 2019',41,'0157','04b8','DS-570W',''),('Windows 7',42,'132e','04c5','fi-7160',''),('Windows 10',43,'132e','04c5','fi-7160',''),('Windows 2016',44,'132e','04c5','fi-7160',''),('Windows 2019',45,'132e','04c5','fi-7160',''),('Windows 7',46,'1000','090c',NULL,''),('Windows 10',47,'1000','090c',NULL,''),('Windows 2016',48,'1000','090c',NULL,''),('Windows 2019',49,'1000','090c',NULL,'');
/*!40000 ALTER TABLE `driver` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `matrix`
--

DROP TABLE IF EXISTS `matrix`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `matrix` (
  `Horizon_client_version` varchar(255) DEFAULT NULL,
  `Horizon_agent_version` varchar(255) DEFAULT NULL,
  `id` int NOT NULL AUTO_INCREMENT,
  `vendor_id` varchar(255) DEFAULT NULL,
  `product_id` varchar(255) DEFAULT NULL,
  `model` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=32 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `matrix`
--

LOCK TABLES `matrix` WRITE;
/*!40000 ALTER TABLE `matrix` DISABLE KEYS */;
INSERT INTO `matrix` VALUES ('5.4.0','7.12.0',16,'0554','1001','PowerMic II'),('5.4.0','7.12.0',17,'0554','1001','PowerMic III'),('5.4.0','7.12.0',18,'0911','0c1c','3200'),('5.4.0','7.12.0',19,'0911','0c1c','3500'),('5.4.0','7.12.0',20,'056a','00a3','STU-520A'),('5.4.0','7.12.0',21,'04f9','2044','QL-720NW'),('5.4.0','7.12.0',22,'03f0','5c17','P2055'),('5.4.0','7.12.0',23,'04b8','0157','DS-570W'),('5.4.0','7.12.0',27,'090c','1000',NULL),('5.4.0','7.12.0',31,'04c5 ','132e ','fi-7160 ');
/*!40000 ALTER TABLE `matrix` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `vendor`
--

DROP TABLE IF EXISTS `vendor`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vendor` (
  `vendor_id` varchar(255) NOT NULL,
  `vendor_name` varchar(255) DEFAULT NULL,
  `vendor_logo` varchar(255) DEFAULT NULL,
  `vendor_link` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`vendor_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vendor`
--

LOCK TABLES `vendor` WRITE;
/*!40000 ALTER TABLE `vendor` DISABLE KEYS */;
INSERT INTO `vendor` VALUES ('04F9','Brother','brother.png','https://www.brother-usa.com/home/'),('0554','Nuance','nuance.jpg','https://www.nuance.com'),('090C','Samsung','samsung.png','https://www.samsung.com/us'),('1E3D','Chipsbrand',NULL,NULL);
/*!40000 ALTER TABLE `vendor` ENABLE KEYS */;
UNLOCK TABLES;

/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `user` (
  `username` varchar(20) NOT NULL,
  `password` varchar(255) DEFAULT NULL,
  `role` varchar(20) DEFAULT NULL,
  PRIMARY KEY (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-06-30  1:14:03
