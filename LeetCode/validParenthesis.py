class Solution(object):
    def isValid(self, expression):
        stack = {')': '(', '}': '{', ']': '['}
        statement = []

        for i in expression:
            if i in stack.values():
                statement.append(i)
            elif i in stack.keys():
                if not statement or statement[-1] != stack[i]:
                    return False
                statement.pop()
        return len(statement) == 0
        
