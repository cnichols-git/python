#!/bin/python

## cnichols - take a sting and reverse it, then print it

# sys module caputers the string typed after the file name
import sys

value1 = sys.argv[1]

# write your solution here
output = value1[::-1]
print(output)

var = "This is a line of text"
output = var[::-1]
print(output)