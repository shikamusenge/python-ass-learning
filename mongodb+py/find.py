from conn_mongo import customersCollection

data = customersCollection.find()

for item in data:
    print(item)