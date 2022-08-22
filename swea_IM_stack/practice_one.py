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
<<<<<<< HEAD
print(stk)
=======

>>>>>>> 7a996084a1a27ad6d1c9f62d1d7ad998111e3fc6
stk.push(1)
stk.push(2)
stk.push(3)

print(stk.pop())
print(stk.pop())
<<<<<<< HEAD
print(stk.pop())


=======
print(stk.pop())
>>>>>>> 7a996084a1a27ad6d1c9f62d1d7ad998111e3fc6
