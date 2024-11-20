stack = []
variable_dict = {"(": ")", "{": "}", "[": "]"}
equation = "a  + (b-c)(0"

for char in equation:
    if char in variable_dict:
        stack.append(char)
        print(char ,stack)
        print("true")
    elif char in variable_dict.values():
        if not stack or variable_dict[stack.pop(0)] != char:
            print("False")

if stack:
    print("false")
    