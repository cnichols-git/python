#!/usr/bin/env python3

# condition statems with if|elif|else 

# once one of the conditions is meet the statemnt will stop

name = 'Chris'
if len(name) >=6:
    print( 'name is long' )
elif len(name) ==5:
    print( 'name is 5 characters long' )
elif len(name) >=4:
    print( 'name is 4 or more' )
else:
    print( 'name is short' )