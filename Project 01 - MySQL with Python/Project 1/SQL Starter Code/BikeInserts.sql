use bikedb;

INSERT INTO BikeKiosk (`kioskID`, addr1, addr2, city, stat, zip, capacity) 
	VALUES (1, 'Broadway&23rd', NULL, 'NYC', 'NY', '11111', 6);
INSERT INTO BikeKiosk (`kioskID`, addr1, addr2, city, stat, zip, capacity) 
	VALUES (2, '603 Avenue A', NULL, 'NYC', 'NY', '12222', 2);
INSERT INTO BikeKiosk (`kioskID`, addr1, addr2, city, stat, zip, capacity) 
	VALUES (3, '333 First Avenue', 'northbound', 'NYC', 'NY', '11111', 4);
INSERT INTO BikeKiosk (`kioskID`, addr1, addr2, city, stat, zip, capacity) 
	VALUES (4, '655 Columbus Ave', '', 'NYC', 'NY', '12111', 5);
	
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`,atKiosk) 
	VALUES (1, 'ToughBike Classic', 2, '2015-02-19 11:33:03.564','y');
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`, atKiosk) 
	VALUES (2, 'FastBike', 1, '2015-02-18 11:33:29.263','y');
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`, atKiosk) 
	VALUES (3, 'ToughBike XTreme', 3, '2015-02-18 10:33:45.537','y');
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`, atKiosk) 
	VALUES (4, 'Lucille', 2, '2015-02-19 11:25:28.215','y');
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`, atKiosk) 
	VALUES (6, 'SuperFast', 3, '2021-02-19 11:25:28.215','y');
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`, atKiosk) 
	VALUES (7, "Kona Humuhumunukunukuapua'a", 1, '2021-02-19 11:25:28.215','y');
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`, atKiosk) 
	VALUES (8, 'Clockwork', 4, '2021-02-19 11:25:28.215','y');
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`, atKiosk) 
	VALUES (9, 'TailWind', 1, '2021-02-19 11:25:28.215','y');
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`, atKiosk) 
	VALUES (10, 'Road Dust', 3, '2021-02-19 11:25:28.215','y');
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`, atKiosk) 
	VALUES (11, 'The Flying Englishman', 4, '2021-02-19 11:25:28.215','y');
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`, atKiosk) 
	VALUES (12, 'Trek', 1, '2021-02-19 11:25:28.215','y');
INSERT INTO Bike (`bikeID`, model, `currentKioskID`, `timeArrived`, atKiosk) 
	VALUES (13, 'Mr. Bean', 1, '2021-02-19 11:25:28.215','y');