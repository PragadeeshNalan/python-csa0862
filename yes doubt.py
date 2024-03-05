stk=eval(input("enter a dictionary:"))
l=[]
def push(stk):
    for i in stk:
        if stk[i]=='asia':
            l.append(i)
def pop(l):
    while stk!=[] and l!=[]:
        print(l.pop())
push(stk)
pop(l)
