import sys
from io import StringIO

test_input1 = """3 4
A B B D
E B B B
I J B B
"""

test_input2 = """2 2
a b
c d
"""
test_input3 = """5 4
A A B D
A A B B
I J B B
C C C G
C C K P
"""


# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)

def getsubmat(mat,start_row,end_row,start_col,end_col):
  return [i[start_col:end_col] for i in mat[start_row:end_row] ]

def read_matrix():
    # n = int(input())
    n, m = map(int, input().split(' '))

    matrix = []
    for _ in range(n):
        row = [x for x in input().split(' ')]
        matrix.append(row)

    return matrix


matrix = read_matrix()

n = len(matrix)
m = len(matrix[0])
counter = 0
current_row = 0
current_col = 0

a=[]
for r in range(n-1):
    for c in range(m-1):
        a = [matrix[r][c],matrix[r+1][c],matrix[r][c+1],matrix[r+1][c+1]]
        if matrix[r][c]==matrix[r+1][c]==matrix[r][c+1]==matrix[r+1][c+1]:
            counter+=1
        print(a)

print(counter)












