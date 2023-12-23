import subprocess

# List of file names to execute in sequence
file_names = ["MongoDb\\insertOneRow.py", "MongoDb\\insertManyRow.py", "MongoDb\\insertBulkData.py","MongoDb\\findOne.py",
              "MongoDb\\findOneAndUpdate.py","MongoDb\\findOneAndReplace.py","MongoDb\\findOneAndDelete.py"#,"MongoDb\\DeleteAll.py"#
              ]

# Iterate through the list and execute each file
for file_name in file_names:
    subprocess.run(["python", file_name])


