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
    def deleteEvens(self):
        q=queue()
        while not self.is_empty():
            if self.peek()%2!=0:
                val=self.peek()
                q.enqueue(val)
            self.pop()
        while not q.is_empty():
            val=q.peek()
            self.push(val)
            q.dequeue()

s=stack()
s.push(4)
s.push(3)
s.push(7)
s.push(9)
s.push(6)
s.deleteEvens()
print(s.data)
        

