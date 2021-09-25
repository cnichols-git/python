#!/bin/python3

##
# cnichols - doing things with strings

# looking for a string 
with open("/home/chris/Documents/test_logs", "r") as f:
    for line in f:
        var = line.find('opened')
        if var != -1:
            print(line)