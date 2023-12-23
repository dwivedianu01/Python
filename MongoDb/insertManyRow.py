# program to insert multiple rows in database
# importing Mongoclient from pymongo
from pymongo import MongoClient 

# Making Connection
myclient = MongoClient("mongodb://localhost:27017/") 

# database 
db = myclient["tech2"]

collection = db["Employee"]

# Creating Dictionary of records to be 
# inserted
record = [{ "_id": 2,
		"name": "Pooja",
		"Employed Id": "10002",
		"Department": "IT",
    "Email": "pooja@tech2.com",
    "Mobile": "+919111111111",
    "Age": 35
    },
    { "_id": 3,
		"name": "Siddhant",
		"Employed Id": "10003",
		"Department": "IT",
    "Email": "sid@tech2.com",
    "Mobile": "+919222222222",
    "Age": 6
    },
    { "_id": 4,
		"name": "Anush",
		"Employed Id": "10004",
		"Department": "IT",
    "Email": "anush@tech2.com",
    "Mobile": "+919333333333",
    "Age": 1
    },
    { "_id": 5,
		"name": "Sandeep",
		"Employed Id": "10005",
		"Department": "IT",
    "Email": "sandy@tech2.com",
    "Mobile": "+919444444444",
    "Age": 37
    },
    { "_id": 6,
		"name": "Mahesh",
		"Employed Id": "10006",
		"Department": "IT",
    "Email": "mh@tech2.com",
    "Mobile": "+919555555555",
    "Age": 67
    },
    { "_id": 7,
		"name": "Neeta",
		"Employed Id": "10007",
		"Department": "IT",
    "Email": "neeta@tech2.com",
    "Mobile": "+919666666666",
    "Age": 59
    }
    ]



# by using collection.insert_many()
rec_ids = collection.insert_many(record)
print("Ids inserted:", rec_ids.inserted_ids)


