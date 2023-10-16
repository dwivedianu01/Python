import pymongo

# Set up a MongoDB connection
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["admin"]
collection = db["salesorder"]

# Function to search text in all fields of documents
def search_text(query):
    regex_pattern = f".*{query}.*"
    print(regex_pattern)
    query_filter = {"$or": []}
    for key in collection.find_one().keys():
          query_filter["$or"].append({key: {"$regex": regex_pattern, "$options": "i"}})

    results = list(collection.find(query_filter))
    return results

if __name__ == "__main__":
    # Get user input for the search query
    query = input("Enter the search query: ")

    # Perform the search
    results = search_text(query)

    # Display the results
    print(f"Search Results Count: {len(results)}")
    for result in results:
        print(result)


