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


s = stack()

s.push(30)
s.push(20)
s.push(15)
s.push(10)
s.push(5)
print(s.data)
s.pushinsidestack(12)
print(s.data)
        