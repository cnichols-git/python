#!/usr/bin/env python3

# simple loop that counts to 4, but starting at 1
"""
count = 1
while count <= 4:
    print( 'looping' )
    count += 1
"""

# print out even numbers from 0 - 10
count = 0
while count < 10:
    if count % 2 == 0:
        count += 1
        continue
    print(f"We're counting odd numbers: {count}")
    count += 1
