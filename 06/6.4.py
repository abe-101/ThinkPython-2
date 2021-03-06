#!/usr/bin/python3

'''
Andrea Cocco 2020
Chapter 6 Exercise 4 from the book:
    
Think Python, 2nd Edition
by Allen Downey
http://thinkpython2.com

Write a function called is_power that takes parameters a and b
and returns True if a is a power of b.
Note: you will have to think about the base case.
'''
def is_power(a, b):
    """Check if a is a power of b"""
    if  a > b:
        if a%b == 0:
            c = a/b 
            return is_power(c, b)
        else:
            return a%b == 0 # base case
    else:
        return a == b # base case 

def ask_user():
    """Prompt the user to enter the two numbers to check"""
    numa = input('Insert a number A to check if it is a power of a number B.\n')
    numa = int(numa)
    numb = input('Insert a number B.\n')
    numb = int(numb)
    print(is_power(numa, numb))
    quit()

def quit():
    """Prompt the user to choose if he wants to quit or not"""
    q = input('Do you want to quit? [y/n]\n')
    if q == 'y':
        print('Goodbye')
    else:
        ask_user()

ask_user()
