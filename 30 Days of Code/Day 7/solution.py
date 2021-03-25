import math
import os
import random
import re
import sys

def listToString(s):
    
    str1 = ""
    
    for ele in s:
        str1 += ele
        str1 += " "
        
    return str1

if __name__ == '__main__':
    n = int(input())

    arr = list(map(str, input().rstrip().split()))
    
    arr.reverse()
  
    text = listToString(arr)
    
    print(text)
