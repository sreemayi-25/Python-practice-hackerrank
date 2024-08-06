#!/bin/python3

import math
import os
import random
import re
import sys
from itertools import chain
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

matrix_decoded="".join(list(chain.from_iterable(zip(*matrix))))
print(re.sub(r"\b\W+\b"," ",matrix_decoded))
