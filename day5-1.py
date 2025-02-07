student_scores = input("Input a list of student scores.").split()

for n in range (0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)


m = 0 #m = highest score
for n in student_scores: # n = item(s) in student_scores
    if n > m:
        m = n  # if the score in student_score is highest, add the data to m , and again looping to test all the score
print(f"The highest score in the class is {m}.")
    