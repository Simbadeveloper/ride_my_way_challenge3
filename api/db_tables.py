import psycopg2

def connect_to_db():
    """  Method for connecting to the database.  """

    connection = 'dbname=development user=carpool password=carpool host=localhost '
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
            driver varchar NOT NULL,
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
            user_id int,
            ride_id int):
        """
    )
    cur.execute(table)
    conn.commit()
