/*
 Navicat Premium Data Transfer

 Source Server         : localhost
 Source Server Type    : MySQL
 Source Server Version : 50728
 Source Host           : localhost:3306
 Source Schema         : vote

 Target Server Type    : MySQL
 Target Server Version : 50728
 File Encoding         : 65001

 Date: 14/03/2021 21:11:25
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for zsc_node
-- ----------------------------
DROP TABLE IF EXISTS `zsc_node`;
CREATE TABLE `zsc_node` (
  `node_id` int(11) NOT NULL AUTO_INCREMENT COMMENT '节点ID',
  `node_name` varchar(20) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '节点名称',
  `node_address` varchar(500) COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '节点钱包地址',
  `node_logo` varchar(500) COLLATE utf8mb4_unicode_ci DEFAULT NULL COMMENT '节点Logo',
  `node_amount` text COLLATE utf8mb4_unicode_ci NOT NULL COMMENT '节点票数',
  `node_result` int(4) DEFAULT NULL COMMENT '结果 1=在线 0=离线',
  `create_at` timestamp NULL DEFAULT CURRENT_TIMESTAMP COMMENT '创建时间',
  PRIMARY KEY (`node_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Records of zsc_node
-- ----------------------------
BEGIN;
INSERT INTO `zsc_node` VALUES (6, '火币', '0x7b68d5fe63b6e1afbe7386cb129b4ee11c7367e7', NULL, '88119650315426526207081', 1, NULL);
INSERT INTO `zsc_node` VALUES (7, '火币2', '0x884e01ac2ca8816c86d1f167524ab192898cdcb1', NULL, '139717754512480898677720', 1, NULL);
INSERT INTO `zsc_node` VALUES (8, '火币3', '0xaca71dbe4ed4fe773fce11e691dd522bbad259e1', NULL, '199664009026910054688525', 1, NULL);
INSERT INTO `zsc_node` VALUES (9, '火币4', '0xc4dd76a86e6f59ac9b461a3c3566646a316d5787', NULL, '208639031524008737567359', 1, NULL);
COMMIT;

-- ----------------------------
-- Table structure for zsc_node_vote
-- ----------------------------
DROP TABLE IF EXISTS `zsc_node_vote`;
CREATE TABLE `zsc_node_vote` (
  `nv_id` int(11) NOT NULL AUTO_INCREMENT,
  `node_id` int(11) DEFAULT NULL,
  `node_address` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `vote_address` varchar(100) COLLATE utf8mb4_unicode_ci DEFAULT NULL,
  `vote_amount` text COLLATE utf8mb4_unicode_ci,
  PRIMARY KEY (`nv_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci;

-- ----------------------------
-- Records of zsc_node_vote
-- ----------------------------
BEGIN;
INSERT INTO `zsc_node_vote` VALUES (3, 6, '0x7b68d5fe63b6e1afbe7386cb129b4ee11c7367e7', '0x7b68d5fe63b6e1afbe7386cb129b4ee11c7367e7', '88119650315426526207081');
INSERT INTO `zsc_node_vote` VALUES (4, 7, '0x884e01ac2ca8816c86d1f167524ab192898cdcb1', '0x884e01ac2ca8816c86d1f167524ab192898cdcb1', '139717754512480898677720');
INSERT INTO `zsc_node_vote` VALUES (5, 8, '0xaca71dbe4ed4fe773fce11e691dd522bbad259e1', '0xaca71dbe4ed4fe773fce11e691dd522bbad259e1', '199664009026910054688525');
INSERT INTO `zsc_node_vote` VALUES (6, 9, '0xc4dd76a86e6f59ac9b461a3c3566646a316d5787', '0xc4dd76a86e6f59ac9b461a3c3566646a316d5787', '208639031524008737567359');
COMMIT;

SET FOREIGN_KEY_CHECKS = 1;
