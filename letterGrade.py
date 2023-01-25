# dictionary, which will hold all grades and subjects
grades = {}

def letter_grade(grade):
    """Calculates grade based on number given."""
    if grade >= 90.0:
        print("Your grade is an A. Great job!")
    elif grade < 90.0 and grade >= 80.0:
        print("Your grade is a B! Great job!")
    elif grade < 80.0 and grade >= 70.0:
        print("Your grade is a C. That's ok, as long as you tried your best. \n If you want to increase your grade, try using online resources or asking for help with dificult subjects.")
    elif grade < 70.0 and grade >= 60.0:
        print("Your grade is a D. Try asking for help or practicing online if you wish to improve your grade. You can do it!")
    elif grade < 60.0:
        print("Sorry, you got an F. You may need to retake this class. \n If you need this class to graduate, please remember to study. There are many helpful resources online such as Kahn Academy or Quizlet to help you. \n Your teachers too. You can do it!")
    
# Main part of program. 
print("Welcome to Gradesuite! Use this program to determine your letter grade and the average of all your grades! \n The first step is entering all of your grades,so let's begin!")
# Calculating all of the grades
active = True
while active:
    sub = input("What is the subject for the class? ")
    num = input("Enter your grade: ")
    try:
        num = float(num)
    except ValueError:
        print("Invalid response. Please enter a number.")
        continue
    letter_grade(num)
    again = input("Would you like to calculate another grade? Enter Y or N: ").upper()
# Showing the user their grades, and exiting with average when selecting no.
    if again == "Y":
        grades[sub] = num
        print("Grades added: ")
        for k, v in grades.items():
            print(f"{k}: {v}")
        continue
    else:
        grades[sub] = num
        print("Ok, goodbye!")
        print("Here are your grades: ")
        for k, v in grades.items():
            print(f"{k}: {v}")
            total = sum(grades.values())
        print(f"Your average is: {total / len(grades.values())}")    
        active = False
