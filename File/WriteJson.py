# Python program to write JSON to a file 
 
import json
 
# Data to be written
input_data = {
    "name": "salman",
    "emp_id": 534562,    
    "address": "Lane 3, Chandigarh"
}
 
file = open ('data/data_new.json', "a+")    
json.dump(input_data, file)

