def reverse_string(k):
    o=len(k)
    
    for i in range (o):
        print(k[o-1-i],end="")
        
    

q=input("enter the string to be reversed-")
print("reversed=",end="")
reverse_string(q)