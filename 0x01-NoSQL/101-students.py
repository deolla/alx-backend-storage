#!/usr/bin/env python3
"""A Python function that returns all students sorted by average score"""


def top_students(mongo_collection):
    students = mongo_collection.find()
    student_scores = []
    
    for student in students:
        if 'scores' in student:
            scores = student['scores']
            average_score = sum(score['score'] for score in scores) / len(scores)
            student_scores.append((student['_id'], student['name'], scores, average_score))
    sorted_students = sorted(student_scores, key=lambda x: x[3], reverse=True)
    
    for student in sorted_students:
        student_id = student[0]
        student_name = student[1]
        scores = student[2]
        average_score = student[3]
        print(f"[{student_id}] {student_name} - {scores}")
    
    for student in sorted_students:
        student_id = student[0]
        student_name = student[1]
        average_score = student[3]
        print(f"[{student_id}] {student_name} => {average_score}")
    return sorted_students
