from conn_mongo import customersCollection

myquery = { "age": 24 }

deleted_customer=customersCollection.delete_many(myquery)

print(f"delete succesfully:{deleted_customer}")