#!/usr/bin/env python3
"""Python script that provides stats about Nginx logs stored in MongoDB"""
import pymongo


# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["logs"]
collection = db["nginx"]
total_logs = collection.count_documents({})
print(f"{total_logs} logs")

print("Methods:")

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
for method in methods:
    count = collection.count_documents({"method": method})
    print(f"\tmethod {method}: {count}")

status_check_count = collection.count_documents({
    "method": "GET", "path": "/status"
})

print(f"{status_check_count} status check")
