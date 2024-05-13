#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'poisonousPlants' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY p as parameter.
#

def poisonousPlants(p):
    stack = []  # Stack to store (plant, days) pairs
    max_days_alive = 0  # Maximum days a plant can be alive
    for plant in p:
        days_alive = 0  # Days the current plant has been alive
        # If the stack is not empty and the current plant is more toxic than the top plant of the stack
        while stack and plant <= stack[-1][0]:
            _, days = stack.pop()  # Remove less toxic plants from the stack
            days_alive = max(days_alive, days)  # Update days_alive with the maximum value
        if not stack:
            days_alive = 0  # If the stack is empty, the current plant will never die
        else:
            days_alive += 1  # Increment days_alive by 1 since the current plant is more toxic than the previous one
        max_days_alive = max(max_days_alive, days_alive)  # Update max_days_alive
        stack.append((plant, days_alive))  # Push the current plant and its days_alive to the stack
    return max_days_alive
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = poisonousPlants(p)

    fptr.write(str(result) + '\n')

    fptr.close()
