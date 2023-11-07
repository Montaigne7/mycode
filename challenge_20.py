#!/usr/bin/env python3

# create a list called wordbank
wordbank= ["indentation", "spaces"]

# create a list of tlg students
tlgstudents= ['Albert', 'Anthony', 'Brenden', 'Craig', 'Deja', 'Elihu', 'Eric', 'Giovanni', 'James', 'Joshua', 'Maria', 'Mohamed', 'PJ', 'Philip', 'Sagan', 'Suchit', 'Meka', 'Trey', 'Winton', 'Xiuxiang', 'Yaping']

# add the integer 4 to the wordbank list
wordbank.append(4)

# calculate the size of the list
length = len(tlgstudents)

# ask user input for a number
num = input(print("Please enter a number between 1 and", length, ":"))

# change num variable from string to integer
num = int(num)

# convert from human readable number to slice format
num = num - 1

# randomly generate number between 0 and 20 and set as variable num
#import random
#num = random.randrange(0, length)

# slice list of tlgstudents using num variable from user input
student_name = tlgstudents[num]

#display the the requested output from lists
print(student_name, "always uses", wordbank[2], wordbank[1], "to indent.")


