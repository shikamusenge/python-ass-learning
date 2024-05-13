from conn_mongo import customersCollection

data = customersCollection.find_one({"name":"KWIZERA Elisa"})

print(data)