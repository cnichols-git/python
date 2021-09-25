#!/bin/python3

##
# cnichols - doing things with strings

# looking for a string 
with open("/home/chris/Documents/test_logs", "r") as file:
    for line in file:
        var = line.find('opened')
        if var != -1:
            alert = line.split()
            # print(alert)
            print(alert[6], alert[7], "By user: ", alert[10], "Date: ", alert[0], alert[1])
