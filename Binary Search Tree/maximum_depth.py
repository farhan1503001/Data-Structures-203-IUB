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

def maximum_depth(root):
    if root==None:
        return 0
    else:
        l_depth=maximum_depth(root.left)
        r_depth=maximum_depth(root.right)
        if l_depth<=r_depth:
            return r_depth+1
        else:
            return l_depth+1

if __name__=='__main__':
    tree=BST()
    lister=[]
    for i in range(12):
        lister.append(r.randint(10,123))
    
    for val in lister:
        tree.insert(val)

    tree.inorder(tree.root)
    print(maximum_depth(tree.root))


