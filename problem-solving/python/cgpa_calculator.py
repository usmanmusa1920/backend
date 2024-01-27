# -*- coding: utf-8 -*-
# Very Basic CGPA Calculator
# You can improve the code if you wish, and please share it, so we can benefit from your improvements.

print(
    "This is a CGPA calculator. The program would first ask for the total number of courses you offered in a given semester or session, and then goes to ask for the CU and grade(a,b,c,d, or e) for each particular course.\nNOTE: If you made an error in your input, the program is gonna crash you have to start all over again. So, be carefull in what you press.\n\tSTART")

courses = int(input("What is the total number of courses you offered?\n"))

course_count_raw = 1

# If you want the course codes to be used while asking for their CU and grade, here's a list to store them.
course_codes = []

grade_points = []
total_credit_units = []

for i in range(courses):
    course_count = str(course_count_raw)

    course_count_raw += 1

    course_credit_unit = float(input("How many credit unit is course: " + course_count + "?"))

    total_credit_units.append(course_credit_unit)

    grade = input("What is your grade:")

    if grade == "F" or grade == "f":
        grade = 0
    elif grade == "E" or grade == "e":
        grade = 1
    elif grade == "D" or grade == "d":
        grade = 2
    elif grade == "C" or grade == "c":
        grade = 3
    elif grade == "B" or grade == "b":
        grade = 4
    elif grade == "A" or grade == "a":
        grade = 5
    else:
        print(
            "You inputted a wrong grade. The grade should be any Upper/Lower case alphabet from \"A\" to \"F\". Please restart the program and input the right grade.")
        exit()

    grade_point = grade * course_credit_unit
    grade_points.append(grade_point)

answer = round(sum(grade_points) / sum(total_credit_units), 2)

print("Your CGPA for", courses, "courses is:", answer)

if 4.49 < answer < 5.01:
    print("\nYou got a First Class.")
elif 3.49 < answer < 4.5:
    print("\nYou got a Second Class Honours.")
elif 2.39 < answer < 3.5:
    print("\nYou got a Second Class Lower.")
elif 1.49 < answer < 2.4:
    print("\nYou got a Third Class ")
elif 0.99 < answer < 1.5:
    print("\nYou got a Pass.")
elif 1 > answer:
    print("\nYou Failed.")
else:
    print("\nAn error occured while trying to calculate your grade. Please Restart and Repeat.")
