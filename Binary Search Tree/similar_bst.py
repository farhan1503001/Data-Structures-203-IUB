from maxineachlevel import BST

def is_similar(root1,root2):
    if root1==None and root2==None:
        return True
    if root1==None and root2!=None:
        return False
    if root1!=None and root2==None:
        return False
    
    if (root1.data==root2.data) and is_similar(root1.left,root2.left) and is_similar(root1.right,root2.right):
        return True
    else:
        return False
    
def is_similarnonrec(root1,root2):
    if root1==None and root2==None:
        return True
    if root1 or root2:
        return False
    q1=[]
    q2=[]
    q1.append(root1)
    q2.append(root2)

    while len(q1)!=0 and len(q2)!=0:
        temp1=q1[0]
        temp2=q2[0]
        if temp1.data!=temp2.data:
            return False
        q1.pop(0)
        q2.pop(0)
        if temp1.left and temp2.left:
            q1.append(temp1.left)
            q2.append(temp2.left)
        elif temp1.left or temp2.left:
            return False
        if temp1.right and temp2.right:
            q1.append(temp1.right)
            q2.append(temp2.right)
        elif temp1.right or temp2.right:
            return False
    return True


if __name__=="__main__":
    tree=BST()
    tree1=BST()
    lister=[5,12,9,7,3,1,2]
    lister1=[5,12,9,7,4,1,2]
    """
    for i in range(12):
        lister.append(r.randint(10,123))
    """
    
    for val in lister:
        tree.insert(val)

    for item in lister1:
        tree1.insert(item)

   # tree.inorder(tree.root)
    res=is_similar(tree.root,tree1.root)
    res1=is_similarnonrec(tree.root,tree1.root)
    print(res1)

        
