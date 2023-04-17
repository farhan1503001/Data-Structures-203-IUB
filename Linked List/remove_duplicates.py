from reverse_linkedlist import linked_list
from reverse_linkedlist import node
def remove_duplicates(l1:linked_list):
    """
    Here in this function we will remove duplicate 
    numbers from the linked list
    """
    dictionary=dict()
    curr=l1.head
    prev=None
    while curr:
        if curr.data not in dictionary:
            dictionary[curr.data]=None
            prev=curr
        else:
            prev.next=curr.next

        curr=curr.next
        

    l1.printlist()


if __name__=='__main__':
    l1=linked_list()
    l1.insert(32)
    l1.insert(44)
    l1.insert(44)
    l1.insert(15)
    l1.insert(22)
    l1.insert(15)
    l1.insert(19)
    l1.insert(20)
    remove_duplicates(l1)