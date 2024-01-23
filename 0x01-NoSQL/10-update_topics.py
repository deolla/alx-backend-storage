#!/usr/bin/env python3
"""A Python function that changes all topic of school document based on name"""


def update_topics(mongo_collection, name, topics):
    """Changes all topics of a school document based on the name"""
    updates = mongo_collection.update_many({
        'name': name },
        { '$set': {'topics': topics }}
    )
    doc = updates.modified_count
    return doc

