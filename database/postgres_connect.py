from datetime import date
from re import ASCII
import psycopg2
import pandas as pd
import json

day_var = date.today().strftime('%Y-%m-%d')

f = open('database/counter.json')
counters = json.load(f)
condo_key_counter = counters['condo_key_counter']
house_key_counter = counters['house_key_counter']

try:
    connection = psycopg2.connect(
        user = "jasontruong", 
        host = "localhost", 
        port = 5432,
        )
    cursor = connection.cursor()
    connection.commit()

except:
    print('Check connection parameters')

#Check if dataTable exists or not
# if 
#connection.commit()
# cursor.execute("""SELECT EXISTS (
#     SELECT FROM 
#         pg_tables
#     WHERE 
#         schemaname = 'public' AND 
#         tablename  = 'HOUSE_DATA'
#     );""")
# cursor.fetchone()[0]

# create_table_query = '''CREATE TABLE condo_townh_data 
#                         (id SERIAL PRIMARY KEY,
#                         Address VARCHAR(255),
#                         Description VARCHAR(10000),
#                         Laundry VARCHAR(8),
#                         Price INT,
#                         Beds VARCHAR(255),
#                         Baths VARCHAR(255),
#                         Date_Listed VARCHAR(255),
#                         Monthly_Mortage FLOAT,
#                         Link VARCHAR(255));
#             '''

# cursor.execute(create_table_query)
# connection.commit()
connection.commit()
house_list = pd.read_csv("house_data/HouseData_{}.csv".format(day_var))
for ind in house_list.index:
    
    address = house_list['Address'][ind]
    description = house_list['Description'][ind]
    laundry = house_list['Laundry'][ind]
    price = int(house_list['Price'][ind])
    beds = str(house_list['Beds'][ind])
    baths = str(house_list['Baths'][ind])
    date_listed = house_list['Date Listed'][ind]
    monthly_mortgage = house_list['Estimated Monthly Mortgage Payment ($)'][ind]
    lnk = house_list['Link'][ind]
    if "-" in house_list['Address'][ind]:
        condo_key_counter += 1
        insert_placeholder = 'INSERT INTO condo_townh_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        cursor.execute(insert_placeholder, (condo_key_counter,address,description,laundry,price,beds,baths,date_listed,monthly_mortgage,lnk))
    
    else:
        house_key_counter += 1
        insert_placeholder = 'INSERT INTO house_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
        cursor.execute(insert_placeholder, (house_key_counter,address,description,laundry,price,beds,baths,date_listed,monthly_mortgage,lnk))
connection.commit()



cursor.close()
connection.close()

newdict = {"condo_key_counter": condo_key_counter,"house_key_counter": house_key_counter}
with open("database/counter.json", "w") as jsonFile:
    json.dump(newdict, jsonFile)

# ck_table = "SELECT * FROM pg_catalog.pg_tables;"
#cursor.execute(ck_table)

# /Applications/Postgres.app/Contents/Versions/14/bin/psql -p5432 "jasontruong"

# test_case2 = "INSERT INTO test VALUES (%s,%s);"
# cursor.execute(test_case2,(item))
# connection.commit()
# test_case = "SELECT * FROM test"
# cursor.execute(test_case)
# cursor.fetchall()


#https://stackoverflow.com/questions/23103962/how-to-write-dataframe-to-postgres-table
