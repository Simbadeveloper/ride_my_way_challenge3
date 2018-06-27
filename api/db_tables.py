import os
import psycopg2

from config import con

#connecting to the database
# con = psycopg2.connect(os.environ['DEV_DB_URI'])
try:
    con = psycopg2.connect(database='development', user='postgres', host='localhost', password='password77')
except:
    print ("NOPE NOPE NOPE!!")
#object that allows the execution of sql statements to the database
cur = con.cursor()

def users():
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
    con.commit()

def rides():
    pass

def requests():
    pass

