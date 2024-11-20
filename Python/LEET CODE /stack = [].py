
stack = []
variable_dict = {"(": ")", "{": "}", "[": "]"}
equation = "(a)  + (b-c)"

for char in equation:
    if char in variable_dict:
        print("yes" )
        stack.append(char)
    elif char in variable_dict.values():
        if not stack or variable_dict[stack.pop(0)] != char:
           print("False")
           break

