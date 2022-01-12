def is_valid_expression(expression):
    cnt = 0

    for ch in expression:
        if ch=="(":
            cnt+=1
        elif ch==")":
            cnt-=1
        if cnt<0:
            return False
    return cnt==0
expression1 = "(2+3)-(3+4)"
expression2 = "(2+3))-(3+4)"
print(is_valid_expression(expression1))
print(is_valid_expression(expression2))