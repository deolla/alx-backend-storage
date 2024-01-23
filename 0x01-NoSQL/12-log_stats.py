#!/usr/bin/env python3
"""A Python script that provides stats about Nginx logs stored in MongoDB"""
from pymongo import MongoClient


def get_nginx_logs_stats():
    """Get Nginx Log"""
    client = MongoClient('mongodb://localhost:27017/')
    db = client.log
    collection = db.nginx

    total_logs = collection.count_documents({})
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    method_stats = {method: collection.count_documents({
        "method": method
    }) for method in methods}

    get_status_count = collection.count_documents({
        "method": "GET", "path": "/status"
    })
    client.close()
    return total_logs, method_stats, get_status_count


def display_stats(total_logs, method_stats, get_status_count):
    """ Display Status"""
    print(f"{total_logs} logs")
    print("Methods:")
    for method in method_stats:
        print(f"\tmethod {method}: {method_stats[method]}")
    print(f"{get_status_count} status check")


if __name__ == "__main__":
    total_logs, method_stats, status_check_count = get_nginx_logs_stats()
    display_stats(total_logs, method_stats, status_check_count)
