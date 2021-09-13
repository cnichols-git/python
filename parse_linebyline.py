#!/usr/bin/python3

##
# cnichols - this should take a file and pull out some of the data with certain conditions

# for practice - define some vars and interact with user 
# Get some input from the user.
name = input("Welcome, \n May I please have your name? \n")

# check for length 
num_length = len(name) 

# if input is 10 or less print it out
if num_length <= 11:
    print("Hey",name, "let's parse a file")

# read from a file and outpiut each line as a string
#file = open("/home/chris/Documents/test_logs", "r")

#with open('/home/chris/Documents/test_logs') as file:
    # do stuff with file
    # := whalrus assigns value to a variable as a part of am expression
with open('/home/chris/Documents/test_logs', 'r', encoding='UTF-8') as file:
    while (line := file.readline().rstrip()):
        print(line, "test")

