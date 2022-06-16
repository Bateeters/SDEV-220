# Brian Teeters
# file location: SDEV-220/M02/caseStudy.py

# This program is for SDEV 220 M02 Lab - Case Study.
# It will accept user input of last and first names as well as GPA.
# It will then test to see if the student made either the Dean's List or Honor Roll.
# Entering "ZZZ" will quit the program.


'''
Write a Python app that will accept student names and GPAs and
test if the student qualifies for either the Dean's List or the Honor Roll. Your app will:

ask for and accept a student's last name.
quit processing student records if the last name entered is 'ZZZ'.
ask for and accept a student's first name.
ask for and accept the student's GPA as a float.

test if the student's GPA is 3.5 or greater and, if so,
print a message saying that the student has made the Dean's List.

test if the student's GPA is 3.25 or greater and, if so,
print a message saying that the studnet has made the Honor Roll.
'''


while True:
    lastName = input("Enter last name please [ZZZ to quit]: ")
    if lastName == 'ZZZ':   # quit
        break

    else:
        firstName = input("Enter first name please: ")
        gpa = float(input("Enter student's GPA: "))
        print("The student", firstName.capitalize(),
              lastName.capitalize(), "has a GPA of", gpa)

        if gpa >= 3.50:
            print(firstName.capitalize(), lastName.capitalize(),
                  "has made the Dean's List.")
        elif 3.50 > gpa >= 3.25:
            print(firstName.capitalize(), lastName.capitalize(),
                  "has made the Honor Roll.")
        else:
            print(firstName.capitalize(), lastName.capitalize(),
                  "did not make the Honor Roll or Dean's List. Keep trying!")
