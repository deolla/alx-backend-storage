#!/usr/bin/env python3
"""A Python function that returns all students sorted by average score"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    students = mongo_collection.find()

    student_scores = []

    for student in students:
        if 'topics' in student:
            scores = [topic.get('score', 0) for topic in student['topics']]
            average_score = sum(scores) / len(scores) if len(scores) > 0 else 0
            student_scores.append({
                '_id': student.get('_id'),
                'name': student.get('name'),
                'topics': student.get('topics'),
                'averageScore': average_score
            })

    sorted_students = sorted(
        student_scores,
        key=lambda x: x['averageScore'],
        reverse=True
    )

    return sorted_students
