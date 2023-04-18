class Node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None

class doublylinkedlist:
  def __init__(self):
    self.head=None
    self.tail=None

  def insert(self,value):
    if self.head==None:
      self.head=Node(value)
      self.tail=self.head
    else:
      current=self.head
      while current.next!=None:
        current=current.next
      newnode=Node(value)
      current.next=newnode
      newnode.prev=current
      self.tail=newnode 
  def addAfterValue(self,givenValue,newValue):
    if self.head==None:
      return
    if self.head.data==givenValue:
      newnode=Node(newValue)
      newnode.next=self.head
      self.head=newnode
    else:
      curr=self.head
      prev=None
      while curr.data!=givenValue:
        prev=curr
        curr=curr.next
      newnode=Node(newValue)
      prev.next=newnode
      newnode.prev=prev
      newnode.next=curr
      curr.prev=newnode
  def printlist(self):
    current=self.head
    while current!=None:
      print(current.data,end="-->")
      current=current.next


