def countnumber():
    k=input("Enter the string to find the uppercase letter and lowerletters=")
    count=0
    d={"upper case":0,"lower case":0}
    for i in k:
        if i.isupper():
            d["upper case"]+=1
            
        elif i.islower():
            d["lower case"]+=1
    
            
    
    return(d)

print(countnumber())