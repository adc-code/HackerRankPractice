#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the solve function below.
def solve(s):
    newS = []
    count = 0;
    nextC = False;
    for c in s:
        newC = c
        if c == ' ':
            nextC = True
        elif nextC == True or count == 0:
            newC = c.upper ()
            nextC = False
        
        newS.append (newC)
        count += 1

    return ''.join (newS)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()


