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

    def search(self,root,key):
        if root==None:
            return False
        if root.data==key:
            return True
        elif root.data<key:
            return self.search(root.left,key)
        else:
            return self.search(root.right,key)

    def inorder(self,root): 
        current=root
        if current==None:
            return
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)
def counting_nodes(root):
    if root==None:
        return
    else:
        q=[]
        q.append(root)
        count=0
        while len(q)!=0:
            temp=q.pop(0)
            count=count+1
            if temp.left!=None:
                q.append(temp.left)
            else:
                q.append(temp.right)
        print("Number of nodes is: ",count)

if __name__=='__main__':
    tree=BST()
    lister=[]
    for i in range(12):
        lister.append(r.randint(10,123))
    
    for val in lister:
        tree.insert(val)

    tree.inorder(tree.root)

    print(tree.search(tree.root,97))


