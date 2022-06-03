# fibonachi number
from tkinter import N


def fib(n):
    if n <= 1:
        return 1
    else:
        return fib (n-1) + fib (n-2)

for i in range (10):
    print (fib(i))

# factorial
def factorial (n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

n=10
print ("factorial of",n, "is", factorial(n))

#the Hanoi game
disc = [0,0,0] # binary system to represent the pilars in Hanoi 2^x = size of disc, x < 10

for i in range (n):
    disc[0] += pow(2, i)
print(disc)
def moveDisc (fr, to):
    for i in range (10):
        if disc[fr] & pow(2,i) > 0:
            disc[fr] -= pow(2,i)
            disc[to] += pow(2,i)
            print (disc)
            return
def moveHanoi (fr, to, lv): # move lv discs from disc[fr] to disc[to] (with other as spare)
    sp = 3 - fr - to
    if lv == 1:
         moveDisc (fr, to)       
    else:
        moveHanoi (fr, sp, lv-1)
        moveDisc (fr, to)
        moveHanoi (sp, to, lv-1)

moveHanoi(0,1,2)