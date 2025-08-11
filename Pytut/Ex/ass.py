x = lambda n: '{} is div'.format(n) if n%5 == 0 and n%3 == 0 else '{} is not div'.format(n)
print(x(15))
L = ['amazon', 'google', 'microsoft', 'instagram', 'yahoo', 'Hello', 'Hi']

h = lambda L : ['{}'.format(i) for i in L if len(i)>=7]
print(h(L))


def filte(L):
    N = []
    for i in L:
        if len(i) >= 7:
            N.append(i)

    L=N
    print(L)
filte(L)



L=['apple', 'mango', 'orange', 'berry', 'coconut']
b = lambda L : [i.upper() for i in L]
print(b(L))

d={}
a = lambda n : '{}'.format({n:n[::-1]})
n="Welcome"
print(a(n))

f = lambda w : '%s'%({w:w[::-1]})

print(f("Welcome"))

import math

L=[36,49,81,16,9]
def sort(L):
    for i in L:
        print(math.sqrt(i))

sort(L)
