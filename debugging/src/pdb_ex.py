"""
Debug Example
"""
import sys
import pdb
from random import choice

random1 = list(range(1,12))
random2 = list(range(1,12))

while True:
    print("To exit this game type 'exit'")
    pdb.set_trace()
    num1 = choice(random1)
    num2 = choice(random2)
    answer = int(input("What is {0} times {1}? ".format(num1, num2)))

    if answer == 'exit':
        print("Now exiting the game!")
        sys.exit()
    elif answer == num1 * num2:
        print("Correct!")
    else:
        print("Wrong!")
