from search import BST,node
def num_descendents(root):
    if root==None:
        return 0
    return 1+num_descendents(root.left)+num_descendents(root.right)

def visit_nodes(root):
    if root==None:
        return 0
    visit_nodes(root.left)
    count=num_descendents(root)
    print(f"{root.data} node has {count-1} descendents")
    visit_nodes(root.right)
    
if __name__=="__main__":
    lister=[5,4,13,3,11,27]
    tree=BST()
    for val in lister:
        tree.insert(val)
    visit_nodes(tree.root)