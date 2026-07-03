student_name = input("Enter student name: ")
student_age = int(input("Enter student age: "))
student_branch = input("Enter student branch: ")
student_semester = int(input("Enter student semester: "))
current_year = 2026
Birth_year = current_year - student_age
after_5_years = student_age + 5
print("**********Student card***********")
print("Student Name:", student_name)
print("Student Age:", student_age)
print("Student Branch:", student_branch)
print("Student Semester:", student_semester)
print("Student Birth Year:", Birth_year)
print("Student Age in 5 Years:", after_5_years)
print("*********************************")