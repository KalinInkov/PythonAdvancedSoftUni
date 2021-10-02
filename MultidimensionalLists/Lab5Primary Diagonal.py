import sys
from io import StringIO


test_input1 = """3
11 2 4
4 5 6
10 8 -12
"""
test_input2 = """3
1 2 3
4 5 6
7 8 9
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
# new_matrix = []

n = len(matrix)
# m = len(matrix[0])
#[print(z) for z in matrix]
print(
    sum([matrix[i][i] for i in range(n)])
)
