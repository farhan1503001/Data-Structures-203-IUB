import random as r
class node:
    def __init__(self,val) -> None:
        self.data=val
        self.left=None
        self.right=None
class BST:
    def __init__(self) -> None:
        self.root=None

    def insert(self,val):
        newnode=node(val)
        if self.root==None:
            self.root=newnode
        else:
            current=self.root
            parent=None
            while current!=None:
                parent=current
                if val<=current.data:
                    current=current.left
                else:
                    current=current.right
            if val<=parent.data:
                parent.left=newnode
            else:
                parent.right=newnode

    def inorder(self,root):
        current=root
        if current==None:
            return
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)
def odd_or_even(root):
    if root==None:
        return
    if root.left==None and root.right==None:
        if root.data%2==0:
            print(root.data," is even")
        else:
            print(root.data," is odd")
        return
    else:
        odd_or_even(root.left)
        odd_or_even(root.right)

if __name__=='__main__':
    tree=BST()
    lister=[5,12,9,7,3,1,2]
    """
    for i in range(12):
        lister.append(r.randint(10,123))
    """
    
    for val in lister:
        tree.insert(val)

    tree.inorder(tree.root)
    odd_or_even(tree.root)


