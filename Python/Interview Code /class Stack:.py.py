class Stack:
    def __init__(self):
        # Initialize an empty list to store stack elements
        self.stack = []

    def push(self, x: int) -> None:
        # Add the element to the top of the stack
        self.stack.append(x)

    def pop(self) -> int:
        # Check if the stack is not empty before popping
        if not self.is_empty():
            return self.stack.pop()
        else:
            raise IndexError("pop from empty stack")

    def top(self) -> int:
        # Return the top element without removing it, if stack is not empty
        if not self.is_empty():
            return self.stack[-1]
        else:
            raise IndexError("stack is empty")

    def is_empty(self) -> bool:
        # Return True if the stack is empty, otherwise False
        return len(self.stack) == 0

check_stack = Stack()
check_stack.push(10)
check_stack.push(19)
print(check_stack.top())
print(check_stack.pop())
print(check_stack.pop())
print(check_stack.pop())