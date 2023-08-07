# Diagonal Difference
# By https://www.hackerrank.com/jessicaccp on Aug 6, 2023

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    primary = 0
    secondary = 0
    
    for a in range(0, len(arr)):
        for b in range(0, len(arr[0])):
            if a == b:
                primary += arr[a][b]
            if a + b == len(arr[0]) - 1:
                secondary += arr[a][b]
                
    output = primary - secondary
    if output < 0:
        output *= -1
        
    return output
                

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
