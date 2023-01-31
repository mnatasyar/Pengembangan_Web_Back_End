-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1:3307
-- Generation Time: Jan 31, 2023 at 12:53 PM
-- Server version: 10.4.27-MariaDB
-- PHP Version: 8.1.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `db_genshin`
--

-- --------------------------------------------------------

--
-- Table structure for table `genshins`
--

CREATE TABLE `genshins` (
  `id` int(11) NOT NULL,
  `icon` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `name` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `weapontype` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `base` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `substat` varchar(255) CHARACTER SET latin1 COLLATE latin1_swedish_ci DEFAULT NULL,
  `createdAt` datetime NOT NULL,
  `updatedAt` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Dumping data for table `genshins`
--

INSERT INTO `genshins` (`id`, `icon`, `name`, `weapontype`, `base`, `substat`, `createdAt`, `updatedAt`) VALUES
(3, 'https://genshin.honeyhunterworld.com/img/i_n11509.webp', 'Mistsplitter Reforged', 'Sword', '+48 (+674)', 'Crit DMG +9.6% (+44.1%)', '2023-01-29 13:19:39', '2023-01-29 13:34:52'),
(4, 'https://genshin.honeyhunterworld.com/img/i_n12510.webp', 'Redhorn Stonethresher', 'Claymores', '+44 (+542)', 'Crit DMG +19.2% (+88.2%)', '2023-01-31 09:25:08', '2023-01-31 09:25:08'),
(5, 'https://genshin.honeyhunterworld.com/img/i_n15509.webp', 'Thundering Pulse', 'Bow', '+46 (+608)', 'Crit DMG +14.4%(+66.2%)', '2023-01-31 09:26:45', '2023-01-31 09:26:45');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `genshins`
--
ALTER TABLE `genshins`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `genshins`
--
ALTER TABLE `genshins`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
