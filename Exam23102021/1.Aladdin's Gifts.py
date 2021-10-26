import sys
from io import StringIO
from collections import deque

test_input1 ="""0 20 30 25
120 60 11 400 10 0
"""
test_input2 = """30 5 21 6 0 91
15 9 5 15 8
"""
test_input3 = """200 1000 200 200
105 200 32 20 10 5 100 200
"""

#sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)

def sum_present(materials, magic_level):
    sum_present = materials[-1] + magic_level[0]
    if sum_present < 100:
        if sum_present % 2 == 0:
            sum_present = materials[-1] * 2 + magic_level[0] * 3
            return sum_present
        elif sum_present % 2 != 0:
            sum_present *= 2
            return sum_present
    elif sum_present>499:
        sum_present/=2
        return sum_present
    return sum_present


values_of_materials = [int(x) for x in input().split()]
magic_levels = deque([int(x) for x in input().split()])

table = {'Gemstone':0,
         'Porcelain Sculpture':0,
         'Gold':0,
         'Diamond Jewellery':0
}


while values_of_materials or magic_levels:
    if  not values_of_materials:
        break
    if not magic_levels:
        break

    if 100<=sum_present(values_of_materials,magic_levels)<=199:
        table['Gemstone']+=1
        values_of_materials.pop()
        magic_levels.popleft()
    elif 200<=sum_present(values_of_materials,magic_levels)<=299:
        table['Porcelain Sculpture']+=1
        values_of_materials.pop()
        magic_levels.popleft()
    elif 300<=sum_present(values_of_materials,magic_levels)<=399:
        table['Gold']+=1
        values_of_materials.pop()
        magic_levels.popleft()
    elif 400<=sum_present(values_of_materials,magic_levels)<=499:
        table['Diamond Jewellery']+=1
        values_of_materials.pop()
        magic_levels.popleft()
    else:
        values_of_materials.pop()
        magic_levels.popleft()


if (table['Gemstone']>0 and table['Porcelain Sculpture']>0)\
        or (table['Gold']>0 and table['Diamond Jewellery']>0):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")


if values_of_materials:
    print(f'Materials left: {",".join([str(x) for x in values_of_materials])}')
if magic_levels:
    print(f'Magic left: {", ".join([str(x) for x in magic_levels])}')

for k, v in sorted(table.items()):
    if v>0:
        print(f'{k}: {v}')
# print(table)


