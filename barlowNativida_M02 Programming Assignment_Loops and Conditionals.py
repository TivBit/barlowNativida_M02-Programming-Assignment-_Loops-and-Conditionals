# -*- coding: utf-8 -*-
"""
Created on %(Date: 29 Jan 2023)s

@author: %(Tiv Barlow)s
Python Version 3.11.1
SDEV 220 Spring 2023
Assignment: M02 Programming Assignment - Loops and Conditionals

"""

#4.1 START ===============================
secret = 6
guess = 3

if guess < secret: 
    print("too low")
    
elif guess > secret:
    print("too high")
    
else:
    print("just right")
#4.1 END   ===============================

print()

#4.2 START ===============================
small = True
green = True

if small: 
    if green: 
        print("It's a pea.")
    else:
        print("It is a cherry.")
        
if green:
    if green:
        print("It is a pea, or a watermelon.")
    else:
        print("It is a cherry, or a pumpkin.")
#4.2 END   ===============================

print()

#6.1 START ===============================
#Use a for loop to print the values of the list [3, 2, 1, 0].

for x in range(3, -1, -1):
    print(x)
#6.1 END   ===============================

print()


#6.2 START ===============================
#Assign the value 7 to the variable guess_me, and the value 1 to the variable
#number. Write a while loop that compares number with guess_me. Print 'too low'
#if number is less than guess me. If number equals guess_me, print 'found it!'
#and then exit the loop. If number is greater than guess_me, print 'oops' and
#then exit the loop. Increment number at the end of the loop.

guess_me = 7
number = 8


while guess_me < number:
    if guess_me < number:
        print("too low")
        return
        break
    elif guess_me == number:
        print("found it!")
        break
    if guess_me > number:
        print("oops")
        break
    
#6.2 END   ===============================


print()


#6.3 START ===============================
#Assign the value 5 to the variable guess_me. Use a for loop to iterate a
#variable called number over range(10). If number is less than guess_me,
#print 'too low'. If it equals guess_me, print found it! and then break out
#of the for loop. If number is greater than guess_me, print 'oops' and then
#exit the loop.
print()
print()

i = 0
guess_me = 5
number = input("Guess a number between 1-10: ")



for number in range(11):
    if guess_me < number:
        print("too low")
    if guess_me == number:
        print("found it!")
        break
    else:
        print("oops")
        break
i=+1

    
    





    





