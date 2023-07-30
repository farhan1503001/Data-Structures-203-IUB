class stack:
    def __init__(self):
        self.data=[]
    def push(self,val):
        self.data.append(val)
    def is_empty(self):
        if len(self.data)<=0:
            return True
        else:
            return False
    def pop(self):
        if self.is_empty()==False:
            self.data.pop()
        else:
            pass
    def peek(self):
        if self.is_empty()!=False:
            return self.data[-1]
        
        
#out of class function: 1
def removeLargerData(stack:stack,givenValue):
    temp_stack=stack()
    while stack.is_empty()!=True:
        temp=stack.peek()
        stack.pop()
        if temp<=givenValue:
            temp_stack.push(temp)
        else:
            pass
    while temp_stack.is_empty()!=True:
        val=temp_stack.peek()
        temp_stack.pop()
        stack.push(val)
        
    return stack
