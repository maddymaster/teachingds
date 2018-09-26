names = input("Enter your Student names separated by commas: ").title().split(",")
assignments = input("Enter assignment counts separated by commas: ").split(",")
grades = input("Enter grades separated by commas: ").split(",")


message = "Hi {}, \n\n This is a reminder that you have {} assignments left to before you can graduate. You're current grade is {} and can increase to {} if you submit all assignments before the due date.\n\n"

for name, assignment, grade in zip(names, assignments, grades):
    print(message.format(name, assignment, grade, int(grade)+ int(assignment)*2))

print(names)