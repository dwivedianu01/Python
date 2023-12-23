# Python program to demonstrate
# find_one() method

from pymongo import MongoClient

client = MongoClient('localhost', 27017)


# Connecting to the database named
# tech2
db = client.tech2

coll = db.Employee


# Searching through the database
# using find_one method.
result = coll.find_one({'_id': 1})
print(result)
