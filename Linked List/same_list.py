class node:
    def __init__(self,val) -> None:
        self.value=val
        self.next=None 

class linked_list:
    def __init__(self) -> None:
        self.head=None
    def insert(self,value):
        if self.head==None:
            self.head=node(value)
        curr=self.head
        while(curr.next!=None):
            curr=curr.next 
        curr.next=node(value)
    def print_list(self):
        curr=self.head
        while curr!=None:
            print(curr.value)
            curr=curr.next
    def size(self):
        curr=self.head
        counter=0
        while(curr!=None):
            counter+=1
            curr=curr.next

        return counter
    

def same_list(l1,l2):
    #prothome list initialize korbo
    flag=True
    if l1.size()!=l2.size():
        print("Lists are different not the same so ignore the shit")
    else:
        curr1=l1.head
        curr2=l2.head

        while(curr1!=None and curr2!=None):
            if curr1.value!=curr2.value:
                flag=False
                print('Lists are not the same')
            else:
                pass
            curr1=curr1.next
            curr2=curr2.next
    if flag:
        print("Lists are same")
    

if __name__=='__main__':
    l1=linked_list()
    l2=linked_list()
    l1.insert(11)
    l1.insert(22)
    l1.insert(6)
    l1.insert(8)
    l2.insert(11)
    l2.insert(22)
    l2.insert(7)
    l2.insert(8)
    same_list(l1,l2)
