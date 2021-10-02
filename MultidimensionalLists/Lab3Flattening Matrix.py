import sys
from io import StringIO


test_input1 = """2
1, 2, 3
4, 5, 6
"""
test_input2 = """3
10, 2, 21, 4
5, 20, 41, 9
6, 2, 4, 99
"""

#sys.stdin = StringIO(test_input1)
sys.stdin = StringIO(test_input2)


def read_matrix():
    n = int(input())
    # n,m = map(int, input().split(', '))

    matrix = []
    for _ in range(n):
        row = [int(x) for x in input().split(', ')]
        matrix.append(row)

    return matrix

matrix = read_matrix()
new_matrix = []

for row in matrix:
    new_matrix.extend(row)

# print(                            За мен лично това по-малко разбираем вариянт също
#     [x for row in matrix for x in row]
# )

#print(matrix)
print(new_matrix)



