def infix_to_postfix(expression): 
    stack = [] 
    result = [] 
 
    for char in expression: 
        if char.isalnum():                                 # If the character is an operand (A-Z, 0-9) 
            result.append(char)                       # Add operand to the result list 
        elif char in '+-*/':                                # If the character is an operator 
            # Pop the operator from the stack and add it to the result list 
            while stack and stack[-1] in '+-*/': 
                result.append(stack.pop()) 
            stack.append(char)  # Push the current operator onto the stack 
 
    # Pop all remaining operators from the stack to the result 
    while stack: 
        result.append(stack.pop()) 
 
    # Join the result list into a string and return it 
    return ''.join(result) 
 
# Test example for infix to postfix conversion 
infix_expr = "A+B*C-D" 
postfix_expr = infix_to_postfix(infix_expr) 
print("Infix Expression:", infix_expr) 
print("Postfix Expression:", postfix_expr)