from converting_binary import stack,queue

def temparatures(lister):
    st=stack()
    ans=[0 for i in range(len(lister))]
    for i in range(len(lister)):
        if st.is_empty():
            st.push(i)
        else:
            while not st.is_empty() and lister[st.peek()]<lister[i]:
                ans[st.peek()]=i-st.peek()
                st.pop()
            st.push(i)

    #Final result is:
    print(ans)
    return ans

if __name__=='__main__':
    temparatures([35,36,40,32,28,13,45])