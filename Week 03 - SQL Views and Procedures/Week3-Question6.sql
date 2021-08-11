USE nypl_menus;

DELIMITER \\
DROP PROCEDURE IF EXISTS avg_dish_price \\
CREATE PROCEDURE avg_dish_price(dish VARCHAR(30))
BEGIN
	SELECT
		ROUND(AVG(menu_items.price),2) AS 'avg_price'
    FROM dishes, menu_items
    WHERE
		dishes.dish_id = menu_items.dish_id AND
        dishes.name LIKE CONCAT('%',dish,'%');
END \\
DELIMITER ;

CALL avg_dish_price('pizza');
CALL avg_dish_price('steak');