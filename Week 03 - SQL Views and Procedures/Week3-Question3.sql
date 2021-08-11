USE nypl_menus;

CREATE VIEW Location_Dishes AS
SELECT
	menus.location AS 'Location',
	menus.event AS 'Event',
	dishes.name as 'Dish_Name'
FROM menus, dishes, menu_items, menu_pages
WHERE
	dishes.dish_id = menu_items.dish_id AND
    menu_items.menu_page_id = menu_pages.menu_page_id AND
    menu_pages.menu_id = menus.menu_id;

SELECT * FROM Location_Dishes;

SELECT * FROM Location_Dishes
WHERE Dish_Name LIKE '%gumbo%';