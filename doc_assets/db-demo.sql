CREATE TABLE `device` (
  `device_id` int PRIMARY KEY AUTO_INCREMENT,
  `device_name` varchar(255),
  `device_verion` varchar(255),
  `vendor_id` int,
  `description` varchar(255),
  `picture` varchar(255)
);

CREATE TABLE `vendor` (
  `vendor_id` int PRIMARY KEY AUTO_INCREMENT,
  `vendor_name` varchar(255),
  `vendor_logo` varchar(255),
  `vendor_link` varchar(255)
);

CREATE TABLE `matrix` (
  `device_id` int PRIMARY KEY,
  `client_id` int,
  `agent_id` int
);

CREATE TABLE `client` (
  `client_id` int PRIMARY KEY,
  `client_os` varchar(255),
  `client_version` varchar(255)
);

CREATE TABLE `agent` (
  `agent_id` int PRIMARY KEY,
  `agent_os` varchar(255),
  `agenbt_version` varchar(255)
);

ALTER TABLE `device` ADD FOREIGN KEY (`vendor_id`) REFERENCES `vendor` (`vendor_id`);

ALTER TABLE `device` ADD FOREIGN KEY (`device_id`) REFERENCES `matrix` (`device_id`);

ALTER TABLE `matrix` ADD FOREIGN KEY (`client_id`) REFERENCES `client` (`client_id`);

ALTER TABLE `matrix` ADD FOREIGN KEY (`agent_id`) REFERENCES `agent` (`agent_id`);
