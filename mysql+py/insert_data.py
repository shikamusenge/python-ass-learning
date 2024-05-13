from conn_mysql import conn
cuso = conn.cursor()
name=input("Enter Name")
address = input("Address")
sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = (name, address)
cuso.execute(sql, val)
conn.commit()
print(f"data inserted{cuso.rowcount}")

conn.close()