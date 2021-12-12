class Queue:
    def __init__(self):
        self.stack = []
    def enqueue(self, x):
        self.stack.append(x)
    def dequeue(self):
        if len(self.stack) == 0:
            return AssertionError('empty queue')
        else:
            x = self.stack.pop()
            return x
    def enprint(self):
        return self.stack

ochered = Queue()
coms = ['+1', '+10', '-', '-']
ans = []
for i in range(len(coms)):
    string = str(coms[i])
    if string[0] == '+':
        ochered.enqueue(string[0:])
    elif string[0] == '-':
        ans.append(ochered.dequeue())
print(ans)