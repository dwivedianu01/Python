from pymongo import MongoClient 


myclient = MongoClient("mongodb://localhost:27017/") 

# database 
db = myclient["tech2"] 


Collection = db["Employee"] 

# Search Filter

print("Response : ") 
print(Collection.delete_many({})) 

print("\nThe data after delete() operation is:") 

for data in Collection.find(): 
	print(data) 
