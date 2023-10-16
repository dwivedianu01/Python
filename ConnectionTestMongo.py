# importing module 
from pymongo import MongoClient 
  
# creation of MongoClient 
client=MongoClient() 
try:
# Connect with the portnumber and host 
  client = MongoClient("mongodb://userid:password@localhost:27017/test-db") 
  db = client["test-sbfdb"]
  print("connect")
  collection_names = db.list_collection_names()

  # Print the collection names
  for collection_name in collection_names:
      print(collection_name)

  # Close the connection when you're done
  client.close()
# Access database 
except:
  print("Failed")

