from psycopg2 import sql
from psycopg2 import extras
import psycopg2
import os

table = "car"
def select_cars(curr,conn,select_sql):
    select_sql = sql.SQL(
        """
        SELECT * 
        FROM {table}
        """
    ).format(
        table = sql.Identifier(table)
    )
    curr.execute(select_sql)
    results = curr.fetchall()
    return results

def insert_car(curr,conn,brand):
    try:
        curr.execute("INSERT INTO car (brand) VALUES (%s)", (brand,))
    except Exception as e:
        conn.close()

if __name__ == "__main__":
    conn = psycopg2.connect(
        os.getenv("POSTGRES_CONNECT_STRING","dbname = ******* user = ******* password = ******* host = ******* port = *******")
    )
    cursor = conn.cursor(cursor_factory = psycopg2.extras.DictCursor)
    conn.autocommit = True

    cars = select_cars(cursor,conn,select_cars)
    print(cars)

    insert_car(cursor,conn,'BMW')
    insert_car(cursor,conn,'Audi')

    cars = select_cars(cursor,conn,select_cars)
    print(cars)

    cursor.close()
    conn.close()





