'''f=open("newfile.txt", "r")
f2=open("newfile.txt", "w")
for i in f:
    if i[0]!="A":
       f2.write(str(i))
f.close()
f2.close()

f2=open("newfile.txt","r")
for i in f2:
    print(i)'''
def longlines():
    fh=open("newfile.txt", "r")
    L= []
    rd=fh.readlines ()
    for i in rd:
         s=i.split()

         if len(s)>10:
            L.append(i)
    print (L, end=" ")
    fh.close()
longlines()

def countvowels():
     fh=open("newfile.txt", "r")
     c=0
     for i in fh.read():
         if i in 'AEIOUaeiou':
           c+=1
     print("count of vowels;", c)
     fh.close()
countvowels ()
