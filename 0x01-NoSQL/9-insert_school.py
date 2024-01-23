#!/usr/bin/env python3
"""A Python function that inserts new document in collection based on kwargs"""


def insert_school(mongo_collection, **kwargs):
    """Inserts a new document in a collection"""
    docs = {}
    for key, value in kwargs.items():
        docs[key] = value
    ids = mongo_collection.insert_one(docs)
    new_ids = ids.inserted_id
    return new_ids
