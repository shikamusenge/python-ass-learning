import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')
mydb = myclient['customers']
customersCollection=mydb['customers']