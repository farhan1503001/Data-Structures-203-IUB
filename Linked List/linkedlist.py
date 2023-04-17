class node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
class Linkedlist:
    def __init__(self) -> None:
        self.head=None

    def insert(self,value):
        if self.head is None:
            self.head=node(value)
        else:
            curr=self.head
            while curr.next:
                curr=curr.next

            curr.next=node(value)

    def list_size(self):
        count=0
        curr=self.head
        while curr:
            count=count+1
            curr=curr.next

        return count
    def printlist(self):
        curr=self.head
        while curr:
            print(curr.data,end="-->")
            curr=curr.next   
        print()
    def delete(self,position):
        if self.head is None:
            return False
        else:
            index=position-1
            if index>self.list_size():
                return False
            else:
                count=0
                curr=self.head
                prev=None
                while curr:
                    
                    if count==index:
                        prev.next=curr.next
                    else:
                        prev=curr
                    curr=curr.next
                    count=count+1
        self.printlist()

if __name__=='__main__':
    l1=Linkedlist()
    l1.insert(22)
    l1.insert(32)
    l1.insert(15)
    l1.insert(78)
    l1.insert(23)
    l1.printlist()
    l1.delete(2)