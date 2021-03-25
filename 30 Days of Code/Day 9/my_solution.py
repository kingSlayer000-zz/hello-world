import math
import os
import random
import re
import sys
import functools


def factorial(x):
    numList = range(1, x+1)
    
    result = functools.reduce(lambda a, b : a * b, numList)
    
    return result

num = int(input())

print(factorial(num))
