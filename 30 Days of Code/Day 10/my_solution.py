import math
import os
import random
import re
import sys
import functools

def tenBaseToTwoBase(numInt):
    result = ""
    
    while numInt > 0:
        if numInt % 2 == 0:
            result = "0" + result
        elif numInt == 0:
            break
        else:
            result = "1" + result
        numInt = int(numInt / 2)   
    
    return result
        
        
if __name__ == '__main__':
    n = int(input())
    
    result = tenBaseToTwoBase(n)
    
    list1 = result.split("0")
    list1 = list(filter(None, list1))

    max1 = ""
    
    max1 = functools.reduce(lambda a, b : a if len(a) > len(b) else b, list1)
    
    print(len(max1))
    
