def intopo(exp):
    stack=[]
    result = []

    for i in exp:
        if i.isalnum():
            stack.append(i)
        elif i in '+/-*':
            while stack and stack[-1] in '+/-*':
                result.append(stack.pop())
            stack.append(i)

    while stack:
        result.append(stack.pop())
    return "".join(result)

print(intopo("a+b*c-d"))