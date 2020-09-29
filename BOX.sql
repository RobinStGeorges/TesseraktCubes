-- phpMyAdmin SQL Dump
-- version 4.6.6deb5
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jun 06, 2020 at 01:08 AM
-- Server version: 10.3.22-MariaDB-0+deb10u1
-- PHP Version: 7.3.14-1~deb10u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `tesseraktbdd`
--

-- --------------------------------------------------------

--
-- Table structure for table `box_list`
--

CREATE TABLE `box_list` (
  `id` int(11) NOT NULL,
  `id_box` int(11) NOT NULL,
  `date_last_connection` datetime NOT NULL,
  `is_connected` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `box_list`
--

INSERT INTO `box_list` (`id`, `id_box`, `date_last_connection`, `is_connected`) VALUES
(1, 0, '2020-06-04 00:00:00', 1);

-- --------------------------------------------------------

--
-- Table structure for table `matrice`
--

CREATE TABLE `matrice` (
  `id` int(11) NOT NULL,
  `id_box` int(11) NOT NULL,
  `coord_x` int(11) NOT NULL,
  `coord_y` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `matrice`
--

INSERT INTO `matrice` (`id`, `id_box`, `coord_x`, `coord_y`) VALUES
(15, 1, 0, 0),
(20, 2, 0, 1);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `box_list`
--
ALTER TABLE `box_list`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `matrice`
--
ALTER TABLE `matrice`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `box_list`
--
ALTER TABLE `box_list`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT for table `matrice`
--
ALTER TABLE `matrice`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
