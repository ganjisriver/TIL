class stack():
    def __init__(self):
        self.stack = []

    def push(self, data):
        self.stack.append(data)

    def top(self):
        top_value = self.stack[-1]
        return top_value
    def pop(self):
        pop_value = self.stack.pop()
        return pop_value

stk = stack()
print(stk)
stk.push(1)
stk.push(2)
stk.push(3)

print(stk.pop())
print(stk.pop())
print(stk.pop())


