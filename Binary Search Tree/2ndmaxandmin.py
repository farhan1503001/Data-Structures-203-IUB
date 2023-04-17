import random as r
class node:
    def __init__(self,data) -> None:
        self.data=data
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

    def inorder(self,root):
        current=root
        if current==None:
            return
        self.inorder(current.left)
        print(current.data)
        self.inorder(current.right)

#Here we will use queue to print out all nodes
def level_order_traversal(root):
    #Here print all the label nodes
    if root==None:
        return
    else:
        #Now we will create a queue
        q=[]
        #Now insert the root inside it
        q.append(root)
        save_list=[]
        
        while q:
            q_len=len(q)
            while q_len>0:
                #print the shit#THEN add new shit
                node=q.pop(0)
                print(node.data,end=" ")
                save_list.append(node.data)
                if node.left!=None:
                    q.append(node.left)
                if node.right!=None:
                    q.append(node.right)
                q_len=q_len-1
         
                print("")
        #Now code for finding second max 
        has_list=set(save_list)
        has_list.remove(max(has_list))
        print(max(has_list))
        #Now code for second min
        h_list=set(save_list)
        h_list.remove(max(h_list))
        print(min(h_list))

if __name__=='__main__':
    tree=BST()
    lister=[5,12,9,7,3,1,2]
    """
    for i in range(12):
        lister.append(r.randint(10,123))
    """
    
    for val in lister:
        tree.insert(val)

    #tree.inorder(tree.root)
    level_order_traversal(tree.root)


