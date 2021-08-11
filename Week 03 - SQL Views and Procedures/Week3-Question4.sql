DELIMITER \\
DROP PROCEDURE IF EXISTS Subtract_5 \\
CREATE PROCEDURE Subtract_5(num INT)
BEGIN
	DECLARE Result INT;
    SET Result = num - 5;
    SELECT Result;
END \\
DELIMITER ;

CALL Subtract_5(13);
CALL Subtract_5(2);