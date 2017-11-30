import psycopg2
import os
import random

# Externalizing configuration
PGHOST = os.getenv('PGHOST', 'db')
PGDATABASE = os.getenv('PGDATABASE', 'postgres')
PGUSER = os.getenv('PGUSER', 'postgres')
PGPASSWORD = os.getenv('PGPASSWORD', 'mysecretpassword')

# Generating test data
optionA = "a"
optionB = "b"
random.choice([optionA, optionB])
tuples = [(i, random.choice([optionA, optionB])) for i in range(1,16)]

try:
    conn = psycopg2.connect(dbname=PGDATABASE, user=PGUSER, password=PGPASSWORD, host=PGHOST)
    cursor = conn.cursor()
    cursor.execute("""DROP TABLE IF EXISTS votes""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS votes (id VARCHAR(255) NOT NULL UNIQUE, vote VARCHAR(255) NOT NULL);""")
    args_str = ','.join(cursor.mogrify("(%s,%s)", x).decode('utf-8') for x in tuples)
    cursor.execute("INSERT INTO votes VALUES " + args_str)
    cursor.execute("""COMMIT;""")
    cursor.execute("""SELECT COUNT (*) FROM votes;""")
    res = cursor.fetchone()
    print("Inserted {} values in table votes (PGDATABASE={}, PGHOST={}, PGUSER={})".format(res[0], PGDATABASE, PGHOST, PGUSER))
except Exception as e:
    print("Uh oh, can't connect. Invalid dbname, user or password?")
    print(e)