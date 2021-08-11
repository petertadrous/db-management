USE nypl_menus;

CREATE VIEW Ordered_Menus AS
SELECT
	menus.name AS 'Name',
	menus.sponsor AS 'Sponsor',
	menus.dish_count AS 'Num_Dishes',
	menus.menu_date AS 'Menu_Date',
	menus.page_count AS 'Page_Count'
FROM menus
ORDER BY dish_count DESC;

SELECT * FROM Ordered_Menus;

SELECT * FROM Ordered_Menus
WHERE Menu_Date > '1950-01-01';