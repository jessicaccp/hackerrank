# Plus Minus
# By https://www.hackerrank.com/jessicaccp on Aug 5, 2023

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    total = float(len(arr))
    positive = 0
    negative = 0
    zero = 0
    
    for number in arr:
        if number == 0:
            zero += 1
        elif number > 0:
            positive += 1
        else:
            negative += 1
            
    print("{:.6f}".format(positive / total))
    print("{:.6f}".format(negative / total))
    print("{:.6f}".format(zero / total))
    

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)
