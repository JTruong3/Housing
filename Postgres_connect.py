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




