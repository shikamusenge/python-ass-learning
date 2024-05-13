from conn_mysql import conn

mycursor = conn.cursor()

sql = "DELETE FROM customers WHERE customer_id=1"

mycursor.execute(sql)

conn.commit()

print(mycursor.rowcount, "record(s) deleted")
