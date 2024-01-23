#!/usr/bin/env python3
"""A Python script that provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def get_nginx_logs_stats():
    """Connect to MongoDB"""
    client = MongoClient()
    db = client.logs
    collection = db.nginx

    # Get the total number of logs
    total_logs = collection.count_documents({})

    print(f"{total_logs} logs")

    # Get the count of different methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_counts = {method: collection.count_documents({
        "method": method
    }) for method in methods}

    print("Methods:")
    for method, count in method_counts.items():
        print(f"    method {method}: {count}")

    # Get the count of logs with method=GET and path=/status
    status_check_count = collection.count_documents({
        "method": "GET", "path": "/status"
    })

    print(f"{status_check_count} status check")


if __name__ == "__main__":
    get_nginx_logs_stats()
