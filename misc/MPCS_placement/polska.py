# https://uchicago.kattis.com/problems/uchicago.rpn
# Polsa 

tokens = input().split()
stack = []

for token in tokens:
    if token.isdigit():
        stack.append(int(token))
    elif token == 'true':
        stack.append(True)
    elif token == 'false':
        stack.append(False)
    elif token in ['+', '*', '==', 'and', 'or']:
        if len(stack) < 2:
            print("SYNTAX ERROR")
            exit()
        else:
            a = stack.pop()
            b = stack.pop()
            if (str(a) in ['True', 'False'] and str(b).isdigit()) or (str(a).isdigit() and str(b) in ['True', 'False']):
                print("TYPE ERROR")
                exit()
            elif str(a) in ['True', 'False'] and str(b) in ['True', 'False'] and token in ['+', '*', '==']:
                print("TYPE ERROR")
                exit()
            elif str(a).isdigit() and str(b).isdigit() and token in ['and', 'or']:
                print("TYPE ERROR")
                exit()          
            elif token == '+':
                    stack.append(a + b)
            elif token == '*':
                    stack.append(a * b)
            elif token == '==':
                    stack.append(a == b)
            elif token == 'and':
                    stack.append(a and b)
            elif token == 'or':
                    stack.append(a or b)
if len(stack) == 1:
    if str(stack[0]) in ['True', 'False']:
        print(str(stack[0]).lower())
    else:
        print(stack[0])
else:
    print("SYNTAX ERROR")