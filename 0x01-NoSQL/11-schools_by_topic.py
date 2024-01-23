#!/usr/bin/env python3
"""A Python function that returns list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    docs = mongo_collection.find({
        'topic': topic
    })
    schools = []

    for i in docs:
        schools.append(i['names'])
    return schools
