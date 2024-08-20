#!/usr/bin/env python3
from pymongo import MongoClient


def nginx_stats(mongo_collection):
    """Provides statistics about Nginx logs stored in a MongoDB collection."""
    # Count total number of documents in the collection
    total_logs = mongo_collection.count_documents({})
    
    # Count the number of documents with each HTTP method
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {method: mongo_collection.count_documents({"method": method}) for method in methods}
    
    # Count the number of documents with method=GET and path=/status
    get_status = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    
    # Output the statistics
    print(f"{total_logs} logs")
    print("Methods:")
    for method in methods:
        print(f"\tmethod {method}: {method_stats[method]}")
    print(f"{get_status} status check")

if __name__ == "__main__":
    # Establish MongoDB connection
    client = MongoClient("mongodb://localhost:27017/")
    
    # Access the logs database and nginx collection
    db = client.logs
    nginx_collection = db.nginx
    
    # Display the stats
    nginx_stats(nginx_collection)
