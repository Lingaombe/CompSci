def Delimeter(exp):
    stack = []
    braces = {
        ']':'[','}':'{',')':'('
    }

    for i in exp:
        if i in braces.values():
            stack.append(i)
        elif i in braces:
            if not stack or stack[-1] != braces[i]:
                return False
            stack.pop()
        return len(stack) == 0
    
print(Delimeter('[a+(b+c))'))