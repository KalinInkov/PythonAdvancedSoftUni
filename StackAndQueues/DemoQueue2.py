from collections import deque

q = deque()
# append,popleft
#appendleft, pop

q.append(1)
q.append(2)
q.append(3)

while q:
    print(q.popleft())