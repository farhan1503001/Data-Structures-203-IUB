class Node:
  def __init__(self,val):
    self.data=val
    self.next=None 
    self.prev=None
class dlinkedlist:
  def __init__(self):
    self.head=None
    self.tail=None
  def insert(self,val):
    if self.head==None:
      newnode=Node(val)
      self.head=newnode
      self.tail=newnode
    else:
      current=self.head
      while current.next!=None:
        current=current.next
      newnode=Node(val)
      current.next=newnode
      newnode.prev=current
      self.tail=newnode
  def print(self):
    current=self.head
    while current!=None:
      print(current.data,end="->")
      current=current.next
    print()