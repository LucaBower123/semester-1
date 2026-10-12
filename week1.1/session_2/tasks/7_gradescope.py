# To test that you can successfully download a file and upload it to gradescope

# You are going to write a very simple program:

# Ask a user to enter two numbers (one per input)
# multiply those numbers together
# print out the result

try:
    number_1 = int(input("enter a number"))
    number_2 = int(input("enter a number"))
    number_3 = number_1*number_2
    print(number_3)
except:
    print("That is not a number")


# There is an extra point available for validating that they entered numbers!
# Add to your code so that if they entered something other than an integer it prints
# 'That is not a number' and exits.

# Download your file, and upload it to the 'Week 1 Session 2 - Practice Upload' task on Minerva.
# You will get some feedback - ensure you are passing the tests!