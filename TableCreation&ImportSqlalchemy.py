#  Using Sqlalchemy 

import pandas as pd
import glob
from sqlalchemy import create_engine
import sqlalchemy

engine = create_engine("postgresql://postgres:password@localhost:5432/postgres")


filepath = r"D:\\Index"
totalnor = 0
for file in glob.glob(filepath + "\*.csv"):
    # df = pd.read_csv(file, index_col=0, parse_dates=['Date'], dayfirst = True)
    df = pd.read_csv(file)
    # df1 = pd.DataFrame(df, columns= ['Date','Expiry','Strike', 'Time', 'Open', 'High', 'Low', 'Close'])
    df1 = pd.DataFrame(df)
    print(file)
    index = df.index
    nor = len(index)
    totalnor = totalnor + nor
    print(nor)
    df1.to_sql('niftyindex', engine, if_exists='append', index=False, dtype={
                    'Date': sqlalchemy.types.Date(),
                    'Time': sqlalchemy.types.Time(), 
                    'Open': sqlalchemy.types.Float(precision=3, asdecimal=True),
                    'High': sqlalchemy.types.Float(precision=3, asdecimal=True),
                    'Low': sqlalchemy.types.Float(precision=3, asdecimal=True),
                    'Close': sqlalchemy.types.Float(precision=3, asdecimal=True)})



print(totalnor)
print("\nImporting Done successfully!")

engine.execute('ALTER TABLE niftyindex ADD PRIMARY KEY ("Date", "Time");')
print("Table Primary key altered")


# conn=psycopg2.connect(
#     database="postgres",
#     user="postgres",
#     password="password",
#     host="localhost",
#     port="5432"
# )
# cursor = conn.cursor()
  
# # query to count total number of rows
# sql = 'SELECT count(*) from niftyindex;'
# data=[]
  
# # execute the query
# cursor.execute(sql,data)
# results = cursor.fetchone()
  
# #loop to print all the fetched details
# for r in results:
#   print(r)
# print("Total number of rows in the table:", r)


# conn.commit()
  
# # Closing the connection
# conn.close()