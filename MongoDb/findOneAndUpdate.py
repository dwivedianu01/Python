from pymongo import MongoClient
from pymongo import ReturnDocument


# Create a pymongo client
client = MongoClient('localhost', 27017)

db = client['tech2']

# Create a collection
coll = db['Employee']

result = coll.find_one({'_id': 3})
print(result)

# Increasing Age of Siddhnat by 7 
print(
coll.find_one_and_update({'_id': 3}, 
						{ '$set': { "Age" : '7'} }, 
						projection = { "name" : 1,"Age" : 1 }, 
						return_document = ReturnDocument.AFTER))

