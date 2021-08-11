USE nypl_menus;

CREATE VIEW totalMenus AS
DELIMITER \\
DROP PROCEDURE IF EXISTS totalMenus \\
CREATE PROCEDURE totalMenus(num INT)
BEGIN
	SELECT COUNT(*) AS total_menus
    FROM Ordered_Menus
    WHERE Page_Count = num;
END \\
DELIMITER ;

CALL totalMenus(13);
CALL totalMenus(3);