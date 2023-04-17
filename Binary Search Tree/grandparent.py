from search import BST,node

def is_grandparent(root,key1,key2):
    if root==None:
        return 
    else:
        #first e key1 k khojo then kahini somapto hobe
        curr=root
        while curr.data!=key1:
            if curr.data<key1:
                curr=curr.right
            elif curr.data>key1:
                curr=curr.left
        #Now we have found key1 now we will see whether exists or not
        grandparent=curr
        if grandparent.left.left!=None and grandparent.left.left.data==key2:
            print("Yes Grandparent")
        elif grandparent.left.right!=None and grandparent.left.right.data==key2:
            print("Yes Grandparent")
        elif grandparent.right.left!=None and grandparent.right.left.data==key2:
            print("Yes Grandparent")
        elif grandparent.right.right!=None and grandparent.right.right.data==key2:
            print("Yes Grandparent")
        else:
            print("No not grandparent")

