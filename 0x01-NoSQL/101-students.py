#!/usr/bin/env python3
"""Top student"""
from pymongo import MongoClient


def top_students(mongo_collection):
    pipeline = [
        {
            "$unwind": "$scores"
        },
        {
            "$group": {
                "_id": "$_id",  # Group by student ID
                "averageScore": {"$avg": "$scores.score"}
            }
        },
        {
            "$lookup": {
                "from": "students",
                "localField": "_id",
                "foreignField": "_id",
                "as": "student_info"
            }
        },
        {
            "$unwind": "$student_info"
        },
        {
            "$project": {
                "_id": 0,
                "student_id": "$_id",
                "name": "$student_info.name",
                "averageScore": 1
            }
        },
        {
            "$sort": {"averageScore": -1}
        }
    ]

    result = list(mongo_collection.aggregate(pipeline))
    return result
