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


def maximum_level(root):
    if root==None:
        return 
    else:
        q=[]
        q.append(root)
        #Additional stopper which will indicate each level ending
        level=0
        print("Maximum of {level} is ",root.data)
        q.append("END")
        while len(q)!=0:
            temp=q.pop(0)
            if temp=='END':
                if len(q)!=0:
                    level+=1
                    max=q[0].data
                    for val in q:
                        if val.data>max:
                            max=val.data
                    print(f"Maximum of {level} is {max}")
                q.append("END")
                continue
            if temp.left!=None:
                q.append(temp.left)
            if temp.right!=None:
                q.append(temp.right)


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
    maximum_level(tree.root)
