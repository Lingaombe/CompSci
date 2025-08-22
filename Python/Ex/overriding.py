class Parent:
    def add(self, a, b):
        c = a+b
        return c

class Child(Parent):
    def add(self, a, b):
        c = a-b
        return c

obj = Parent()

print(obj.add(10,20))