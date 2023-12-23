# program to insert multiple rows in database
# importing Mongoclient from pymongo
import random
import string
from pymongo import MongoClient 

# Making Connection
myclient = MongoClient("mongodb://localhost:27017/") 

# database 
db = myclient["tech2"]

collection = db["Employee"]
def generate_mobile_number():
    # The first digit should be between 7 and 9 to comply with common mobile number ranges
    first_digit = str(random.randint(7, 9))
    rest_of_digits = ''.join(str(random.randint(0, 9)) for _ in range(9))
    mobile_number = first_digit + rest_of_digits
    return mobile_number
# Creating Dictionary of records to be 
# inserted
for i in range(8, 40):
  # generating random strings
  name = ''.join(random.choices(string.ascii_uppercase +
                             string.digits, k=9))
  record = { "_id": i,
      "name": name,
      "Employed Id": "1000"+ str(i),
      "Department": "IT",
      "Email": name+"@tech2.com",
      "Mobile": ""+generate_mobile_number(),
      "Age": i*2
      }
  rec_id = collection.insert_one(record)
print("Id inserted: " + str(rec_id.inserted_id))    






