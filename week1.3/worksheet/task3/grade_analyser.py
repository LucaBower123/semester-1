# Worksheet 1.3: Task 3

# Your code for the overall grade classification

# ask for filename of the student file
filename = input("enter the filename")
# open the file
with open(f"{filename}") as infile:
    data = infile.readlines()
outfile = open(f"{filename}_out.csv", "w")
# read in the data, and for each student calculate their average grade and classification

rows = []
data = [line.strip().split(",") for line in data]
line = 0
len = 0
for row in data:
    rows.append(row)
    len += 1

rows.pop(0)
#print (rows)
means = []
with open(f"{filename}_out.csv", "w") as outfile:
    for item in range (len-1):
        num = 0
        total = 0
        mean = 0
        for i in range(1,13):
            if rows[item][i] != "":
                num = num + 1
                total += int(rows[item][i])
            else:
                mean = total/num
                break
            mean = total/num
                
        if mean >= 70:
            classification = "1"
        elif mean >=60:
            classification = "2:1"
        elif mean >=50:
            classification = "2:2"
        elif mean >=40:
            classification = "3"
        elif mean <40:
            classification = "F"

        outfile.write(f"{rows[item][0]},{mean:.2f},{classification}" + "\n")

# write out this calculated data in the format without a header:
#      student_id,average_grade,classification - replace this with actual value
#      The average grade should be given to 2 decimal places
#      this can be achieved by using the following in an fstring: {variable_name:.2f}


# write this data out to a file named input_file_name + _out.csv - e.g. the input file name 'student_data.csv' -> 'student_data.csv_out.csv'

# You can compare your output files with the 4 example files in example_outfiles folder

