from search import BST,node

def print_ancestor(root,key):
    if root==None:
        return
    else:
        curr=root
        print("Printing ancestors>>>>")
        while curr!=None:
            
            if curr.data==key:
                break
            print(curr.data,end="--->")
            if curr.data<key:
                curr=curr.right

            elif curr.data>key:
                curr=curr.left
        if curr==None:
            print("Not found")

if __name__=="__main__":
    lister=[5,7,3,9,8,11,4,1,25]
    tree=BST()
    for val in lister:
        tree.insert(val)

    print_ancestor(tree.root,8)