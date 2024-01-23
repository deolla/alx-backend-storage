#!/usr/bin/env python3
"""Top student"""
from pymongo import MongoClient


def top_students(mongo_collection):
    pipeline = [
        {
            "$unwind": "$scores"  # Unwind the scores array to get separate documents for each score
        },
        {
            "$group": {
                "_id": "$_id",  # Group by student ID
                "averageScore": {"$avg": "$scores.score"}  # Calculate the average score
            }
        },
        {
            "$lookup": {
                "from": "students",  # Assuming the collection name is "students"
                "localField": "_id",
                "foreignField": "_id",
                "as": "student_info"
            }
        },
        {
            "$unwind": "$student_info"  # Unwind the student_info array
        },
        {
            "$project": {
                "_id": 0,  # Exclude the default _id field
                "student_id": "$_id",
                "name": "$student_info.name",
                "averageScore": 1
            }
        },
        {
            "$sort": {"averageScore": -1}  # Sort by averageScore in descending order
        }
    ]

    result = list(mongo_collection.aggregate(pipeline))
    return result
