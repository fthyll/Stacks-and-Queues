#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'largestRectangle' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY h as parameter.
#

def largestRectangle(h):
    stack = []
    max_area = 0
    i = 0
    
    while i < len(h):
        if not stack or h[i] >= h[stack[-1]]:
            stack.append(i)
            i += 1
        else:
            top_index = stack.pop()
            if stack:
                width = i - stack[-1] - 1
            else:
                width = i
            area = h[top_index] * width
            max_area = max(max_area, area)
    
    while stack:
        top_index = stack.pop()
        if stack:
            width = i - stack[-1] - 1
        else:
            width = i
        area = h[top_index] * width
        max_area = max(max_area, area)
    
    return max_area

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    h = list(map(int, input().rstrip().split()))

    result = largestRectangle(h)

    fptr.write(str(result) + '\n')

    fptr.close()
