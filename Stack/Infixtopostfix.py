from parenthesis_balance import stack
operands=['1','2','3','4','5','6','7','8','9','0']
openbr=['(','{','[']
closebr=[')','}',']']
op=['+','-','*','/','^','%']
h_p=['*','/']
l_p=['+','-']
def infix_to_postfix(string):
    s=stack()
    out=""
    for c in string:
        #jodi operator hoy taile output e
        if c in operands:
            out+=c
        elif c in openbr:
            #jodi ( hoy taile stack e
            s.push(c)
        elif c in closebr:
            #jodi close bracket hoy taile jottokhon na first bracket pai stack pop korte hobe
            while s.peek()!=openbr[closebr.index(c)]:
                temp=s.peek()
                if temp in op:
                    out+=temp
                else:
                    pass
                s.pop()
            s.pop()
        elif c in op:
            #jodi c operand hoy
            if c in h_p and s.peek() in h_p:
                #borolok vs borolok thakte parbe na so pop
                temp=s.peek()
                out+=temp
                s.pop()
                s.push(c)
            elif c in l_p and s.peek() in h_p:
                #boroloker barite chotolok so pop
                temp=s.peek()
                out+=temp
                s.pop()
                s.push(c)
            elif c in h_p and s.peek() in l_p:
                #chotoloker barite borolok push
                s.push(c)
            else:
                #naile push
                s.push(c)
    if s.is_empty():
        print(out)
    else:
        #faka na thakle sob pop kore out e dhele dao
        while not s.is_empty():
            val=s.peek()
            out+=val
            s.pop()
        print(out)


if __name__=='__main__':
    infix_to_postfix("(2+3)*5/(2+3)")

