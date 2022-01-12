def get_matching_brackets(expression):
    opening_bracket_indicies = []
    sub_expression = []
    for i in range(len(expression)) :
        ch =expression[i]
        if ch=="(":
            opening_bracket_indicies.append(i)
        elif ch==")":
            start_index = opening_bracket_indicies.pop()
            end_index = i
            sub_expression.append(
                expression[start_index:end_index+1]
            )
    return sub_expression

expression = "1 + (2 - (2 + 3) * 4 / (3 + 1)) * 5"
sub_expression = get_matching_brackets(expression)
#print(*get_matching_brackets(expression),sep= "\n")
[print(exp) for exp in sub_expression]