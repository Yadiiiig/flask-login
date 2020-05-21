-- --------------------------------------------------------
-- Host:                         127.0.0.1
-- Server versie:                10.4.10-MariaDB - mariadb.org binary distribution
-- Server OS:                    Win64
-- HeidiSQL Versie:              10.3.0.5771
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;


-- Databasestructuur van pentest wordt geschreven
CREATE DATABASE IF NOT EXISTS `pentest` /*!40100 DEFAULT CHARACTER SET utf8mb4 */;
USE `pentest`;

-- Structuur van  tabel pentest.failed_logins wordt geschreven
CREATE TABLE IF NOT EXISTS `failed_logins` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL,
  `tryip` varchar(50) NOT NULL,
  `amountTries` int(11) NOT NULL DEFAULT 0,
  `lockedTill` datetime DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4;

-- Dumpen data van tabel pentest.failed_logins: ~0 rows (ongeveer)
/*!40000 ALTER TABLE `failed_logins` DISABLE KEYS */;
/*!40000 ALTER TABLE `failed_logins` ENABLE KEYS */;

-- Structuur van  tabel pentest.logusers wordt geschreven
CREATE TABLE IF NOT EXISTS `logusers` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(50) NOT NULL DEFAULT '',
  `password` varchar(100) NOT NULL DEFAULT '',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- Dumpen data van tabel pentest.logusers: ~0 rows (ongeveer)
/*!40000 ALTER TABLE `logusers` DISABLE KEYS */;
INSERT INTO `logusers` (`id`, `username`, `password`) VALUES
	(16, 'test', '$5$rounds=535000$6F64zN71npR6IcOR$WOsARhYlirZwi8YlWfEBf0eHAg6lq4PhsTu4QNh9Ko9');
/*!40000 ALTER TABLE `logusers` ENABLE KEYS */;

/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IF(@OLD_FOREIGN_KEY_CHECKS IS NULL, 1, @OLD_FOREIGN_KEY_CHECKS) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
