matrix = [
    [1, 2, 3, 4, 5],
    [6, 7, 8, 9, 10],
    [11, 12, 13, 14, 15],
    [16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25],

]
n=5
#Primary diagonal
print(f"---Primary---")
print(
    [matrix[i][i] for i in range(5)]
)
print(f"---Secondary--")
print(
    [matrix[i][n-i-1] for i in range(5)]
)

below_primary_diag = []
for r in range(n):
    for c in range(r+1):
        below_primary_diag.append(matrix[r][c])
print(below_primary_diag)
