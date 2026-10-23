# Worksheet 1.2: Task 2 Solution
import sys
from util import read_numbers
try:
    numbers = read_numbers()
except:
    sys.exit("Error: no numbers provided")

length = len(numbers)
if length == 0:
    sys.exit("Error: no numbers provided")
print (length)

numbers.sort()
print (numbers)
min = min(numbers)
max = max(numbers)
mean = sum(numbers) / len(numbers)

if length != 1:
    if length%2 == 1:
        median = numbers[((length + 1)//2)-1]
    else:
        num1 = numbers[(length//2)-1]
        num2 = numbers[(length//2)]
        median = (num1 + num2)/2

    print (f"Minimum = {min}")
    print (f"Maximum = {max}")
    print (f"Mean = {mean}")
    print (f"Median = {median}")
else:
    print (f"Minimum = {numbers[0]}")
    print (f"Maximum = {numbers[0]}")
    print (f"Mean = {numbers[0]}")
    print (f"Median = {numbers[0]}")

