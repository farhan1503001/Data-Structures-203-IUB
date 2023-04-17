from search import BST
from search import node
#Cousin's level are similar but but parent's are different
def level(root,key,l):
    if root==None:
        return 0
    
    if root.data==key:
        return l
    #prothome bame jabo
    l_level=level(root.left,key,l+1)
    #jodi bame na thake taile l_level 0 hobe
    if l_level>0:
        return l_level
    r_level=level(root.right,key,l+1)
    if r_level>0:
        return r_level
    
def sibling(root,a,b):
    if root==None:
        return False
    
    return (
            (root.left==a and root.right==b) or  (root.left==b and root.right==a) or sibling(root.left,a,b) or sibling(root.right,a,b)
            )

def cousin(root,a,b):
    #sibling na but same level e
    if (level(root,a,1)==level(root,b,1)) and (sibling(root,a,b)!=True):
        return True
    else:
        return False

#Driver code
if __name__=="__main__":
    lister=[5,7,3,9,8,11,4,1,25]
    tree=BST()
    for val in lister:
        tree.insert(val)

    node1=tree.root.left.right
    node2=tree.root.left.left
    res=sibling(tree.root,node1,node2)
    print(res)


