"""
Sadiqur. Sakib
period #8
Digits Project
"""

from turtle import *


def movefd(x):
    pu()
    fd(x)
    pd()


def go(p):# the postion of wher turtle should go after drawing the letters
    pu()
    goto(p)
    pd()
    setheading(0)


def zero(x): # the function to drar the digit 0
    for i in range(2):
        fd(x)
        rt(90)
        fd(2 * x)
        rt(90)


def one(x): # the function to drar the digit 1
    start = pos()
    movefd(x)
    rt(90)
    fd(2 * x)
    go(start)


def two(x): # the function to drar the digit 2
    start = pos()
    fd(x)
    rt(90)
    fd(x)
    rt(90)
    fd(x)
    lt(90)
    fd(x)
    lt(90)
    fd(x)
    go(start)


def three(x): # the function to drar the digit 3
    start = pos()
    fd(x)
    rt(90)
    fd(x)
    rt(90)
    fd(x)
    bk(x)
    lt(90)
    fd(x)
    rt(90)
    fd(x)
    go(start)


def four(x): # the function to drar the digit 4
    start = pos()
    movefd(x)
    rt(90)
    fd(2 * x)
    go(start)
    rt(90)
    fd(x)
    lt(90)
    fd(x)
    go(start)


def five(x): # the function to drar the digit 5
    start = pos()
    fd(x)
    bk(x)
    rt(90)
    fd(x)
    lt(90)
    fd(x)
    rt(90)
    fd(x)
    rt(90)
    fd(x)
    go(start)


def six(x):# the function to drar the digit 6
    start = pos()
    rt(90)
    fd(2 * x)
    lt(90)
    fd(x)
    lt(90)
    fd(x)
    lt(90)
    fd(x)
    go(start)
    fd(x)
    go(start)


def seven(x):# the function to drar the digit 7
    start = pos()
    fd(x)
    rt(90)
    fd(2 * x)
    go(start)


def eight(x):# the function to drar the digit 8
    start = pos()
    for i in range(4):
        fd(x)
        rt(90)
    for i in range(2):
        fd(x)
        rt(90)
        fd(2 * x)
        rt(90)


def nine(x):# the function to drar the digit 9
    start = pos()
    fd(x)
    rt(90)
    fd(2 * x)
    rt(90)
    fd(x)
    go(start)
    for i in range(4):
        fd(x)
        rt(90)
    go(start)


def space(x):#the function for spacing between each digit
    movefd(1.5*x)


def check(i, x):
    if (i == 0):
        zero(x)
    elif (i == 1):
        one(x)
    elif (i == 2):
        two(x)
    elif (i == 3):
        three(x)
    elif (i == 4):
        four(x)
    elif (i == 5):
        five(x)
    elif (i == 6):
        six(x)
    elif (i == 7):
        seven(x)
    elif (i == 8):
        eight(x)
    elif (i == 9):
        nine(x)
