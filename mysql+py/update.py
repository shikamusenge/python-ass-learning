from conn_mysql import conn
cuso = conn.cursor()
name=input("Enter Name")
address = input("Address")
sql = "UPDATE customers SET name=%s, address=%s where customer_id=%s"
val = (name, address, 3)
cuso.execute(sql, val)
conn.commit()
print(f"data inserted{cuso.rowcount}")

conn.close()