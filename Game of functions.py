def suml(l):
    k=len(l)
    s=0
    for i in range (k):
        s=s+l[i]
    return(s)
p=int(input("enter the number elements-"))
o=[]
for i in range(p):
    q=int(input())
    o.append(q)
    
print("entered list",o)
print("sum of list=",suml(o))
