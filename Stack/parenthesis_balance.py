class stack:
    def __init__(self) -> None:
        self.data=[]
    def push(self,item):
        self.data.append(item)
    def is_empty(self):
        if len(self.data)==0:
            return True
        else:
            return False
    def peek(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            return self.data[-1]
    def pop(self):
        if self.is_empty():
            print("Stack is empty")
            return
        else:
            return self.data.pop()

def parenthesis_balance(string):
    p1=stack()
    for c in string:
        if c=='(' or c=='{' or c=='[':
            p1.push(c)
        else:
            last_item=p1.peek()
            if (c==')' and last_item!='(') or(c=='}' and last_item!='{') or (c==']' and last_item!='['):
                print("Brackets are not balanced")
                return
            else:
                p1.pop()
    if p1.is_empty():
        print("Brackets are balanced")
    else:
        print("Brackets are not balanced")



if __name__=="__main__":
    string=str(input("Enter the string: "))
    parenthesis_balance(string)
