#!/bin/python3

# cnichols - 

def missing_char(str, n):
  front = str[:n]   # up to but not including n
  back = str[n+1:]  # n+1 through end of string
  return front + back
print(missing_char("kitten", 1))

def hello():
    print("hello")

hello()

# making a sting that is printed as an array
s = "this is a string"
front = s[:5]
back = s[9+1:]
print(front + back)

s = "this is a string"
front = s[:5]
back = s[9+1:]
name = front.strip() + back.strip()
print(name)