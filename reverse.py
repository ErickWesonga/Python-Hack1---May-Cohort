class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def reverse_string(input_string):
    # Create a stack object
    stack = Stack()

    # Push all characters of the string onto the stack
    for char in input_string:
        stack.push(char)

    # Pop all characters from the stack and form the reversed string
    reversed_string = ''
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string

# Test the function
input_string = "Hello, World!"
reversed_output = reverse_string(input_string)
#print(f"Original String: {input_string}")
print(f"Reversed String: {reversed_output}")