#!/bin/python3

##
# cnichols - doing things with strings

#------------#

from os import read


# l='Name = stack words'
# pos=l.index(':' or '=')  

# pos = max(l.find(':'), l.find('='), 0)      
# print(l[pos:].strip())    

# print(l[max(l.find(':'),l.find('='),0):].strip())
#--------------- Breakdown
# max -> highest of values; find returns -1 if it isn't there.
#        using a 0 at the end means if ':'/'=' aren't in the string, print the whole thing.
# l.find(),l.find() -> check the two characters, using the higher due to max()
# l[max():] -> use that higher value until the end (implied with empty :])
# .strip() -> remove whitespace

#------------#

# file = open('/home/chris/Documents/test_logs', "r")
# data = file.read().split(":")
# for i in data:
#     print(data)

# looking for a string 

# declare what we are looking for
s = "session opened"
with open("/home/chris/Documents/test_logs", "r") as f:
    for line in f:
        var = line.find('opened')
        if var != -1:
            print(line)