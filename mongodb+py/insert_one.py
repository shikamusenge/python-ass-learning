from conn_mongo import customersCollection
new_customer={
    "name":"SHIKAMUESENGE Philemon",
    "age":24,
    "adress":"KIREHE-EAST-RWANDA"
}

created_customer=customersCollection.insert_one(new_customer)

print(f"customer added:{created_customer}")