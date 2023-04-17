class Node:
    def __init__(self,data) -> None:
        self.data=data
        self.next=None
        self.prev=None

class doublylinkedlist:
    def __init__(self) -> None:
        self.head=None
    def insert(self,value):
        if self.head==None:
            self.head=Node(value)
        else:
            curr=self.head
            while curr.next!=None:
                curr=curr.next
            newnode=Node(value)
            newnode.prev=curr
            curr.next=newnode
    def reverse_list(self,prev,node):
        if node==None:
            self.head=prev
            return
        nextnode=node.next
        node.next=node.prev
        node.prev=nextnode
        self.reverse_list(node,nextnode)
    def print_list(self):
        curr=self.head
        while curr!=None:
            print(curr.data,end="->")
            curr=curr.next
        print()
if __name__=="__main__":
    list=doublylinkedlist()
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
    list.reverse_list(None,list.head)
    list.print_list()
