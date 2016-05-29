import psycopg2 as pg
def getConnection():
    try:
        return pg.connect(database='amitdb',user='amit',password='amit',host='localhost', port=5432)
    except:
        return None
