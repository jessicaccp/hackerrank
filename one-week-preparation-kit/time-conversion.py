# Time Conversion
# By https://www.hackerrank.com/jessicaccp on Aug 5, 2023

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    if s[0:2] == "12" and s[-2:] == "AM":
        s = "00" + s[2:]
    elif s[0:2] == "12" and s[-2:] == "PM":
        pass
    elif s[-2:] == "PM":
        s = str(int(s[0:2]) + 12) + s[2:]
        
    s = s[:-2]
    return s
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
