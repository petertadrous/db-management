import mysql.connector
from mysql.connector import errorcode
import pandas as pd


def connect_to_db(database_name):
    try:
        cnx = mysql.connector.connect(user='root',
                                      password='kettlecorn',
                                      host='localhost',
                                      database=database_name)
    
        return cnx
    except mysql.connector.Error as e:
        print(e)
        print("done")
        
def query_to_df(database,query):
    cnx = connect_to_db(database)
    
    with cnx.cursor() as cursor:
        
        cursor.execute(query)
        df = pd.DataFrame(cursor.fetchall(), columns=cursor.column_names)

    cnx.close()
    
    return df



db = 'university'
question_2 = """
SELECT
    lastName,
    firstName
FROM student
WHERE major = 'Math'
"""
cnx = connect_to_db(db)
with cnx.cursor() as cursor:
    cursor.execute(question_2)

    for (firstName, lastName) in cursor:
        print("{}, {} is a student".format(lastName,firstName))

cnx.close()




question_3_database = 'world'
question_3_query = """
SELECT
    Name,
    Region
FROM country
ORDER BY Name;
"""
question_3_df = query_to_df(question_3_database, question_3_query)

print(question_3_df)




question_4_database = 'nypl_menus'
question_4_query = """
select menus.sponsor, menus.place, menus.location, dishes.name
from menus, menu_pages, menu_items, dishes
where menus.menu_id = menu_pages.menu_id
    and menu_pages.menu_page_id = menu_items.menu_page_id 
    and dishes.dish_id = menu_items.dish_id
    and dishes.name like '%lo mein%';

"""
question_4_df = query_to_df(question_4_database, question_4_query)

print(question_4_df)

