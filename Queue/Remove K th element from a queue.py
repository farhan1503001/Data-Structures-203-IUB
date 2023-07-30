class Queue:
    def __init__(self) -> None:
        self.data=[]
    def enqueue(self,val):
        self.data.append(val)
    def is_empty(self):
        if len(self.data)<=0:
            return True
        else:
            return False
    def dequeue(self):
        if self.is_empty()!=False:
            self.data.pop(0)
        else:
            pass
    def front(self):
        if self.is_empty()!=False:
            return self.data[0]
        else:
            pass
        
#function 2 
def removeKthelement(queue:Queue,K:int):
    temp_s=stack()
    count=0
    while queue.is_empty()!=False:
        temp_val=queue.front()
        queue.dequeue()
        count+=1
        if count==K:
            continue
        temp_s.push(temp_val)
        
