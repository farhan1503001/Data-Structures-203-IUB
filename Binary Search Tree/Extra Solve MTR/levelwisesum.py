class BinaryTreeNode:
    def __init__(self,val) -> None:
        self.data=val
        self.left=None
        self.right=None

class BST:
    def __init__(self) -> None:
        self.root=None
    def insert(self,val):
        newnode=BinaryTreeNode(val)
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


def levelwisesum(root):

    if root==None:
        return 
    else:
        q=[]
        q.append(root)
        q.append("END")
        level=1
        total_sum=0
        temp_sum=0
        while len(q)>1:
            temp=q.pop(0)
            if temp=="END":
                q.append("END")
                
                print(temp_sum,level,total_sum)
                total_sum+=temp_sum
                level=level+1
                temp_sum=0
                continue
            temp_sum+=temp.data*level

            if temp.left!=None:
                q.append(temp.left)
            if temp.right!=None:
                q.append(temp.right)
        total_sum+=temp_sum
        return total_sum
if __name__=='__main__':
    tree=BST()
    lister=[10,7,16,3,9,24,8,25]
    """
    for i in range(12):
        lister.append(r.randint(10,123))
    """
    
    for val in lister:
        tree.insert(val)

    sum=levelwisesum(tree.root)
    print(sum)



