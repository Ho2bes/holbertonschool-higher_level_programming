#!/usr/bin/python3
space = ""
for i in range(10):
    for j in range(i+1, 10):
        space += "{}{}, ".format(i, j)
space = space[:-2]
print(space)
