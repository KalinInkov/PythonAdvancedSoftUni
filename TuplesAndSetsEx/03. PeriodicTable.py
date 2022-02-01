n= int(input())
unique_list = []

for _ in range(n):
    command = input().split()
    for el in command:
        unique_list.append(el)

[print(x) for x in set(unique_list)]