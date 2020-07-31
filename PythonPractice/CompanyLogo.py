#!/bin/python3

import math
import os
import random
import re
import sys

import collections

if __name__ == '__main__':
    s = sorted(input())

    sCount = collections.Counter (s)
    #print (sCount)

    results = (sCount.most_common(3))
   
    for i in results:
        print (*i)



