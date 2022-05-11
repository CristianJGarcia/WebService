-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2.1
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: May 03, 2020 at 04:25 PM
-- Server version: 5.7.26-0ubuntu0.16.04.1
-- PHP Version: 7.0.33-0ubuntu0.16.04.4

SET SQL_MODE
= "NO_AUTO_VALUE_ON_ZERO";
SET time_zone
= "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `hqc265`
--

-- --------------------------------------------------------

--
-- Table structure for table `Properties`
--

CREATE TABLE `Properties`
(
  `id` int
(1) NOT NULL,
  `address` text NOT NULL,
  `city` text NOT NULL,
  `state` char
(2) NOT NULL,
  `zip` text NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `Properties`
--

INSERT INTO `Properties` (`
id`,
`address
`, `city`, `state`, `zip`) VALUES
(6, '15801 chase hill blvd', 'San antonio', 'TX', '78256'),
(7, '456 Example St.', 'Fort Sill', 'OK', '83230'),
(8, '321 Example St.', 'Sesame', 'TX', '81234'),
(10, '143 Martini Dr.', 'AAFS', 'OK', '83230'),
(11, '176 Martini Dr.', 'AAFS', 'OK', '87432'),
(12, '605 Martini Dr.', 'AAFS', 'OK', '87432'),
(13, '705 Martini Dr.', 'AAFS', 'OK', '87432'),
(15, 'Swagger Test Dr.', 'Stressed City', 'NO', '83230'),
(83, 'testing', 'test', 'CA', 'test'),
(84, 'testing', 'test', 'CA', 'test'),
(92, 'testing', 'test', 'CA', 'test');

--
-- Indexes for dumped tables
--

--
-- Indexes for table `Properties`
--
ALTER TABLE `Properties`
ADD PRIMARY KEY
(`id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `Properties`
--
ALTER TABLE `Properties`
  MODIFY `id` int
(1) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=119;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
