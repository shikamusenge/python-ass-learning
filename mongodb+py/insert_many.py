from conn_mongo import customersCollection
new_customer=[{
    "name": "HOGOZA Peace",
    "age": 22,
    "adress": "NYAGATARE-EAST-RWANDA"
},
{
    "name": "UWITONDANISHEMA Muslim",
    "age": 23,
    "adress": "NGOMA-EAST-RWANDA"
},{
    "name": "KWIZERA Elisa",
    "age": 24,
    "adress": "NYARUGENGE-KIGARI-RWANDA"
}
]

created_customer=customersCollection.insert_many(new_customer)

print(f"customer added:{created_customer}")