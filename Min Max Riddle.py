#!/bin/python3

import math
import os
import random
import re
import sys

def riddle(arr):
    n = len(arr)
    
    # Step 1: Initialize arrays to store the left and right boundaries of each element
    left_boundary = [-1] * n
    right_boundary = [n] * n
    
    # Step 2: Use monotonic stack to find the left boundaries
    stack = []
    for i in range(n):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            left_boundary[i] = stack[-1]
        stack.append(i)
    
    # Clear the stack for next usage
    stack.clear()
    
    # Step 3: Use monotonic stack to find the right boundaries
    for i in range(n - 1, -1, -1):
        while stack and arr[stack[-1]] >= arr[i]:
            stack.pop()
        if stack:
            right_boundary[i] = stack[-1]
        stack.append(i)
    
    # Step 4: Calculate the answer for each window size
    ans = [0] * (n + 1)
    for i in range(n):
        length = right_boundary[i] - left_boundary[i] - 1
        ans[length] = max(ans[length], arr[i])
    
    # Step 5: Fill in any missing answers
    for i in range(n - 1, 0, -1):
        ans[i] = max(ans[i], ans[i + 1])
    
    # Step 6: Return the final result
    return ans[1:]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = riddle(arr)

    fptr.write(' '.join(map(str, res)))
    fptr.write('\n')

    fptr.close()
