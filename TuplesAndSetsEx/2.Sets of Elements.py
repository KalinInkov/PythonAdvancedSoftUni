n,m = [ int(x) for x in input().split()]
first_set = []
second_set = []

for _ in range(n):
    first_set.append(int(input()))
for _ in range(m):
    second_set.append(int(input()))


res = set(first_set)&set(second_set)


[print(x) for x in res]


