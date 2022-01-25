from collections import deque
import sys
from io import  StringIO


test_input1 = """5, 25, 25, 115
5, 15, 25, 35
"""
test_input2 = """30, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 10
"""
test_input3 = """0, 40, 5, 55, 50, 100, 110, 35, 40, 35, 100, 80
20, 25, 20, 5, 20, 20, 70, 5, 35, 0, 0
"""
#sys.stdin = StringIO(test_input1)
#sys.stdin = StringIO(test_input2)
sys.stdin = StringIO(test_input3)

bomb_effects = deque(int(x) for x in input().split(', '))
bomb_casings = [int(x) for x in input().split(', ')]
bomb_made = False
bombs = {
    'Datura Bombs':0,
    'Cherry Bombs':0,
    'Smoke Decoy Bombs':0
}
while (bomb_effects and bomb_casings):


    current_b_effect = bomb_effects[0]
    current_b_casing = bomb_casings[-1]
    sum_bomb = current_b_effect+current_b_casing

    if sum_bomb==40:
        bombs['Datura Bombs']+=1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif sum_bomb==60:
        bombs['Cherry Bombs']+=1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif sum_bomb==120:
        bombs['Smoke Decoy Bombs']+=1
        bomb_effects.popleft()
        bomb_casings.pop()
    elif sum_bomb==0:
        bomb_effects.popleft()
        bomb_casings.pop()
    else:

        bomb_casings[-1]-=5
    if (bombs['Datura Bombs']>=3 and bombs['Cherry Bombs']>=3 and bombs['Smoke Decoy Bombs']>=3):
        bomb_made = True
        break


bomb_effects = list(bomb_effects)
if bomb_made:
    print("Bene! You have successfully filled the bomb pouch!")
else:
    print("You don't have enough materials to fill the bomb pouch.")
if bomb_effects:
    print(f"Bomb Effects: {', '.join([str(x) for x in bomb_effects])}")
else:
    print("Bomb Effects: empty")
if bomb_casings:
    print(f"Bomb Casings: {', '.join([str(x) for x in bomb_casings])}")
else:
    print("Bomb Casings: empty")
[print(k,v,sep=': ') for k,v in sorted(bombs.items()) ]





