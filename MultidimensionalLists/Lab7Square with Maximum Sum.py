import sys
from io import StringIO


test_input1 = """3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
"""

test_input2 = """2, 4
10, 11, 12, 13
14, 15, 16, 17
"""



sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)


def read_matrix():
    #n = int(input())
    n,m = map(int, input().split(', '))

    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)

    return matrix

matrix = read_matrix()
max_square_matrix = []
sums = []
n = len(matrix)
m = len(matrix[0])

for r in range(n-1):

     for c in range(m-1):
       current_sum = matrix[r][c]+\
                   matrix[r][c+1]+\
                   matrix[r+1][c]+\
                   matrix[r+1][c+1]

       sums.append((
           current_sum,
           r,
           c
       ))
print(sums[0][0])

max_sum = 0
for p in range(len(sums)):
    current_sum = sum(sums[int(p)][0])
    if current_sum>max_sum:
        max_sum=current_sum

print(max_sum)




# [print(x) for x in matrix]