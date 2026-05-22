-- MySQL dump 10.13  Distrib 8.0.45, for Win64 (x86_64)
--
-- Host: localhost    Database: pathpilot_db
-- ------------------------------------------------------
-- Server version	8.0.45

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `careers`
--

DROP TABLE IF EXISTS `careers`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `careers` (
  `id` int NOT NULL AUTO_INCREMENT,
  `career_name` varchar(150) NOT NULL,
  `stream_id` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `stream_id` (`stream_id`),
  CONSTRAINT `careers_ibfk_1` FOREIGN KEY (`stream_id`) REFERENCES `streams` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `careers`
--

LOCK TABLES `careers` WRITE;
/*!40000 ALTER TABLE `careers` DISABLE KEYS */;
INSERT INTO `careers` VALUES (1,'Engineering - CS',1),(2,'Engineering - EC',1),(3,'Engineering - Mechanical',1),(4,'Medicine',1),(5,'Research',1),(6,'Management',2),(7,'Finance',2),(8,'Law',2),(9,'Design',3),(10,'Media',3),(11,'Law',3);
/*!40000 ALTER TABLE `careers` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `questions`
--

DROP TABLE IF EXISTS `questions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `questions` (
  `id` int NOT NULL AUTO_INCREMENT,
  `question_text` text NOT NULL,
  `career_id` int DEFAULT NULL,
  `weight` int DEFAULT '1',
  PRIMARY KEY (`id`),
  KEY `career_id` (`career_id`),
  CONSTRAINT `questions_ibfk_1` FOREIGN KEY (`career_id`) REFERENCES `careers` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=124 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `questions`
--

LOCK TABLES `questions` WRITE;
/*!40000 ALTER TABLE `questions` DISABLE KEYS */;
INSERT INTO `questions` VALUES (1,'Do you enjoy programming?',1,2),(2,'Do you like problem solving?',1,3),(3,'Are you interested in electronics and circuits?',2,2),(4,'Do you like hands-on experiments?',2,3),(5,'Are you interested in biology?',4,3),(6,'Do you like helping people?',4,2),(7,'Do you enjoy organizing tasks?',6,2),(8,'Are you good at leadership?',6,3),(17,'Do you enjoy logical puzzles and algorithms?',1,2),(18,'Are you interested in developing software applications?',1,2),(19,'Do you like working with data structures?',1,2),(20,'Are you comfortable learning new programming languages?',1,1),(21,'Do you enjoy debugging and problem-solving in code?',1,3),(22,'Are you interested in AI, Machine Learning, or Data Science?',1,2),(23,'Do you like working on team projects in software development?',1,1),(24,'Are you interested in understanding how electronic devices work internally?',2,2),(25,'Do you enjoy working with circuits and components like resistors and capacitors?',2,3),(26,'Are you comfortable solving numerical problems related to physics?',2,2),(27,'Do you like learning about communication systems such as mobile networks?',2,2),(28,'Are you interested in signal processing and transmission?',2,2),(29,'Do you enjoy working with microcontrollers and embedded systems?',2,3),(30,'Are you curious about how WiFi, Bluetooth, and satellites function?',2,2),(31,'Do you like debugging hardware issues?',2,3),(32,'Are you interested in robotics and automation systems?',2,2),(33,'Do you enjoy laboratory experiments involving electronic equipment?',2,1),(34,'Are you interested in understanding how machines and engines work?',3,3),(35,'Do you enjoy studying mechanics and motion of objects?',3,3),(36,'Are you comfortable solving physics-based numerical problems?',3,2),(37,'Do you like working with tools and mechanical equipment?',3,2),(38,'Are you interested in automobile design and manufacturing?',3,3),(39,'Do you enjoy learning about thermodynamics and heat transfer?',3,2),(40,'Are you curious about robotics and mechanical automation systems?',3,2),(41,'Do you like designing mechanical parts using software like CAD?',3,2),(42,'Are you interested in production and industrial processes?',3,2),(43,'Do you enjoy practical workshop and lab sessions?',3,1),(44,'Are you deeply interested in human biology and anatomy?',4,3),(45,'Do you enjoy studying how the human body functions?',4,3),(46,'Are you comfortable handling blood, injuries, or medical emergencies?',4,3),(47,'Do you like helping people recover from illness?',4,2),(48,'Are you patient and calm under stressful situations?',4,2),(49,'Are you willing to study for many years to become a specialist?',4,2),(50,'Do you enjoy diagnosing problems and finding solutions?',4,2),(51,'Are you interested in medical research and new treatments?',4,2),(52,'Do you have strong empathy towards sick or injured individuals?',4,3),(53,'Are you comfortable working long hours in hospitals or clinics?',4,1),(54,'Are you curious about discovering new knowledge or theories?',5,3),(55,'Do you enjoy conducting experiments or investigations?',5,3),(56,'Are you comfortable analyzing data and drawing conclusions?',5,3),(57,'Do you like reading research papers and academic articles?',5,2),(58,'Are you patient enough to work on long-term projects?',5,2),(59,'Do you enjoy solving complex and unsolved problems?',5,3),(60,'Are you interested in innovation and scientific advancements?',5,2),(61,'Do you prefer deep analysis over quick results?',5,2),(62,'Are you comfortable working independently for long hours?',5,2),(63,'Do you enjoy forming hypotheses and testing them systematically?',5,3),(64,'Do you enjoy leading a team towards a common goal?',6,3),(65,'Are you confident in making important decisions under pressure?',6,3),(66,'Do you like planning and organizing tasks effectively?',6,3),(67,'Are you comfortable communicating with different types of people?',6,2),(68,'Do you enjoy resolving conflicts between team members?',6,2),(69,'Are you interested in business strategies and growth planning?',6,2),(70,'Do you take responsibility for outcomes of group work?',6,2),(71,'Are you good at time management?',6,2),(72,'Do you enjoy motivating others to perform better?',6,3),(73,'Are you comfortable presenting ideas to a group?',6,2),(74,'Do you enjoy working with numbers and calculations?',7,3),(75,'Are you interested in understanding how financial markets operate?',7,3),(76,'Do you like analyzing profits, losses, and investment risks?',7,3),(77,'Are you comfortable interpreting financial statements and reports?',7,2),(78,'Do you enjoy budgeting and managing expenses effectively?',7,2),(79,'Are you interested in stock markets and investment strategies?',7,2),(80,'Do you pay close attention to financial details?',7,2),(81,'Are you comfortable making data-driven financial decisions?',7,3),(82,'Do you enjoy studying economic trends and their impact?',7,2),(83,'Are you interested in banking and financial services?',7,1),(84,'Are you interested in understanding legal systems and court procedures?',8,3),(85,'Do you enjoy debating and presenting arguments logically?',8,3),(86,'Are you confident speaking in front of others?',8,2),(87,'Do you like analyzing situations from multiple perspectives?',8,3),(88,'Are you interested in protecting the rights of individuals or organizations?',8,2),(89,'Do you enjoy reading and interpreting complex documents?',8,2),(90,'Are you patient enough to handle lengthy legal processes?',8,2),(91,'Do you have strong critical thinking skills?',8,3),(92,'Are you interested in corporate or business law?',8,2),(93,'Do you stay updated with current legal or political issues?',8,1),(94,'Do you enjoy creating visual concepts and artwork?',9,3),(95,'Are you interested in graphic or UI/UX design?',9,2),(96,'Do you pay attention to colors, layouts, and aesthetics?',9,3),(97,'Do you enjoy sketching or digital illustration?',9,2),(98,'Are you interested in product or fashion design?',9,2),(99,'Do you like experimenting with creative ideas?',9,3),(100,'Are you comfortable using design software tools?',9,2),(101,'Do you enjoy transforming ideas into visual formats?',9,3),(102,'Are you detail-oriented when working on creative projects?',9,2),(103,'Do you prefer creative tasks over analytical ones?',9,1),(104,'Do you enjoy creating content such as videos, blogs, or podcasts?',10,3),(105,'Are you confident speaking in front of a camera or audience?',10,3),(106,'Do you stay updated with current events and trending topics?',10,2),(107,'Are you interested in journalism or news reporting?',10,2),(108,'Do you enjoy storytelling and creative writing?',10,3),(109,'Are you comfortable working under tight deadlines?',10,2),(110,'Do you like engaging with people through social media platforms?',10,2),(111,'Are you interested in film, television, or digital media production?',10,2),(112,'Do you have strong communication and presentation skills?',10,3),(113,'Do you enjoy researching topics before creating content?',10,2),(114,'Are you interested in social justice and human rights issues?',11,3),(115,'Do you feel strongly about fairness and equality in society?',11,3),(116,'Do you enjoy discussing political and constitutional matters?',11,2),(117,'Are you interested in public policy and governance?',11,2),(118,'Do you like analyzing social issues from a legal perspective?',11,3),(119,'Are you confident in expressing your opinions during debates?',11,2),(120,'Do you stay informed about national and international legal developments?',11,2),(121,'Are you interested in working for NGOs or public service organizations?',11,2),(122,'Do you enjoy reading about historical legal cases and judgments?',11,1),(123,'Are you motivated to bring positive change through law?',11,3);
/*!40000 ALTER TABLE `questions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `results`
--

DROP TABLE IF EXISTS `results`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `results` (
  `id` int NOT NULL AUTO_INCREMENT,
  `user_id` int DEFAULT NULL,
  `career_id` int DEFAULT NULL,
  `score` int DEFAULT NULL,
  `percentage` decimal(5,2) DEFAULT NULL,
  `suitability` varchar(10) DEFAULT NULL,
  `taken_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  KEY `user_id` (`user_id`),
  KEY `career_id` (`career_id`),
  CONSTRAINT `results_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON DELETE CASCADE,
  CONSTRAINT `results_ibfk_2` FOREIGN KEY (`career_id`) REFERENCES `careers` (`id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=18 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `results`
--

LOCK TABLES `results` WRITE;
/*!40000 ALTER TABLE `results` DISABLE KEYS */;
INSERT INTO `results` VALUES (15,7,6,17,58.62,'Medium','2026-03-01 18:03:03'),(16,8,7,16,69.57,'Medium','2026-03-02 04:43:04'),(17,8,1,5,27.78,'Low','2026-03-02 04:48:40');
/*!40000 ALTER TABLE `results` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `streams`
--

DROP TABLE IF EXISTS `streams`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `streams` (
  `id` int NOT NULL AUTO_INCREMENT,
  `stream_name` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `streams`
--

LOCK TABLES `streams` WRITE;
/*!40000 ALTER TABLE `streams` DISABLE KEYS */;
INSERT INTO `streams` VALUES (1,'Science'),(2,'Commerce'),(3,'Arts');
/*!40000 ALTER TABLE `streams` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `users`
--

DROP TABLE IF EXISTS `users`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `email` varchar(150) NOT NULL,
  `password` varchar(255) NOT NULL,
  `created_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `users`
--

LOCK TABLES `users` WRITE;
/*!40000 ALTER TABLE `users` DISABLE KEYS */;
INSERT INTO `users` VALUES (6,'Alex','alex@gmail.com','scrypt:32768:8:1$XZB3jGW8laGIc5LS$9af652020dab12f139dcca0e618d99184517e34cfade0bdbc149aee8c3ddf88ea736752b480833edef64caf27ecdd0d54a840723b0160f95d47fa220545b5985','2026-03-01 17:37:12'),(7,'Ann George ','anngeorge@gmail.com','scrypt:32768:8:1$FpCjWy8gfbP5oDOc$6d9b2d357fb9784d45b18c55020a329b9654ab9fcb084628571d746f6a40484c1a40dbffc53b0d4cfc4c034a74eeb007622303805464dcbd09158f857dccb728','2026-03-01 18:02:18'),(8,'Eric Joan','ericjoan@gmail.com','scrypt:32768:8:1$xqrmR2FyYmsGliDA$6ef7a206ec247563aff1750ce19dd4e0ad31e2eb697e996d4fcd92f52b548588c33c1d18e45ee46aaf14f08064577130b464103c5fc593ba9c583b36966c81d3','2026-03-01 18:04:10');
/*!40000 ALTER TABLE `users` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2026-03-06  5:59:21
