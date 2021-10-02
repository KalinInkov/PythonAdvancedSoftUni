import sys
from io import StringIO


test_input1 = """3
ABC
DEF
X!@
!
"""
test_input2 = """4
asdd
xczc
qwee
qefw
4
"""


sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)


def read_matrix():
    n = int(input())
    #n,m = map(int, input().split(', '))

    matrix = []
    for _ in range(n):
        row = input()
        matrix.append(row)

    return matrix

matrix = read_matrix()

symbol = input()

n = len(matrix)
m = len(matrix[0])
is_symbol=False

row, col = None, None
# for r in range(n):
#     if is_symbol:
#         break
#     for c in range(m):
#         if  matrix[r][c] ==symbol:
#             row, cow = r, c
#             is_symbol=True
#             print(f'({r}, {c})')
#             break

for r in range(n):
    if symbol in matrix[r]:
        row = r
        col = matrix[r].index(symbol)

        is_symbol=True
        print(f'({r}, {col})')
        break




if not is_symbol:
    print(f"{symbol} does not occur in the matrix")

#print(matrix)
# new_matrix = []

# n = len(matrix)
# m = len(matrix[0])