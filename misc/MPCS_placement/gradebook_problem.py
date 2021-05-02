# https://uchicago.kattis.com/problems/uchicagoplacement.gradebook
# The Professor's Gradebook problem MPCS 2017-2018 Placement Exam
from math import ceil

N, M = input().split() #N is the number of students, M is the number of assingments

N = int(N)
M = int(M)

#building a dictionary for the students and their grades
students_information = {}
for i in range(N):
	student_information = []
	student_information = input().split()
	students_information["student_" + str(i)] = student_information

#print(students_information)

#get rid of lowest grade
for student, grades in students_information.items():
	grades.remove(min(grades[1:M+1]))

#print(students_information)

#calcualting s_total
for student, grades in students_information.items():
	s_total = 0
	temp_grades = grades[1:M+1]
	for grade in temp_grades:
		s_total += int(grade)
	grades.append(s_total)

#print(students_information)

#finding top grade
top_grades = []
for student, grades in students_information.items():
	top_grades.append(int(grades[-1]))

#print(top_grades)
top_grade = max(top_grades)

#print(top_grade)
#print(students_information)

#finding s_adjusted for each student
for student, grades in students_information.items():
	s_total = grades[-1]
	s_adjusted = (s_total) / (top_grade) * 100
	s_adjusted = float(s_adjusted)
	grades.append(math.ceil(s_adjusted))

#print(students_information)

#giving a letter grade
for student, grades in students_information.items():
	if grades[-1] < 60:
		grades.append("F")
	elif grades[-1] < 70:
		grades.append("D")
	elif grades[-1] < 80:
		grades.append("C")
	elif grades[-1] < 90:
		grades.append("B")
	elif grades[-1] <= 100:
		grades.append("A")

for student, grades in students_information.items():
	answer = ""
	answer = (str(grades[0]) + " " + str(grades[-3]) + " " +str(grades[-2]) + " " + str(grades[-1]))
	print(answer)