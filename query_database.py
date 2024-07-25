import mysql.connector as connector

user = "root"
password = ""
database = "littlelemondb"

connection = connector.connect(user = user, 
                               password = password,
                               db = database)

cursor = connection.cursor()

show_tables_query = "SHOW tables" 
cursor.execute(show_tables_query)

print(cursor.fetchall())

cursor.execute("""
                SELECT c.CustomerName AS FullName
                    , c.ContactNumber
                    , o.TotalCost
                FROM customers c
                INNER JOIN orders o
                    ON c.CustomerID = o.CustomerID
                WHERE o.TotalCost > 60 
               """)

for row in cursor.fetchall():
    print(f"Customer Name: {row[0]}")
    print(f"Contact Number: {row[1]}")
    print(f"Total Cost: {row[2]}")


