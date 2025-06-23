-- MySQL dump 10.13  Distrib 8.0.38, for Win64 (x86_64)
--
-- Host: localhost    Database: internship_management
-- ------------------------------------------------------
-- Server version	8.0.38

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
-- Table structure for table `interns`
--

DROP TABLE IF EXISTS `interns`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `interns` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `phone_no` varchar(15) DEFAULT NULL,
  `gender` enum('Male','Female') DEFAULT NULL,
  `institution` varchar(255) DEFAULT NULL,
  `years_of_experience` int DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `phone_no` (`phone_no`)
) ENGINE=InnoDB AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `intern`
--

LOCK TABLES `interns` WRITE;
/*!40000 ALTER TABLE `intern` DISABLE KEYS */;
INSERT INTO `interns` (`id`, `name`, `email`, `phone_no`, `gender`, `institution`, `years_of_experience`) VALUES (1, 'Alice Johnson', 'alice.johnson@example.com', '1234567890', 'Female', 'Harvard University', 2),(2, 'Bob Smith', 'bob.smith@example.com', '2234567890', 'Male', 'MIT', 3),(3, 'Carol Davis', 'carol.davis@example.com', '3234567890', 'Female', 'Stanford University', 1),(4, 'David Brown', 'david.brown@example.com', '4234567890', 'Male', 'UC Berkeley', 4),(5, 'Eva Taylor', 'eva.taylor@example.com', '5234567890', 'Female', 'Oxford University', 2),(6, 'Frank Wilson', 'frank.wilson@example.com', '6234567890', 'Male', 'Cambridge University', 5),(7, 'Grace Lee', 'grace.lee@example.com', '7234567890', 'Female', 'University of Chicago', 3),(8, 'Henry Walker', 'henry.walker@example.com', '8234567890', 'Male', 'Columbia University', 2),(9, 'Isabella White', 'isabella.white@example.com', '9234567890', 'Female', 'Yale University', 1),(10, 'Jack Thompson', 'jack.thompson@example.com', '1234567801', 'Male', 'Princeton University', 4),(11, 'Katherine Martinez', 'katherine.martinez@example.com', '2234567801', 'Female', 'University of Tokyo', 3),(12, 'Liam Anderson', 'liam.anderson@example.com', '3234567801', 'Male', 'Caltech', 2),(13, 'Mia Thomas', 'mia.thomas@example.com', '4234567801', 'Female', 'University of Melbourne', 1),(14, 'Noah Scott', 'noah.scott@example.com', '5234567801', 'Male', 'ETH Zurich', 5),(15, 'Olivia Lewis', 'olivia.lewis@example.com', '6234567801', 'Female', 'Imperial College London', 4),(16, 'Peter Hall', 'peter.hall@example.com', '7234567801', 'Male', 'University of Toronto', 2),(17, 'Quinn Young', 'quinn.young@example.com', '8234567801', 'Female', 'Peking University', 3),(18, 'Ryan King', 'ryan.king@example.com', '9234567801', 'Male', 'National University of Singapore', 1),(19, 'Sophia Adams', 'sophia.adams@example.com', '1234567812', 'Female', 'University of Sydney', 4),(20, 'Thomas Reed', 'thomas.reed@example.com', '2234567812', 'Male', 'University of Hong Kong', 2),(21, 'Uma Patel', 'uma.patel@example.com', '3234567812', 'Female', 'Indian Institute of Technology', 3),(22, 'Victor Green', 'victor.green@example.com', '4234567812', 'Male', 'University of Oxford', 1),(23, 'Wendy Baker', 'wendy.baker@example.com', '5234567812', 'Female', 'University of Cambridge', 5),(24, 'Xavier Bell', 'xavier.bell@example.com', '6234567812', 'Male', 'Massachusetts Institute of Technology', 4),(25, 'Yvonne Collins', 'yvonne.collins@example.com', '7234567812', 'Female', 'Stanford University', 2),(26, 'Zachary Evans', 'zachary.evans@example.com', '8234567812', 'Male', 'University of California, Berkeley', 3),(27, 'Avery Hughes', 'avery.hughes@example.com', '9234567812', 'Female', 'Yale University', 1),(28, 'Blake Carter', 'blake.carter@example.com', '1234567823', 'Male', 'Princeton University', 4),(29, 'Chloe Stewart', 'chloe.stewart@example.com', '2234567823', 'Female', 'Columbia University', 2),(30, 'Dylan Perry', 'dylan.perry@example.com', '3234567823', 'Male', 'University of Chicago', 3);
/*!40000 ALTER TABLE `intern` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2024-07-23 23:31:25
