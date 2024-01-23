#!/usr/bin/env python3
"""Python script that provides stats about Nginx logs stored in MongoDB"""
import pymongo

if __name__ == "__main__":
    client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
    collection = client.logs.nginx
    
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

    ids = collection.aggregate([
        {"$group":
            {
                "_id": "$ip",
                "count": {"$sum": 1}
            }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    print("IPs:")
    for i in ids:
        m = i.get("ip")
        count = i.get("count")
        print(f'\t{m}: {count}')
