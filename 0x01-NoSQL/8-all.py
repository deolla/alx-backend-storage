#!/usr/bin/env python3
"""Write a Python function that lists all documents in a collection"""


def list_all(mongo_collection):
    """lists all documents in a collection"""
    docs = []
    results = mongo_collection.find()
    for i in results:
        docs.append(i)
    if len(docs) == 0:
        return []
    return docs
