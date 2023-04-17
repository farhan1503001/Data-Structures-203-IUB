from search import BST,node

def is_ancestor(root,key1,key2):
    if root==None:
        return
    else:
        curr=root
        print("Printing ancestors>>>>")
        #prothome key1 ase kina khujbo then flag lagabo paile ar  na paile to nai
        Flag1=False
        while curr!=None:
            
            if curr.data==key1:
                Flag1=True
            print(curr.data,end="--->")
            if curr.data<key1:
                curr=curr.right

            elif curr.data>key1:
                curr=curr.left
        if curr==None:
            print("Not found")
            return
        ancestor=curr
        if Flag1==False:
            print("Not found return")
        else:
            #ekhon khujbo key2 
            curr1=ancestor
            while curr1!=None:
                if curr1.data==key2:
                    print(f"{key1} is ancestor of {key2} ")
                    return
                if curr1.data<key1:
                    curr1=curr1.right
                elif curr.data>key1:
                    curr1=curr1.left
            if curr1==None:
                print("not ancestor")

if __name__=="__main__":
    lister=[5,7,3,9,8,11,4,1,25]
    tree=BST()
    for val in lister:
        tree.insert(val)

    print_ancestor(tree.root,8,)