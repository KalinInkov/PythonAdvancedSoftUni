import sys
from io import StringIO
from collections import deque

test_input1 = """ROB-15;SS2-10;NX8000-3
8:00:00
detail
glass
wood
apple
End
"""

test_input2 = """ROB-60
7:59:59
detail
glass
wood
sock
End
"""
#sys.stdin = StringIO(test_input1)


sys.stdin = StringIO(test_input2)

def next_second(h, m, s):
    s += 1
    if s == 60:
        m += 1
        s = 0
    if m == 60:
        h += 1
        m = 0
    if h == 60:
        h = 0
    return h, m, s


robot_info = input().split(';')
robot_dict = {}
avaible_robots = deque()
waiting_robots = deque()
products = deque()
time = [int(x) for x in input().split(':')]

print(next_second(time[0], time[1], time[2]))

product = input()

while product != "End":
    products.append(product)

    product = input()

for robot in robot_info:
    robot_name = robot.split('-')[0]
    robot_time = int(robot.split('-')[1])
    avaible_robots.append([robot_name, robot_time])
    robot_dict[robot_name] = robot_time

while products:
    for robot in waiting_robots:
        robot_name = robot[0]
        robot[1] -= 1
        if robot[1] <= 0:
            avaible_robots.append([robot_name, robot_dict[robot_name]])
    waiting_robots = [r for r in waiting_robots if r[1] > 0]

    # Увеличаваме си времето с една секунда от функцията...
    time = next_second(time[0], time[1], time[2])
    # След това трябва да вземем от продукта, който искаме да работим/взимаме първия/
    current_product = products.popleft()
    # Избираме и първия робот

    if not avaible_robots:
        products.append(current_product)
        continue
    current_robot = avaible_robots.popleft()
    print(f'{current_robot[0]} - {current_product} [{time[0]:02d}:{time[1]:02d}:{time[2]:02d}]')
    waiting_robots.append(current_robot)

# print(avaible_robots)
# print(products)
