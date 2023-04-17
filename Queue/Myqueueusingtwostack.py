from Queue_implementation import stack
class Myqueue:
    def __init__(self) -> None:
        self.s1=stack()
        self.s2=stack()
    def enqueue(self,x):
        #Jotokkhon s1 faka na hoy
        while len(self.s1.data)>0:
            #pop everybit of shit from s1 and store that in s2
            temp=self.s1.peek()
            self.s2.push(temp)
            self.s1.pop()
        #Now push the shit in s1 now
        self.s1.push(x)
        #Now put every bit of shit back to s1
        while len(self.s2.data)>0:
            temp1=self.s2.peek()
            self.s1.push(temp1)
            self.s2.pop()
    def dequeue(self):
        #Now pop the shit from s2
        if self.s1.is_empty():
            print("Invalid operation cannot dequeue data from here")
            return
        else:
            self.s1.pop()
    def size(self):
        return len(self.s1.data)
    def peek(self):
        if self.s1.is_empty():
            print("Queue is empty")
        else:
            x=self.s1.peek()
            return x 
    def printQueue(self):
        print(self.s1.data)

if __name__=='__main__':
    m=Myqueue()
    m.enqueue(12)
    m.enqueue(56)
    m.enqueue(22)
    m.enqueue(11)
    m.enqueue(8)
    m.printQueue()


        