import pandas as pd, json, os
import psycopg2

# List of records
records = [
    ("1", "Ter Stegen", "GK"), 
    ("18", "Alba", "LD"),
    ("15", "Lenglet", "CD"),
    ("3", "Pique", "CD"),
    ("20", "Roberto", "RD"),
    ("21", "De Jong", "LM"),
    ("5", "Busquets", "CM"),
    ("4", "Rakitic", "RM"),
    ("17", "Griezmann", "LS"),
    ("9", "Suarez", "CS"),
    ("10", "Messi", "RS")]
table = pd.DataFrame.from_records(records, columns=["Number", "Name", "Position"])
print(table)

try:
    connection = psycopg2.connect(user = "postgres",
                                    password = "postgres",
                                    host = "localhost",
                                    port = "5432",
                                    database = "postgres")
    cursor = connection.cursor()
    
    select = """ INSERT INTO footballer (player_number, name, position) VALUES (%s,%s,%s) """
    # Cursor for one row
    cursor.execute(select, records[0])

    # Cursor for many rows
    cursor.executemany(select, records)
    connection.commit()

    count = cursor.rowcount
    print(count, "record(s) inserted succefully into postgres table")

except (Exception, psycopg2.Error) as error:
    if(connection):
        print("Failed to insert record(s) into postgres table", error)

finally:
    # Closing database connection
    if(connection):
        cursor.close()
        connection.close()
        print("Postgres connection is closed")