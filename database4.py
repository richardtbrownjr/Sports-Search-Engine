import csv
import psycopg2


con = psycopg2.connect("dbname=panthers2 user=richardt.brownjr.")

cur = con.cursor()


cur.execute("""
CREATE TABLE panthers2 (
    Num varchar PRIMARY KEY,
    Name varchar,
    Pos varchar,
    Age varchar,
    yrushing varchar,
    YReceiving varchar,
    TD varchar);""")

f = open('panthers20153.csv')

cur.copy_from(f, 'panthers2', sep=',', columns=('Num', 'Name', 'Pos', 'Age', 'YRushing', 'YReceiving','TD'))

f.close()

con.commit()
cur.close()
con.close()
