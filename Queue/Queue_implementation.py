from collections import deque

class queue:
    def __init__(self) -> None:
        self.data=deque()
    def enqueue(self,value):
        self.data.append(value)
    def is_empty(self):
        if len(self.data)==0:
            return True
        else:
            return False

    def dequeue(self):
        if self.is_empty():
            return False
        else:
            return self.data.popleft()
    def peek(self):
        if self.is_empty():
            return
        else:
            return self.data[0]
class stack:
    def __init__(self) -> None:
        self.data=[]
    def push(self,item):
        self.data.append(item)
    def is_empty(self):
        if len(self.data)==0:
            return True
        else:
            return False
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            return self.data[-1]
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            return self.data.pop()
    def pushinsidestack(self,value):
        temp=stack()
        while(self.peek()<value):
            temp.push(self.peek())
            self.pop()
        self.push(value)
        while not temp.is_empty():
            self.push(temp.peek())
            temp.pop()


def reverse_queue(q,k):
    s=stack()
    for i in range(k):
        s.push(q.peek())
        q.dequeue()
    while not s.is_empty():
        q.enqueue(s.peek())
        s.pop()
    print(q.data)
    
q = queue()
q.enqueue(10)
q.enqueue(20)
q.enqueue(30)
q.enqueue(40)
q.enqueue(50)
q.enqueue(60)
q.enqueue(70)
q.enqueue(80)
q.enqueue(90)
print("Input:")
print(q.data)
print("Output: ")
reverse_queue(q, 5)