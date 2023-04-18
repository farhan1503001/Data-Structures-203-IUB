from dlinkedlist import dlinkedlist

def deleteLast(head,value):
  #Delete last duplicate value
  current=head
  #tail ber korbo
  while current.next!=None:
    current=current.next
  tail=current
  # 1-3-5-7-78-8-9  delete korbo 8 k
  current=tail
  while current.data!=value:
    current=current.prev
  current.prev.next=current.next
  current.next.prev=current.prev
  #print korar jonno
  curr=head
  while curr!=None:
    print(curr.data,end="-> ")
    curr=curr.next


               
dlist=dlinkedlist()
dlist.insert(1)
dlist.insert(3)
dlist.insert(5)
dlist.insert(7)
dlist.insert(8)
dlist.insert(8)
dlist.insert(8)
dlist.insert(8)
dlist.insert(9)
dlist.print()
deleteLast(dlist.head,8)
print()