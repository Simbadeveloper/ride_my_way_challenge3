import psycopg2
import os

def connect_to_db():
    """  Method for connecting to the database.  """
    DB_URL = os.getenv('DATABASE_URL', None)
    if DB_URL:
        return psycopg2.connect(DB_URL)
    connection = 'dbname=development user=postgres password=password77 host=localhost '
    print (connection)
    try:
        return psycopg2.connect(connection)
    except:
        print("can't connect")

conn=connect_to_db()
cur = conn.cursor()

def users():
    """  Method for creating the users table.  """
    
    table = (
        """ 
        CREATE TABLE users(
        id serial PRIMARY KEY,
        username varchar UNIQUE,
        firstname varchar,
        lastname varchar,
        email varchar UNIQUE, 
        password varchar);
        """
        )
    cur.execute(table)
    conn.commit()
    print("Created")

def rides():
    """  Method for creating the rides table.  """

    table = (
        """
        CREATE TABLE rides(
            id serial PRIMARY KEY,
            driver varchar UNIQUE NOT NULL,
            destination varchar,
            departure_time varchar, 
            route varchar, 
            extras varchar);
        """
    )
    cur.execute(table)
    conn.commit()
    

def requests():
    """  Method for creating the requests table.  """

    table = (
        """
        CREATE TABLE requests(
            id serial PRIMARY KEY,
            username varchar,
            ride_id int,
            status varchar);
        """
    )
    cur.execute(table)
    conn.commit()

if __name__ == "__main__":
   users()
   rides()
   requests()
