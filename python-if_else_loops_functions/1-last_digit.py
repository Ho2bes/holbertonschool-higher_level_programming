#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if number < 0:
    last1 = number % -10
else:
    last1 = number % 10

if last1 > 5:
    print("Last digit of", number, "is", last1, "and is greater than 5")
elif last1 == 0:
    print("Last digit of", number, "is", last1, "and is 0")
else:
    print("Last digit of", number, "is", last1, "and is less than 6 and not 0")
