#find_one_and_replace() method is differ from find_one_and_update() with the help of filter it replace the document rather than update the existing document.
from pymongo import MongoClient 


myclient = MongoClient("mongodb://localhost:27017/") 

# database 
db = myclient["tech2"] 


Collection = db["Employee"] 

# Search Filter
searchFilter ={'Age': 78} 


print("Response : ") 
print(Collection.find_one_and_replace(searchFilter,{'Age': 89})) 

print("\nThe data after find_one_and_delete() operation is:") 

for data in Collection.find(): 
	print(data) 
