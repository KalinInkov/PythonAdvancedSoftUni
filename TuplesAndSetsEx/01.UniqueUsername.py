n = int(input())
usernames = []
for _ in range(n):
    username = input()
    usernames.append(username)



[print(x) for x in set(usernames)]
