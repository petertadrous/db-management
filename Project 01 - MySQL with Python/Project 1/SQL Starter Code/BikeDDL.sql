create database bikedb;
use bikedb;

DROP TABLE if EXISTS Bike;
DROP TABLE if EXISTS BikeKiosk;


CREATE TABLE BikeKiosk	(
	kioskID		INT NOT NULL,
	addr1	VARCHAR(50)  NOT NULL,
	addr2 	VARCHAR(50),
	city    VARCHAR(50)   NOT NULL,
	stat   CHAR(2)      NOT NULL,
	zip     CHAR(7)      NOT NULL,
	capacity  	INT,
	PRIMARY KEY (kioskID))
	ENGINE=INNODB;

CREATE TABLE Bike(
    bikeID INT  NOT NULL, 
    model VARCHAR(50), 
    currentKioskID INT, 
    INDEX kiosk_ind(currentKioskID),
    timeArrived DATETIME,
   atKiosk CHAR(1),
    PRIMARY KEY (bikeID),
    FOREIGN KEY (currentKioskID) REFERENCES bikedb.BikeKiosk(kioskID))
    ENGINE=INNODB;	
