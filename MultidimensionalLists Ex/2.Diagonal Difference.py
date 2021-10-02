import sys
from io import StringIO


test_input1 = """3
11 2 4
4 5 6
10 8 -12
"""
test_input2 = """4
-7 14 9 -20
3 4 9 21
-14 6 8 44
30 9 7 -14
"""


#sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)



def read_matrix():
    n = int(input())
    #n,m = map(int, input().split(', '))

    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(' ')]
        matrix.append(row)

    return matrix

matrix = read_matrix()

n = len(matrix)
primary_diagnonal = [matrix[i][i] for i in range(n)]
secondary_diagnonal = [matrix[i][n-i-1] for i in range(n)]
print(abs(sum(primary_diagnonal)-sum(secondary_diagnonal)))



