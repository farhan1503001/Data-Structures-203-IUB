def min_rec(arr,min,i=0):
    if i==len(arr):
        print(min)
        return min
    if min>arr[i]:
        min=arr[i]
    min_rec(arr,min,i+1)
if __name__=='__main__':
    list=[1,6,4,-3,5,2]
    min_rec(list,list[0],0)