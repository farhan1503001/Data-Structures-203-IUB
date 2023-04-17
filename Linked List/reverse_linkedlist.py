class stack:
    def __init__(self) -> None:
        self.data=[]
    def push(self,value):
        self.data.append(value)
    def is_empty(self):
        if len(self.data)==0:
            return True
        else:
            return False
    def pop(self):
        if self.is_empty():
            return False
        else:
            return self.data.pop()
    def peek(self):
        if self.is_empty():
            return False
        else:
            return self.data[-1]
class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None 
class linked_list:
    def __init__(self) -> None:
        self.head=None
    def insert(self,value):
        if self.head==None:
            self.head=node(value)
        else:
            curr=self.head
            while curr.next:
                curr=curr.next

            curr.next=node(value)

    def printlist(self):
        curr=self.head
        while curr:
            print(curr.data,end="-->")
            curr=curr.next
def reverse_linked_list(l1:linked_list):
    #eitar kaj kisui na just matha ghurai dibo
    previous_node=l1.head
    current=l1.head.next
    previous_node.next=None
    while current!=None:
        #ekhon current er connection ulto kore dibo but
        #ami to samne jabo tai current.next ke store kore rakhbo
        temp=current.next
        current.next=previous_node
        #previous keo dhore raksi
        previous_node=current
        #connection ulto kore dissi
        current=temp 

    #head ekhon change kore dissi
    l1.head=previous_node
    l1.printlist()

def reverse_linked_list_withstack(l1:linked_list):
    curr=l1.head
    s=stack()
    while curr:
        s.push(curr.data)
        curr=curr.next 
    #Now set the linked list
    curr=l1.head
    while not s.is_empty() and curr!=None:
        val=s.peek()
        curr.data=val
        curr=curr.next
        s.pop()

    l1.printlist()
        
    
if __name__=='__main__':
    list=linked_list()
    list.insert(34)
    list.insert(23)
    list.insert(7)
    list.insert(99)
    list.insert(11)

    reverse_linked_list(list)
    reverse_linked_list_withstack(list)