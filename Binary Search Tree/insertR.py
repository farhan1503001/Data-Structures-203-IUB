import random as r
class node:
    def __init__(self,val) -> None:
        self.data=val
        self.left=None
        self.right=None
class BST:
    def __init__(self) -> None:
        self.root=None
    def insertR(self,data,root):
        if root==None:
            return node(data)
        else:
            if data<self.root.data:
                root.left=self.insertR(data,root.left)
            else:
                root.right=self.insertR(data,root.right)

        return root
        

    def inorder(self,root):
        current=root
        if current==None:
            return
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)

if __name__=='__main__':
    tree=BST()
    lister=[]
    for i in range(12):
        lister.append(r.randint(10,123))
    
    for val in lister:
        tree.root=tree.insertR(val,tree.root)

    tree.inorder(tree.root)


