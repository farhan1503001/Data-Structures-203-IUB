def powerset(string,idx,set):
    if idx==len(string):
        print(set)
        return
    powerset(string,idx+1,set+string[idx])
    print("yes",set)
    print("size,",idx)
    powerset(string,idx+1,set)

powerset("abc",0,"")
