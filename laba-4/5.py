class Stack:
    def __init__(self, size):
        self.size = size
        if size < 1:
            raise AssertionError("Stack is empty")
        self.items = []
    def top(self):
        return self.items[len(self.items)-1]
    def push(self, x):
        if len(self.items) == self.size:
            raise AssertionError("Overflow")
        else:
            self.items.append(x)
    def pop(self):
        if len(self.items) >= 2:
            return self.items.pop()
        else:
            raise AssertionError("Stack is empty")
    def show(self):
        return(self.items)
    def maximum(self):  #тк. стек на основе массива время будет O(n)
        return max(self.items)

with open('input.txt') as a:
    lines = a.readlines()
stack = Stack(10)
n = int(lines[20])
for i in range(n):
    ln = str(lines[i+21])
    com = ln.split()
    if com[0] == 'push':
        stack.push(com[1])
    elif com[0] == 'max':
        print(stack.maximum())
    elif com[0] == 'pop':
        stack.pop()