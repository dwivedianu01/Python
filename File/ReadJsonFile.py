import json
json_string = '{"name": "Anupam", "address": "Lame no 5, Down street"}'

json_array = json.loads(json_string)

print(f"JSON array = {json_array}")

file = open ('data/data.json', "r")
 
# Reading from file
jsn = json.loads(file.read())
 
# Iterate
for i in jsn['employees']:
    print(i)
 
# Closing file
file.close()
