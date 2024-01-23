#!/usr/bin/env python3
"""A Python function that returns list of school having a specific topic"""


def schools_by_topic(mongo_collection, topic):
    """Returns the list of school having a specific topic"""
    docs = mongo_collection.find({
        'topics': topic
    })
    schools = []

    for school in docs:
        schools.append({
            '_id': school.get('_id'),
            'name': school.get('name'),
            'topics': school.get('topics', [])
        })

    return schools
