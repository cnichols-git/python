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

##
# file handeling

# Python has several functions for creating, reading, updating, and deleting files
# The default mode is 'rt' (open for reading text)
# open a file
file = open("/home/chris/Documents/test_logs", "r")
print("Below is the output from logs:\n",file.read())


# same as above
#with open("/home/chris/Documents/test_logs", "r") as infile:
    #reader = csv.reader(infile, delimeter=",")
    #header = next(reader)
    #print(header)

# create a file
# outfile = open("", w)