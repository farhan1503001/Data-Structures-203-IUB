class Maxstack:
    def __init__(self) -> None:
        self.stack=[]
        self.max=None
    def push(self,value):
        if len(self.stack)==0:
            self.stack.append((value,value))
            self.max=value
        else:
            if value>self.max:
                self.max=value
            self.stack.append((value,self.max))
    def pop(self):
        if len(self.stack)==0:
            print("stack is empty")
            return False
        else:
            self.stack.pop()
    def peek(self):
        if len(self.stack)==0:
            return False
        else:
            return self.stack[-1][0]
    def Max(self):
        return self.stack[-1][1]
    def is_empty(self):
        if len(self.stack)==0:
            return True
        else:
            return False
        
if __name__=="__main__":
    s=Maxstack()
    s.push(34)
    s.push(12)
    s.push(88)
    s.push(11)
    print(s.Max())
    print(s.peek())