# program to insert one row in database
# importing Mongoclient from pymongo
from pymongo import MongoClient 

# Making Connection
myclient = MongoClient("mongodb://localhost:27017/") 

# database 
db = myclient["tech2"]

collection = db["Employee"]

# Creating Dictionary of records to be 
# inserted
record = { "_id": 1,
		"name": "Anupam",
		"Employed Id": "10001",
		"Department": "IT",
    "Email": "anupam@tech2.com",
    "Mobile": "+919000000000",
    "Age": 40
    }



# by using collection.insert_one()
rec_id = collection.insert_one(record)
print("Id inserted: " + str(rec_id.inserted_id))    


