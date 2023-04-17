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
    def print_alternate_list(self,node,number):
        if node==None:
            return
        if number %2!=0:
            print(node.data,end="-->")
        else:
            pass
        self.print_alternate_list(node.next,number+1)
    def deleteKnodes(self,K,i=0):
        if i>=K:
            return
        self.head=self.head.next
        self.deleteKnodes(K,i+1)
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
    list.print_alternate_list(list.head,1)
    #list.deleteKnodes(5)
    print()
    #list.print_list()
    print()
    list.printreverse(list.head)
