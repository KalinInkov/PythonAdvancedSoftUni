import sys
from io import StringIO


test_input1 = """3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
"""


sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)


def read_matrix():
    #n = int(input())
    n,m = map(int, input().split(', '))

    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(' ')]
        matrix.append(row)

    return matrix

matrix = read_matrix()
# new_matrix = []

n = len(matrix)
m = len(matrix[0])

column_sum = [0]*m

# for r in range(n):
#     for c in range(m):
#         value = matrix[r][c]
#         column_sum[c]+=value

for c in range(m):
    for r in range(n):
        value = matrix[r][c]
        column_sum[c]+=value



# print(matrix)
# print('______________')
# [print(x) for x in matrix]
# print('-------------------------')
[print(x) for x in column_sum]
# print(new_matrix)



