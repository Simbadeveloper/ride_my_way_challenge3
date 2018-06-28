import psycopg2
import sys

"""
Drop all tables of database you given.
"""

try:
    conn = psycopg2.connect("dbname='test_db' user='postgres' password='password77'")
    conn.set_isolation_level(0)
except:
    print "Unable to connect to the database."

cur = conn.cursor()

try:
    cur.execute("SELECT table_schema,users FROM information_schema.tables WHERE table_schema = 'public' ORDER BY table_schema,users")
    rows = cur.fetchall()
    for row in rows:
        print "dropping table: ", row[1]
        cur.execute("drop table " + row[1] + " cascade")
    cur.close()
    conn.close()
except:
    print "Error: ", sys.exc_info()[1]