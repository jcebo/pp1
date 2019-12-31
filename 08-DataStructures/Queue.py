class Queue:

    def __init__(self):
        self.stack = []

    def pop(self):
        if self.is_empty():
            return None
        length=len(self.stack)
        return self.stack.pop(-length)

    def push(self, item):
        self.stack.append(item)

    def is_empty(self):
        return len(self.stack)==0
test=Queue()
a,b,c,d,e=12,8,52,96,32
test.push(a)
test.push(b)
test.push(c)
test.push(d)
test.push(e)
print(test.stack)
for n in range(3):
    print(test.pop())
print(test.stack)