Balanced Brackets Validators = input("Enter bracket string: ")
stack = []
for ch in s:
    if ch == '(' or ch == '{' or ch == '[':
        stack.append(ch)
    elif ch == ')' or ch == '}' or ch == ']':
        if len(stack) == 0:     
            print("Not Balanced")
            break
        top = stack.pop()        
        if (ch == ')' and top != '(') or \
           (ch == ']' and top != '[') or \
           (ch == '}' and top != '{'):
            print("Not Balanced")
            break
else:
    if len(stack) == 0:
        print("Balanced")
    else:
        print("Not Balanced")