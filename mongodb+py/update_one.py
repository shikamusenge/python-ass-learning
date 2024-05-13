from conn_mongo import customersCollection

myquery = { "name":"KWIZERA Elisa" }
newvalues = { "$set": { "adress": "NYAGATARE-EAST-RWANDA" } }

updated_customer=customersCollection.update_one(myquery,newvalues)

print(f"update succesfully:{updated_customer}")