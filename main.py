"""
Fizz Buzz
=========

variable representing your maximum number

make a for loop that goes from 1 to your max number (including your max number)

print each number UNLESS the number is a multiple of 3 or 5

if the number is a multiple of 3 and not 5, print "fizz" instead of the number

if the number is a multiple of 5 and not 3, print "buzz" instead of the number

if the number is a multiple of both 3 and 5, print "fizzbuzz" instead of the number
"""

max_number = 15

# YOUR CODE HERE


for i in range (1, max_number+1) :
    if i % 3 == 0 and i % 5 == 0 :
        print ("fizzbuzz")
    elif i % 3 == 0 :
        print ("fizz")
    elif i % 5 == 0 :
        print ("buzz")
    else:
        print (i)


"""
Example: if max_number is 15, here's what will print out:

1
2
fizz
4
buzz
fizz
7
8
fizz
buzz
11
fizz
13
14
fizzbuzz

"""