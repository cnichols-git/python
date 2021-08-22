#!/usr/bin/env python3

##
# cnichols - this should take a file and pull out some of the data with certain conditions

# for practice - define some vars and interact with user 
# Get some input from the user.
name = input("Welcome, \n May I please have your name? \n")

# check for and clean user input 
num_length = len(name) 

if num_length <= 11:
    print("Hey",name, "let's parse a file")