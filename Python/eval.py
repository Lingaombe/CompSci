def eval(exp):
    result = []

    for i in exp:
        if i.isdigit():
            result.append(int(i))
        else:
            a=result.pop()
            b=result.pop()

            if i=='+':
                result.append(a+b)
            elif i=='-':
                result.append(a-b)
            elif i=='*':
                result.append(a*b)
            elif i=='/':
                result.append(a/b)
    return result.pop()

print(eval('234*+'))