#Luke is daydreaming in Math class. He has a sheet of graph paper with  rows and  columns, and he imagines that there is an 
#army base in each cell for a total of  bases. He wants to drop supplies at strategic points on the sheet, marking each drop 
#point with a red dot. If a base contains at least one package inside or on top of its border fence, then it's considered to 
#be supplied. 
#Given  and , what's the minimum number of packages that Luke must drop to supply all of his bases?

import math
import os
import random
import re
import sys

def gameWithCells(n, m):
    return (m//2+m%2)*(n//2+n%2)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = gameWithCells(n, m)

    fptr.write(str(result) + '\n')

    fptr.close()

