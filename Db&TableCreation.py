import psycopg2 
conn = psycopg2.connect(
   database="postgres", user='postgres', password='postgres', host='localhost', port= '5432'
)
conn.autocommit = True
cursor = conn.cursor()
sql = '''CREATE DATABASE stocks''';
cursor.execute(sql)
print("\n Database created successfully!")

conn.close()



conn = psycopg2.connect(
    database="stocks", user='postgres', password='postgres', host='localhost', port= '5432'
)
conn.autocommit = True
cur = conn.cursor()
cur.execute('''CREATE TABLE prices
               (
                Ticker VARCHAR(40) NOT NULL, 
                Date DATE NOT NULL,
                Open FLOAT NOT NULL,
                High FLOAT NOT NULL,
                Low FLOAT NOT NULL,
                Close FLOAT NOT NULL
                               
                );''')
               
print("\n Table created successfully!")
conn.close()

# Adj_Close FLOAT NOT NULL,
# Volume BIGINT NOT NULL,
