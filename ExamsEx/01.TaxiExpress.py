from collections import deque
import sys
from io import StringIO

test_input1 = """4, 6, 8, 5, 1
1, 9, 15, 10, 6
"""
test_input2 = """10, 5, 8, 9
2, 4, 5, 8
"""
test_input3 = """2, 8, 4, 3, 11, 7
10, 15, 4, 6, 3, 10, 2, 1
"""

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)

customers = deque(int(x) for x in input().split(','))
taxis = deque(int(x) for x in input().split(','))
total_time_passed = 0

while customers and taxis:
    current_customer = customers[0]
    current_taxi = taxis[-1]

    if current_taxi>=current_customer:
        total_time_passed+=current_customer
        customers.popleft()
        taxis.pop()
    elif current_taxi<current_customer:
        taxis.pop()

if not customers:
    print('All customers were driven to their destinations')
    print(f'Total time: {total_time_passed} minutes')
else:
    print('Not all customers were driven to their destinations')
    print(f'Customers left: {", ". join(str(x) for x in customers)}')



