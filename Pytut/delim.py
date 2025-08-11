def balanced(exp):
    stack = []
    pairs = {']':'[','}':'{',')':'('}

    for i in exp:
        if i in pairs.values():
            stack.append(i)

        elif i in pairs:
            if not stack or stack[-1] != pairs[i]:
                return False
            stack.pop()

    return len(stack) == 0

print(balanced('(a+b*[c)'))
        
