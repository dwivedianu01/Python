from pymongo import MongoClient 


myclient = MongoClient("mongodb://localhost:27017/") 

# database 
db = myclient["tech2"] 


Collection = db["Employee"] 

# Search Filter
searchFilter ={'_id': {"$gt": 20}} 


print("Response : ") 
print(Collection.find_one_and_delete(searchFilter)) 

print("\nThe data after find_one_and_delete() operation is:") 

for data in Collection.find(): 
	print(data) 
