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

def largestontopstack(s):
    #amader lagbe ekta helping stack sekhan theke amra max take ber kore rakhbo
    helping_stack=stack()
    if s.is_empty():
        print("Stack is empty")
        return
    #ekhon amra helping stack e vorbo sob faktale maximum ta ber kore nibo
    max=s.peek()
    while not s.is_empty():
        #ekta kore dekhbo then check korbo se boro kina
        val=s.peek()
        if val>max:
            max=val
        helping_stack.push(val)
        s.pop()
    #eibar helper tare faka korbo
    while not helping_stack.is_empty():
        val=helping_stack.peek()
        helping_stack.pop()
        if val!=max:
            s.push(val)
        
    #Finally borotare dhukai dibo
    s.push(max)
    return s
            
        

if __name__=='__main__':
    print("Largest on top stack")
    s=stack()
    s.push(14)
    s.push(15)
    s.push(1)
    s.push(99)
    s.push(32)
    s.push(66)
    print(s.data)
    res_stack=largestontopstack(s)
    print(res_stack.data)
