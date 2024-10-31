gpa = float(input("What is your GPA? Enter: ")) #asks user what their GPA is

if gpa == 4.0:
    print("Highest Honors!") #They have Highest Honors if they have a 4.0 GPA
elif gpa >= 3.9:
    print("High Honors!") #They have High Honors if their GPA is 3.9 and above
elif gpa >= 3.8:
    print("Honors") #They have Honors with a 3.8 GPA and above 

elif gpa >= 3.5:
 #A 3.5 or  more means its okay    print("Good Standing")
 #Below a 3.5 needs improving    print("Needs Improvement")



num1 = int(input("What is your grade level? Enter Number: "))  # Asking the user what grade they are in
prerequisites = input("Have you completed course prerequisites? (yes/no) ")  # Asking about course completion

if num1 >= 10 and prerequisites.lower() == "yes":  # Check if grade level is 10 or higher and prerequisites are met
    print("Eligible for advanced course enrollment.") 
elif num1 < 10 and prerequisites.lower() == "yes":  # Check if grade level is lower than 10 and prerequisites are met
    print("Eligible for basic course enrollment.")
else:  # If they have not completed their prerequisites or are in a lower grade level without prerequisites
    print("Please complete prerequisites and reapply next year.")