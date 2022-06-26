#Using psycopg2

import psycopg2 

conn = psycopg2.connect(
    database="test", user='postgres', password='password', host='localhost', port= '5432'
)
conn.autocommit = True
cur = conn.cursor()
cur.execute('''CREATE TABLE test
               (
                Ticker VARCHAR(40) NOT NULL, 
                Date DATE NOT NULL,
                -- Time TIME NOT NULL,
                Open FLOAT NOT NULL,
                High FLOAT NOT NULL,
                Low FLOAT NOT NULL,
                Close FLOAT NOT NULL
                );''')
               
print("\n Table created successfully!")

# sql2 = ''' COPY test(Ticker,Date,Time,Open,High,Low,Close)
sql2 = ''' COPY test(Ticker,Date,Open,High,Low,Close)
FROM 'D:\\test.csv'
DELIMITER ','
CSV HEADER;'''
  
cur.execute(sql2)
print("\n Importing Done successfully!")


conn.commit()
conn.close()