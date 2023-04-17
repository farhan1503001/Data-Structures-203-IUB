class node:
    def __init__(self,val) -> None:
        self.value=val
        self.next=None 

class linked_list:
    def __init__(self) -> None:
        self.head=None
    def insert(self,value):
        if self.head==None:
            self.head=node(value)
        curr=self.head
        while(curr.next!=None):
            curr=curr.next 
        curr.next=node(value)
    def print_list(self):
        curr=self.head
        while curr!=None:
            print(curr.value)
            curr=curr.next
    def get_average(self):
        sum=0
        count=0
        curr=self.head
        while curr!=None:
            sum+=curr.value
            count+=1
            curr=curr.next
        print("Average value is: ",sum/count)
    def num_occurances(self,value):
        counter=0
        curr=self.head
        while curr!=None:
            if curr.value==value:
                counter+=1
            curr=curr.next
        print("Occured instances is: ",counter)

if __name__=='__main__':
    lister=linked_list()
    lister.insert(23)
    lister.insert(4)
    lister.insert(88)
    lister.insert(12)
    lister.insert(3)
    lister.insert(88)
    lister.print_list()
    lister.num_occurances(88)