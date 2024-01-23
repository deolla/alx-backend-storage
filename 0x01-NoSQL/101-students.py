#!/usr/bin/env python3
"""A Python function that returns all students sorted by average score"""


def top_students(mongo_collection):
    # Find all documents in the collection
    students = mongo_collection.find()

    # Calculate the average score for each student
    for student in students:
        scores = student['topics']
        total_score = sum(score['score'] for score in scores)
        average_score = total_score / len(scores)
        student['averageScore'] = average_score

    # Sort the students by average score in descending order
    sorted_students = sorted(
        students,
        key=lambda x: x['averageScore'],
        reverse=True
    )

    # Print the sorted students and their scores
    for student in sorted_students:
        student_id = student['_id']
        student_name = student['name']
        student_topics = student['topics']
        print("[{}] {} - {}".format(student_id, student_name, student_topics))

    # Return the sorted students
    return sorted_students
