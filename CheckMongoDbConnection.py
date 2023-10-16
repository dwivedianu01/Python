import pymongo

# MongoDB connection parameters
host = "localhost"  # Replace with the MongoDB server's hostname or IP address
port = 27017  # Replace with the MongoDB server's port number
username = "username"  # Replace with your MongoDB username
password = "password"  # Replace with your MongoDB password
database_name = "test-db"  # Replace with the name of the database you want to connect to

try:
    # Create a MongoDB                                                                  client with username and password
    client = pymongo.MongoClient(host, port, username=username, password=password)

    # Check the connection by listing the available databases
    database_list = client.list_database_names()

    if database_name in database_list:
        print(f"Successfully connected to the MongoDB server at {host}:{port} as user {username}")
        print(f"Databases available on the server: {database_list}")
    else:
        print(f"Connected to the MongoDB server, but the database '{database_name}' does not exist.")
    
    # Close the MongoDB client
    client.close()

except pymongo.errors.ConnectionFailure as e:
    print(f"Failed to connect to the MongoDB server: {e}")
except Exception as e:
    print(f"An error occurred: {e}")
