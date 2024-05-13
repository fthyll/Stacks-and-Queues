#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'isBalanced' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
def isBalanced(s):
    stack = []
    # Define opening and closing brackets
    open_brackets = {'(', '[', '{'}
    close_brackets = {')', ']', '}'}
    # Iterate through the string
    for char in s:
        # If the character is an opening bracket, push it onto the stack
        if char in open_brackets:
            stack.append(char)
        # If the character is a closing bracket
        elif char in close_brackets:
            # If the stack is empty, it means there's a closing bracket without a corresponding opening bracket
            if not stack:
                return "NO"
            # Pop the top element from the stack
            top = stack.pop()
            # Check if the top of the stack matches the corresponding opening bracket for the current closing bracket
            if (char == ')' and top != '(') or (char == ']' and top != '[') or (char == '}' and top != '{'):
                return "NO"
    # If the stack is empty after iterating through the string, it means all brackets are balanced
    return "YES" if not stack else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for _ in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
