def palindrome_number(number,newnumber):
    print(number,newnumber)
    if newnumber==0 and number==0:
        print("Yes")
        return True
    if newnumber==0 or number==0:
        return False
    rem1=newnumber%10
    rem2=number%10
    #print(rem1,rem2)
    if rem1!=rem2:
        return False
    palindrome_number(number//10,newnumber//10)

palindrome_number(151,151)