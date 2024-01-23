#!/usr/bin/env python3
"""A Python function that returns all students sorted by average score"""
import operator

def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    students = []

    coll = mongo_collection.find()
    for document in coll:
        if "scores" not in document:
            continue

        scores = document["scores"]

        if not isinstance(scores, list):
            continue

        if len(scores) == 0:
            continue

        average_score = sum(score["score"] for score in scores) / len(scores)

        student_info = {
            "name": document["name"],
            "averageScore": average_score
        }

        students.append(student_info)

    students.sort(key=operator.itemgetter("averageScore"), reverse=True)

    sorted_student_names = [student["name"] for student in students]
    return sorted_student_names
