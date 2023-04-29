from search import BST,node
def find_min_right(root):
    if root==None:
        return
    curr=root
    while curr.left!=None:
        curr=curr.left

    return curr

def delete_values(root,value):
    if root==None:
        return root
    elif root.data<value:
        root.right=delete_values(root.right,value)
    elif root.data>value:
        root.left=delete_values(root.left,value)
    else:
        #ekhon khele dibo
        if root.left==None and root.right==None:
            root=None
            return
        elif root.left==None:
            root=root.right

        elif root.right==None:
            root=root.left
        else:
            min_node=delete_values(root.right)
            root.data=min_node.data
            root.right=delete_values(root.right)
    return root

if __name__=='__main__':
    tree=BST()
    lister=[12,5,17,3,7,13,1,9]
    for val in lister:
        tree.insert(val)

    tree.inorder(tree.root)
    root=delete_values(tree.root,7)
    print()
    tree.inorder(root)
