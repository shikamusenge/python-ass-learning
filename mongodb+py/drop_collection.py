from conn_mongo import customersCollection

dropedcol= customersCollection.drop()
print(f"collection: {dropedcol}")

