#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
     str= input()
     s=Counter(sorted(str))
     for i in s.most_common(3):
         print(*i)
