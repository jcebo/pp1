class Stack:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        return self.stack.pop()

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0
test=Stack()
a,b,c,d,e=2,8,9,52,12
test.push(a)
test.push(b)
test.push(c)
test.push(d)
test.push(e)
print(test.stack)
for n in range(3):
    print(test.pop())
print(test.stack)