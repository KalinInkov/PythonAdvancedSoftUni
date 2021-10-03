import sys
from io import StringIO

test_input1 = """5 6
SoftUni
"""
test_input2 = """1 4
Python
"""

sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)

rows,cols = [int(x) for x in input().split()]
word = input()

matrix = []
word_idx = 0


for row in range(rows):
    matrix.append([None]*cols)
    for col in range(cols):
        if row%2==0:
            matrix[row][col]=word[word_idx]

        else:
            matrix[row][cols-1-col]=word[word_idx]
        word_idx=(word_idx+1)%len(word)
for el in matrix:
    print(''.join(el))



