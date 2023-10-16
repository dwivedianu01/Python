from pymongo import MongoClient # import mongo client to connect  
import pprint  
# Creating instance of mongoclient  
client = MongoClient()  
# Creating database  
db = client.javatpoint  
student = {"id": "10023",  
"name": "Anupam",  
"department": "Art",  
}  
# Creating document  
students = db.student  
# Inserting data  
students.insert_one(student)  
# Fetching data  
pprint.pprint(students.find_one())  
