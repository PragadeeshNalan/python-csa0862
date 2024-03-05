n=int(input("enter the number"))
sp=0
sn=0
cp=0
cn=0
while(n!=-1):
  if(n>0):
    cp+=1
    sp+=n
  else:
    cn+=1
    sn+=n
  n=int(input("enter a number"))
if(cn!=0&cp!=0):
  print("avg of negtive is",sn/cn)
  print("avg of positive is",sp/cp)
