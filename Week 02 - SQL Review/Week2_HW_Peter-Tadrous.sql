-- Prep
CREATE DATABASE world;
USE world;

-- Question 1.
DESCRIBE city;
-- FOREIGN KEY: city.CountryCode refers to country.Code
DESCRIBE country;
-- No Foreign Keys.
DESCRIBE countrylanguage;
-- FOREIGN KEY: countrylanguage.CountryCode refers to country.Code

-- Question 2.
SELECT
	Name,
    Region
FROM country
ORDER BY Name;

-- Question 3.
SELECT
	Name,
    Percentage
FROM country INNER JOIN countrylanguage
ON country.Code = countrylanguage.CountryCode
WHERE Language = 'Chinese'
ORDER BY Percentage DESC;

-- Question 4.
SELECT
	Name,
    Percentage
FROM country INNER JOIN countrylanguage
ON country.Code = countrylanguage.CountryCode
WHERE
	Language = 'Arabic' AND
    Percentage > (
		SELECT avg(Percentage)
        FROM countrylanguage
        WHERE Language = 'Arabic')
ORDER BY Percentage DESC;

-- Question 5.
SELECT sum(city.Population) as 'Urban Population in Western Europe'
FROM city INNER JOIN country
ON city.CountryCode = country.Code
WHERE country.Region = 'Western Europe';

-- Question 6.
SELECT
	country.Name as 'Country',
    count(countrylanguage.Language)
FROM country INNER JOIN countrylanguage
ON country.Code = countrylanguage.CountryCode
GROUP BY country.Name;

CREATE DATABASE nypl_menus;
USE nypl_menus;

-- Question 7a.
-- A row in nypl_menus.menu_pages represents a page on a menu in this database of menus.
-- The primary key is a menu_page_id, which uniquely identifies a single page.
-- The column menu_id connects it to nypl_menus.menus, though it doesn't look like it's stored as a foreign key.

-- Question 7b.
-- A row in nypl_menus.menu_items represents the item number on a particular menu in a database of menus.
-- The column menu_page_id connects it to nypl_menus.menu_pages, though it doesn't look like it's stored as a foreign key.
-- The purpose of the dish_id column is to uniquely identify a particular dish. The same dish may be on several menu's,
-- so the dish data is stored in a separate table.

-- Question 7c.
-- A row in nypl_menus.dishes represents a single dish that is served across this database of menus.
-- This dish can be on one menu, or many menus.

-- Question 7d.
SELECT
	menu_items.menu_items_id as 'Item ID',
    dishes.name as 'Name of Dish',
    dishes.first_appeared as 'Year First Listed',
    dishes.last_appeared as 'Year Last Listed'
FROM menu_items INNER JOIN dishes
ON menu_items.dish_id = dishes.dish_id
WHERE dishes.name LIKE '%Curry%';

-- Question 7e.
SELECT
	menus.sponsor as 'Sponsor/Restaurant',
    menus.place as 'Place',
    menus.location as 'Location',
    dishes.name as 'Name of Dish'
FROM menus, dishes, menu_items, menu_pages
WHERE
	dishes.dish_id = menu_items.dish_id AND
    menu_items.menu_page_id = menu_pages.menu_page_id AND
    menu_pages.menu_id = menus.menu_id AND
    dishes.name LIKE '%lo mein%';