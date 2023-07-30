class node:
     def __init__(self,val):
         self.val=val
         self.next=None
class linked_list:
     def __init__(self) -> None:
        self.head=None
     def insert(self,val):
        if self.head==None:
            self.head=node(val)
        else:
            curr=self.head 
            while curr.next!=None:
                curr=curr.next
                
            curr.next=node(val)
     def print(self):
         curr=self.head
         while curr!=None:
             print(curr.val)
             curr=curr.next
             
#3 
def getSpecificNode(head:node,givenValue):
    curr=head
    prev_val=None
    while curr!=None:
        if curr.val==givenValue:
            return prev_val
        prev_val=curr.val
        curr=curr.next
