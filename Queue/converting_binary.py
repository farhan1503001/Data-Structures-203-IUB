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
def convert_binary(number):
    q=queue()
    for i in range(1,number+1):
        s=stack()
        decimal=i
        while decimal!=0:
            bit=decimal%2
            decimal=decimal//2
            s.push(bit)

        result=""
        while not s.is_empty():
            bit=s.peek()
            s.pop()
            result=result+str(bit)
        q.enqueue(result)
    while not q.is_empty() :
        print(q.peek())
        q.dequeue()

if __name__=="__main__":
    n = int(input("Enter the number: "))
    print(f"Binary number from 1 to {n}: ")
    convert_binary (n)




