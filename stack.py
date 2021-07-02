#we will implement stack today
from pip._vendor.progress.counter import Stack


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []
    def push(self,item):
        self.items.append(item)

    def pop(self):
        self.items.pop()
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)



    s =  Stack()

    s.push(3)
    s.push(7)

    print(s.peek())