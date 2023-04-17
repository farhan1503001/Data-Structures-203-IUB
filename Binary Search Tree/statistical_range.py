from search import BST,node

def statistical_range(root):
    #First e min ber koro 
    if root==None:
        return
    min_curr=root
    while min_curr.left!=None:
        min_curr=min_curr.left
    max_curr=root
    while max_curr.right!=None:
        max_curr=max_curr.right

    print("statistical range: ",max_curr.data-min_curr.data)
    return max_curr.data-min_curr.data