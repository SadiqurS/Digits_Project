"""
Sadiqur. Sakib
period #8
Digits Project
"""


from Digits_Lib_Sadiqur_P8 import *
user = (input("enter the digits:"))#Asks the user what digits they want to print
size = int(input("enter the size:"))#asks the user what the size of each digit should be
for i in range(len(user)):#looks through the length of what the user has
    check((int(user[i])),(size))#Draws the digits and its size based on what the user asked for
    space(size)#creates a spcae between each digit



exitonclick()