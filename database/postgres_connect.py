from datetime import date
from re import ASCII
import psycopg2
import pandas as pd

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

create_table_query = '''CREATE TABLE HOUSE_DATA 
                        (Address VARCHAR(255),
                        Description VARCHAR(255),
                        Laundry VARCHAR(8),
                        Price INT,
                        Beds VARCHAR(255),
                        Baths VARCHAR(255),
                        Date_Listed VARCHAR(255),
                        Property_Type VARCHAR(255),
                        Monthly_Mortage VARCHAR(255),
                        Link VARCHAR(255));
            '''

cursor.execute(create_table_query)
connection.commit()

house_list = pd.read_csv("sample.csv")
for ind in house_list.index:
    insert_placeholder = 'INSERT INTO house_data VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);'
    address = house_list['Address'][ind]
    description = str(ind)
    laundry = house_list['Laundry'][ind]
    price = int(house_list['Price'][ind])
    beds = house_list['Beds'][ind]
    baths = house_list['Baths'][ind]
    date_listed = house_list['Date Listed'][ind]
    property_type = house_list['Property Type'][ind]
    monthly_mortgage = house_list['Estimated Monthly Mortgage Payment ($)'][ind]
    lnk = house_list['Link'][ind]
    cursor.execute(insert_placeholder, (address,description,laundry,price,beds,baths, date_listed,property_type,monthly_mortgage,lnk))




cursor.close()
connection.close()
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
