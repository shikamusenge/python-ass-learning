from conn_mysql import  conn
mycursor = conn.cursor()
newTable=mycursor.execute("CREATE TABLE customers (cutsomer_id int primary key AUTO_INCREMENT, name VARCHAR(255), address VARCHAR(255))")
print(f"table customer created{newTable}")
mycursor.close()
conn.close()
