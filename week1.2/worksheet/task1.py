# Worksheet 1.2: Task 1 Solution
import sys

try:
    grade = int(input("enter a grade in the range 0 to 100: "))
    if 100 < grade or grade < 0:
        sys.exit("Error: Grade must be an integer between 0 and 100")
    if grade <= 39:
        result = "Fail"
    elif grade <= 69:
        result = "Pass"
    else:
        result = "Distinction"
    print (f"{grade} is a {result}")
except:
    sys.exit("Error: Grade must be an integer between 0 and 100")
