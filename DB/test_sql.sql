/*
Navicat MySQL Data Transfer

Source Server         : 192.168.1.251
Source Server Version : 100217
Source Host           : 192.168.1.251:23306
Source Database       : test

Target Server Type    : MYSQL
Target Server Version : 100217
File Encoding         : 65001

Date: 2018-12-03 12:40:02
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for access_log
-- ----------------------------
DROP TABLE IF EXISTS `access_log`;
CREATE TABLE `access_log` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `type` int(11) NOT NULL,
  `method` varchar(10) NOT NULL,
  `url` varchar(255) NOT NULL,
  `parameters` text DEFAULT NULL,
  `response_code` varchar(10) DEFAULT NULL,
  `result` text DEFAULT NULL,
  `time_consuming` int(11) DEFAULT NULL,
  `create_datetime` timestamp NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=19007 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for cache_image_id_score
-- ----------------------------
DROP TABLE IF EXISTS `cache_image_id_score`;
CREATE TABLE `cache_image_id_score` (
  `image_id` varchar(64) NOT NULL,
  `idcard` varchar(20) NOT NULL,
  `score` float NOT NULL,
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `image_path` varchar(512) DEFAULT NULL,
  `create_datetime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  KEY `image` (`image_id`) USING BTREE,
  KEY `idcard` (`idcard`)
) ENGINE=InnoDB AUTO_INCREMENT=55464 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for django_migrations
-- ----------------------------
DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for exception_log
-- ----------------------------
DROP TABLE IF EXISTS `exception_log`;
CREATE TABLE `exception_log` (
  `id` bigint(20) NOT NULL AUTO_INCREMENT,
  `module` varchar(250) CHARACTER SET utf8 COLLATE utf8_bin NOT NULL,
  `service` varchar(250) DEFAULT NULL,
  `parameter` text DEFAULT NULL,
  `content` text NOT NULL,
  `create_datetime` datetime DEFAULT current_timestamp(),
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6273 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for id_info
-- ----------------------------
DROP TABLE IF EXISTS `id_info`;
CREATE TABLE `id_info` (
  `idcard` varchar(30) NOT NULL,
  `nation` varchar(45) DEFAULT NULL,
  `name` varchar(255) DEFAULT NULL,
  `sex` varchar(20) DEFAULT NULL,
  `memo` text DEFAULT NULL,
  `avatar` text DEFAULT NULL,
  `create_datetime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  `image_path` text DEFAULT NULL,
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tracking_type` char(255) DEFAULT '',
  PRIMARY KEY (`id`),
  UNIQUE KEY `idcard_UNIQUE` (`idcard`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=54051 DEFAULT CHARSET=utf8 COMMENT='已知 身份信息库、\r\n图片与id 100对应的';

-- ----------------------------
-- Table structure for image_id_score
-- ----------------------------
DROP TABLE IF EXISTS `image_id_score`;
CREATE TABLE `image_id_score` (
  `image_id` varchar(64) NOT NULL,
  `idcard` varchar(20) NOT NULL,
  `score` float NOT NULL,
  `id` int(11) unsigned NOT NULL AUTO_INCREMENT,
  `image_path` text DEFAULT NULL,
  `create_datetime` timestamp NOT NULL DEFAULT current_timestamp() ON UPDATE current_timestamp(),
  PRIMARY KEY (`id`),
  UNIQUE KEY `image_id` (`image_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=54681 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Table structure for yt_id_uri
-- ----------------------------
DROP TABLE IF EXISTS `yt_id_uri`;
CREATE TABLE `yt_id_uri` (
  `image_id` char(32) DEFAULT '',
  `uri` varchar(255) DEFAULT NULL,
  UNIQUE KEY `image_id` (`image_id`) USING HASH
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
