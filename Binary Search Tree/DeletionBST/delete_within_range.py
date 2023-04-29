#just same code ektu format alada
from search import BST,node
def find_min_right(root):
    if root==None:
        return
    curr=root
    while curr.left!=None:
        curr=curr.left

    return curr
def deletion(root,value):
        #ekhon khele dibo
        if root.left==None and root.right==None:
            root=None
            return
        elif root.left==None:
            root=root.right

        elif root.right==None:
            root=root.left
        else:
            min_node=deletion(root.right)
            root.data=min_node.data
            root.right=deletion(root.right)
        return root
def find_value_in_range(root,low,high):
    if root==None:
        return root
    root.left=find_value_in_range(root.left,low,high)
    root.right=find_value_in_range(root.right,low,high)
    if root.data>=low and root.data<=high:
        #ekhon khele dibo
        return deletion(root,root.data)
    return root

if __name__=='__main__':
    tree=BST()
    lister=[12,5,17,3,7,13,1,9]
    for val in lister:
        tree.insert(val)

    tree.inorder(tree.root)
    root=find_value_in_range(tree.root,1,7)
    print()
    tree.inorder(root)
