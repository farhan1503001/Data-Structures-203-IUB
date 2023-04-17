class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None 
class LinkedList:
    def __init__(self) -> None:
        self.head=None
    def insert(self,value):
        if self.head==None:
            self.head=Node(value)
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            curr.next=Node(value)
    def print_list(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end="->")
            curr=curr.next
    def printreverse(self,node):
        if node==None:
            return
        self.printreverse(node.next)
        print(node.data,end="->")
        
if __name__=="__main__":
    list=LinkedList()
    list.insert(1)
    list.insert(2)
    list.insert(3)
    list.insert(4)
    list.insert(5)
    list.insert(6)
    list.insert(7)
    list.print_list()
    print()
    print()
    list.printreverse(list.head)
