import mysql.connector


def retrieve_data():
    global mycursor, mycursor
    try:
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="level7"
        )
        mycursor = mydb.cursor()
        mycursor.execute("SELECT name, product_name product,quantity FROM `transctions` INNER JOIN customers WHERE customers.customer_id = transctions.customer_id")
        result = mycursor.fetchall()
        print("Retrieved data from the 'customers' table:")
        for row in result:
            print(row)

    except mysql.connector.Error as err:
        print("MySQL Error:", err)

    finally:
        if 'mydb' not in locals() or not mydb.is_connected():
            return
        mycursor.close()
        mydb.close()
        print("Database connection closed.")


retrieve_data()
