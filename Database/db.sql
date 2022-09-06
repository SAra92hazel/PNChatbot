/*
SQLyog Community Edition- MySQL GUI v6.07
Host - 5.5.30 : Database - bargain
*********************************************************************
Server version : 5.5.30
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

create database if not exists `bargain`;

USE `bargain`;

/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;

/*Table structure for table `accuracy` */

DROP TABLE IF EXISTS `accuracy`;

CREATE TABLE `accuracy` (
  `NB` double DEFAULT NULL,
  `SVM` double DEFAULT NULL,
  `NN` double DEFAULT NULL,
  `RF` double DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `accuracy` */

insert  into `accuracy`(`NB`,`SVM`,`NN`,`RF`) values (0.38,0.638,0.553,0.337);

/*Table structure for table `items` */

DROP TABLE IF EXISTS `items`;

CREATE TABLE `items` (
  `menu1` varchar(100) DEFAULT NULL,
  `menu1id` int(11) DEFAULT NULL,
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `subject_` varchar(500) NOT NULL,
  `cost` varchar(100) DEFAULT NULL,
  `mcost` double DEFAULT NULL,
  `des` varchar(1000) DEFAULT NULL,
  `pic` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;

/*Data for the table `items` */

insert  into `items`(`menu1`,`menu1id`,`id`,`subject_`,`cost`,`mcost`,`des`,`pic`) values ('Latops',2,1,'Dell Inspiron 500','25000',20000,'dell thope laptop','mff1.jpg'),('Latops',2,2,'Dell Inspiron 500 2nd Gen','55000',48000,'Shop for new laptops, 2-in-1 PCs and gaming laptop computers from Dell India. Explore the high performance, versatile and powerful SSD laptops for home.\r\n&#8206;30,000 - &#8377;40,000 Laptops & 2... · &#8206;Inspiron · &#8206;Vostro Laptops · &#8206;XPS Laptops','mff1.jpg'),('Mobiles',3,3,'Apple Iphone 11pro ','88000',82000,'Apple Iphone 11pro  128GB, 8 GB.. ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC  ETC ','i9.jpg'),('Saree',1,4,'Dress','3000',2000,'new dress','pf7.jpg'),('Mobiles',3,5,'40000','34000',4000,'dsfsdfd','p3.png'),('Mobiles',3,6,'40000','34000',4000,'dsfsdfd','p3.png'),('Saree',1,7,'eer','34',45,'dfdf','bg3.jpg'),('Mobiles',3,8,'4','4',4,'asdasd','bg3.jpg');

/*Table structure for table `menu1` */

DROP TABLE IF EXISTS `menu1`;

CREATE TABLE `menu1` (
  `menu1` int(11) NOT NULL AUTO_INCREMENT,
  `subject_` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`menu1`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;

/*Data for the table `menu1` */

insert  into `menu1`(`menu1`,`subject_`) values (1,'Saree'),(2,'Latops'),(3,'Mobiles'),(4,'Earrings'),(5,'Watches'),(6,'Bangles');

/*Table structure for table `msgs` */

DROP TABLE IF EXISTS `msgs`;

CREATE TABLE `msgs` (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `msg` varchar(1000) DEFAULT NULL,
  `user_` varchar(100) DEFAULT NULL,
  `time_` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=818 DEFAULT CHARSET=latin1;

/*Data for the table `msgs` */

insert  into `msgs`(`sno`,`msg`,`user_`,`time_`) values (801,'Hello','chatbot','2022-04-26 20:53:00'),(802,'Dear sajid','chatbot','2022-04-26 20:53:00'),(803,'How can I help you..','chatbot','2022-04-26 20:53:00'),(804,'details cost know information product','sajid','2022-04-26 20:53:33'),(805,'Please Enter Product details like name..','chatbot','2022-04-26 20:53:33'),(806,'Dell Inspiron 500','sajid','2022-04-26 20:53:44'),(807,'bargain','sajid','2022-04-26 20:54:10'),(808,'Please Enter Product details like name for getting best deal..','chatbot','2022-04-26 20:54:10'),(809,'Dell Inspiron 500','sajid','2022-04-26 20:54:18'),(810,'Enter your bargain cost for Dell Inspiron 500, Cost:25000/- Rs.','chatbot','2022-04-26 20:54:28'),(811,'20000','sajid','2022-04-26 20:54:41'),(812,'bargain','sajid','2022-04-26 20:55:12'),(813,'Please Enter Product details like name for getting best deal..','chatbot','2022-04-26 20:55:12'),(814,'Dell Inspiron 500','sajid','2022-04-26 20:55:18'),(815,'Enter your bargain cost for Dell Inspiron 500, Cost:25000/- Rs.','chatbot','2022-04-26 20:55:22'),(816,'15000','sajid','2022-04-26 20:55:48'),(817,'Sorry we cannot accept your offering price of15000/-','chatbot','2022-04-26 20:55:48');

/*Table structure for table `purchase` */

DROP TABLE IF EXISTS `purchase`;

CREATE TABLE `purchase` (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `id` varchar(10) DEFAULT NULL,
  `sub` varchar(100) DEFAULT NULL,
  `cost` varchar(100) DEFAULT NULL,
  `freq` varchar(100) DEFAULT NULL,
  `tot_cost` varchar(100) DEFAULT NULL,
  `user` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=23 DEFAULT CHARSET=latin1;

/*Data for the table `purchase` */

insert  into `purchase`(`sno`,`id`,`sub`,`cost`,`freq`,`tot_cost`,`user`) values (8,'1','Dell Inspiron 500','25000','1','25000','sajid24x7@gmail.com'),(9,'1','Dell Inspiron 500','25000','1','25000','sajid24x7@gmail.com'),(10,'1','Dell Inspiron 500','25000','1','25000','sajidshai@hotmail.com'),(11,'2','Dell Inspiron 500 2nd Gen','48000.0','1','48000.0','sajidshai@hotmail.com'),(12,'2','Dell Inspiron 500 2nd Gen','48000.0','1','48000.0','sajidshai@hotmail.com'),(13,'1','Dell Inspiron 500','25000','1','25000','sajid@hotmail.com'),(14,'1','Dell Inspiron 500','25000','1','25000','sj@gmail.com'),(15,'3','Apple Iphone 11pro ','82000.0','1','82000.0','sj@gmail.com'),(16,'1','Dell Inspiron 500','25000','1','25000','a'),(17,'2','Dell Inspiron 500 2nd Gen','55000','2','110000','a'),(18,'3','Apple Iphone 11pro ','88000','2','176000','a'),(19,'1','Dell Inspiron 500','22000','1','22000','a'),(20,'1','Dell Inspiron 500','22500','1','22500','a'),(21,'3','Apple Iphone 11pro ','88000','2','176000','sajid'),(22,'1','Dell Inspiron 500','22500','1','22500','sajid');

/*Table structure for table `questions` */

DROP TABLE IF EXISTS `questions`;

CREATE TABLE `questions` (
  `sno` int(11) DEFAULT NULL,
  `keywords` varchar(500) DEFAULT NULL,
  `action` varchar(100) DEFAULT NULL,
  `reply` varchar(500) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `questions` */

insert  into `questions`(`sno`,`keywords`,`action`,`reply`) values (1,'details cost know information product','details','Please Enter Product details like name..'),(2,'negotiate bargain deal final cost price','bargain','Please Enter Product details like name for getting best deal..'),(3,'thank you','chatbot2','Your Welcome. Good Day..');

/*Table structure for table `reviews` */

DROP TABLE IF EXISTS `reviews`;

CREATE TABLE `reviews` (
  `sno` int(11) NOT NULL AUTO_INCREMENT,
  `prodid` varchar(100) DEFAULT NULL,
  `rating` double DEFAULT NULL,
  `review` varchar(500) DEFAULT NULL,
  `userid` varchar(100) DEFAULT NULL,
  `date_` varchar(100) DEFAULT NULL,
  `uname` varchar(100) DEFAULT NULL,
  `sentiment` varchar(100) DEFAULT 'non',
  PRIMARY KEY (`sno`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=latin1;

/*Data for the table `reviews` */

insert  into `reviews`(`sno`,`prodid`,`rating`,`review`,`userid`,`date_`,`uname`,`sentiment`) values (50,'1',5,'nicework','a','2022-04-09 19:30:05','a','positive'),(51,'1',4,'nice product','a','2022-04-14 15:08:29','a','neutral'),(52,'1',3,'bad product','a','2022-04-14 15:42:29','a','neutral');

/*Table structure for table `users` */

DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `name` varchar(100) DEFAULT NULL,
  `userid` varchar(100) NOT NULL,
  `passwrd` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  `phno` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`userid`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

/*Data for the table `users` */

insert  into `users`(`name`,`userid`,`passwrd`,`email`,`phno`) values (NULL,'a','a',NULL,NULL),('sajid','sajid','1234','sajid24x7@gmail.com','8121953811');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
