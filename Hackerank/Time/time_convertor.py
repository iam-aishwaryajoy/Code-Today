#!/bin/python3

import math
import os
import random
import re
import sys


def timeConversion(s):
    time = list(s)
    cordinate = time[-2:]
    time = time[:-2]
    if cordinate == ['A','M']:
        if (time[0]+time[1])=='12':
            time[0] = '0'
            time[1] = '0'
        result = ''.join(time)
    else:
      real = str(int(time[0] + time[1])  + 12)
      if real == '24':
        result = ''.join(time)
      else:
        time[0] = list(real)[0]
        time[1] = list(real)[1]
        result = ''.join(time)
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()

