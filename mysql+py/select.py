# import mysql.connector
#
# # Establishing a connection to the MySQL server
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="",
#     database="level7"
# )
#
# # Creating a cursor object
# mycursor = mydb.cursor()
#
# # Executing the SQL query
# mycursor.execute("SELECT * FROM customers")
#
# # Fetching all rows from the result
# myresult = mycursor.fetchall()
#
# # Printing the rows
# for x in myresult:
#     print(x)
