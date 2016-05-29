import psycopg2 as pg
import Connection
def getPlaces():
    conn = Connection.getConnection()
    cur = conn.cursor()
    cur.execute('select * from places')
    rows = cur.fetchall()
    conn.close();
    return rows