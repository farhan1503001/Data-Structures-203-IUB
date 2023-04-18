class node:
  def __init__(self,data):
    self.data=data
    self.next=None
    self.prev=None

class dll:
  def __init__(self):
    self.head=None
  def addNodeBeforeValue(self,givenValue,newValue):
    if self.head==None:
      return
    if self.head.data==givenValue:
      newnode=node(newValue)
      newnode.next=self.head
      self.head=newnode
    else:
      curr=self.head
      prev=None
      while curr.data!=givenValue:
        prev=curr
        curr=curr.next
      newnode=node(newValue)
      prev.next=newnode
      newnode.prev=prev
      newnode.next=curr
      curr.prev=newnode
  