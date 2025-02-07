student_heights = input("Input a list of student heights.").split()

for n in range (0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

sum = 0
student_count = 0

for n in student_heights:
    sum += n 
    student_count += 1


average = round(sum/student_count) 
print(average)