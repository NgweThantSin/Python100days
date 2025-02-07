student_score = {
    "Harry" : 81,
    "Ron"   : 78,
    "Hermione" : 99,
    "Draco" : 74,
    "Neville" : 62,
}

student_grades = {} 

for student in student_score:
    grade = student_score[student]
    if grade >= 91 and grade < 100:
        student_grades[student] = "Outstanding"
    elif grade >= 81 and grade < 90:
        student_grades[student] = "Exceeds Expectations"
    elif grade >= 71 and grade < 80:
        student_grades[student] = "Acceptable"
    else:
        student_grades[student] = "Fail"
        
print(student_grades)
