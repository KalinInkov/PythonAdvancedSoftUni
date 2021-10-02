# ll = [1,2,3,4,5,6,7]
#
# print(ll[2])
#
#
# list_of_string = [
#     'Guz1',
#     'Guzi2',
#     'Guzi3'
# ]
#
# list_of_list = [
#     [1,2,3],
#     [2,3,4],
#     [3,4,5]
# ]
#
# print(list_of_string)
#
# print(list_of_list)


n=5 #rows
m=4 # columns

matrix_of_zeroes = []
for _ in range(n):
    row=[0]*m
    matrix_of_zeroes.append(row)

for row in matrix_of_zeroes:
    print(row)

matrix_of_zeroes1 = [[0]*n for _ in range(n)]
print([[0]*n for _ in range(n)])