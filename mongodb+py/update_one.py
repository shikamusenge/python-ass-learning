from conn_mongo import customersCollection

myquery = { "age": 22 }
newvalues = { "$set": { "bonus": "22$" } }

updated_customer=customersCollection.update_many(myquery,newvalues)

print(f"update succesfully:{updated_customer}")