ll = [[7, 1, 3, 3, 2, 1],
      [1, 3, 9, 8, 5, 6],
      [4, 6, 7, 9, 1, 0]]

ll2=[]

for row in ll:
    #[ll2.append(x) for x in ll]
    ll2.extend(row)
print(ll2)
print(ll)

ll = [
    [7, 1, 3, 3, 2, 1], # row 0
      [1, 3, 9, 8, 5, 6], # row 1
      [4, 6, 7, 9, 1, 0], # row 2
        ['a','b','k','p'] # row 3 или row -1
      ]

print(ll[1][0])
print(ll[3][1])
print(ll[-1][1])

print('==========================')

cube = [
    [
        [1,2,3],
        [4,5,6]
    ],
    [
        [11,-2,-53],
        [4,5,6]
    ]

]


print(cube[1][0][0])

matrix = [[7, 1, 3, 3, 2, 1], # row 0
      [1, 3, 9, 8, 5, 6], # row 1
      [4, 6, 7, 9, 1, 0]] # row 2

for row_index in range(len(matrix)):
    for column_index in range(len(matrix[row_index])):
        value = matrix[row_index][column_index]
        print(f'{value}:{row_index, column_index}' , end=' ')
    print()


