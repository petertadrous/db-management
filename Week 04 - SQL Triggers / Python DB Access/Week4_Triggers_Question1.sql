USE university;


DROP TABLE IF EXISTS university.transaction_log;
CREATE TABLE university.transaction_log (
	user_id varchar(30) not null,
	course_id varchar(8) not null,
	trans_id int not null primary key auto_increment,
	descrip varchar(50),
	timeofchange datetime default current_timestamp);


DELIMITER \\
DROP TRIGGER IF EXISTS transaction_trigger; \\
CREATE TRIGGER transaction_trigger
	AFTER UPDATE ON enroll
	FOR EACH ROW
  BEGIN
	INSERT INTO transaction_log (user_id,course_id,descrip)
	VALUES (user(), OLD.classNumber, CONCAT('Grade changed from ',OLD.grade,' to ',NEW.grade,'.'));
END \\
DELIMITER ;


update enroll set grade='A' where stuId='S1001';

SELECT * FROM transaction_log;

update enroll set grade='C' where stuId='S1001' and classNumber='HST205A';
SELECT * FROM transaction_log;