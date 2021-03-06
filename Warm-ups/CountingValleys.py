#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

# if sealevel reached and user is going up, valley was passed
# old comment was if sea level reached and user previously was downhill
def countingValleys(steps, path):
  valley = 0
  level = 0
  # prev = 0
  for i in range(steps):
    if path[i]=='U':
      level+=1
    if path[i]=='D':
      level-=1
    if path[i]=='U' and level==0:
      valley+=1
    # if level >= 0 and prev < 0:
    #     valley += 1
    # prev = level
  return valley
        

if __name__ == '__main__':
  fptr = open(os.environ['OUTPUT_PATH'], 'w')

  steps = int(input().strip())

  path = input()

  result = countingValleys(steps, path)

  fptr.write(str(result) + '\n')

  fptr.close()
