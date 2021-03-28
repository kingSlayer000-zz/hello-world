#!/bin/python3

import math
import os
import random
import re
import sys
import functools


if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    tempArr = []
    tempInt = int
    resultInt = -100
    
    for i in range(len(arr) - 2):
        for x in range(len(arr) - 2):
            
            tempInt = arr[i][x] + arr[i][x+1] + arr[i][x+2] + arr[i+1][x+1] + arr[i+2][x] + arr[i+2][x+1] + arr[i+2][x+2]
            
            if tempInt > resultInt:
                resultInt = tempInt
                
    print(resultInt)
            
