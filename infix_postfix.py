def infix_to_postfix(in_expr):
    # Define operator precedence
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '^': 3}
    op_stack = []
    res_stack = []
    expr = []
    open_b = 0
    close_b = 0
    for char in in_expr:
        if ord(char) != 32 and ord(char) != 9:
            expr.append(char)
        if char == '(':
            open_b +=1
        if char == ')':
            close_b += 1
    if open_b != close_b :
        return 'Invalid Infix Expression'
    #print(expr)
    print("%-8s %-8s %-8s"%("Character","Operator_Stack","Result"))
    for char in expr:
        op = ""
        o = ""
        if char.isalpha() or char.isnumeric():
            res_stack.append(char)
        elif char == '(':
            op_stack.append(char)
        elif char == ')':
            while op_stack and op_stack[-1] != '(':
                res_stack.append(op_stack.pop())
            if op_stack and op_stack[-1] == '(':
                op_stack.pop()
        else:
            while op_stack and op_stack[-1] != '(' and precedence.get(op_stack[-1]) >= precedence.get(char):
                res_stack.append(op_stack.pop())
            op_stack.append(char)
        for elem in op_stack:
            op+=elem
        for elem in res_stack:
            o+=elem
        print("%-8s %-8s %-8s"%(char,op,o))
    while op_stack:
        res_stack.append(op_stack.pop())
    result = ""
    for elem in res_stack:
        result+=elem
    return result

# exp = [0] * 3
# exp[0] = "((A*B)+(C/D))"
# exp[1] = "((A*(B+C))/D)"
# exp[2] = "(A*(B+(C/D)))"

# for elem in exp:
#     res = infix_to_postfix(elem)
#     print()
#     print("Final Result : ")
#     print(res)
#     print()
#     print('******************************************')
#     print()

exp = "(A/B+C*D)"
res = infix_to_postfix(exp)
print(res)