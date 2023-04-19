from search import BST, node

def largest_even_find(root):
    if root==None:
        return
    else:
        q=[]
        q.append(root)
        max_even=None
        while len(q)!=0:
            temp=q.pop(0)
            if temp.data%2==0:
                if max_even==None:
                    max_even=temp.data
                elif max_even<temp.data:
                    max_even=temp.data
                else:
                    pass
            if temp.left:
                q.append(temp.left)
            if temp.right:
                q.append(temp.right)
        print("Maximum even number is: ",max_even)
        return max_even
def even_largest_main(root):
    arr=[]
    largest_even_rec(root,arr)
    if len(arr)==0:
        print("Not found")
    else:
        print("maximum even is: ",max(arr))
        return max(arr)
def largest_even_rec(root,arr):
    if root==None:
        return
    largest_even_rec(root.left,arr)
    if root.data%2==0:
        arr.append(root.data)
    largest_even_rec(root.right,arr)
    
if __name__=="__main__":
    tree=BST()
    lister=[5,3,2,8,12,9,7,11]
    for val in lister:
        tree.insert(val)
    res=largest_even_find(tree.root)
    print("Result is: ",res)
    #using recursion
    res1=even_largest_main(tree.root)
    print("Result is: ",res1)