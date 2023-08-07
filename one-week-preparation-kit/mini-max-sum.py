# Mini-Max Sum
# By https://www.hackerrank.com/jessicaccp on Aug 5, 2023

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    first = True
    
    for a in range(0, len(arr) - 3):
        for b in range(a + 1, len(arr) - 2):
            for c in range(b + 1, len(arr) - 1):
                for d in range(c + 1, len(arr)):
                    if first:
                        mini = arr[a] + arr[b] + arr[c] + arr[d]
                        maxi = arr[a] + arr[b] + arr[c] + arr[d]
                        first = False
                    else:
                        if arr[a] + arr[b] + arr[c] + arr[d] < mini:
                            mini = arr[a] + arr[b] + arr[c] + arr[d]
                        if arr[a] + arr[b] + arr[c] + arr[d] > maxi:
                            maxi = arr[a] + arr[b] + arr[c] + arr[d]
                            
    print(mini, maxi)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
