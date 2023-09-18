import json
 
 
def update(new_json_data, filename='data/data.json'):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data["employees"].append(new_json_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent = 4)
 
    # python object to be appended
input_data = {
    "name": "salman",
    "emp_id": 534562,    
    "address": "Lane 3, Chandigarh"
}
     
update(input_data)
