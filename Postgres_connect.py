from re import ASCII
import psycopg2

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

cursor.execute()



cursor.close()
connection.close()
# ck_table = "SELECT * FROM pg_catalog.pg_tables;"
#cursor.execute(ck_table)

# /Applications/Postgres.app/Contents/Versions/14/bin/psql -p5432 "jasontruong"
