#Hard-03

def Count(x):
    l, u, p, d = 0, 0, 0, 0
    for i in x: 
        if (i.islower()): 
            l+=1            
        if (i.isupper()): 
            u+=1            
        if (i.isdigit()): 
            d+=1            
        if(i=='@'or i=='$' or i=='_'): 
            p+=1
            
    if (l>=1 and u>=1 and p>=1 and d>=1):
        return "OK"
    elif l!=0 and u==0 and d==0 and p==0:
        return "Uppercase character missing, Digit missing, Special character missing"
    elif l==0 and u!=0 and d==0 and p==0:
        return "Lowercase character missing, Digit missing, Special character missing"
    elif l==0 and u==0 and d!=0 and p==0:
        return "Lowercase character missing, Uppercase charecter missing, Special character missing"
    elif l==0 and u==0 and d==0 and p!=0:
        return "Lowercase character missing, Uppercase charecter missing, Digit missing"
    elif l!=0 and u!=0 and d==0 and p==0:
        return "Digit missing, Special character missing"
    elif l!=0 and u==0 and d==0 and p!=0:
        return "Uppercase character missing, Digit missing"
    elif l!=0 and u==0 and d!=0 and p==0:
        return "Uppercase character missing, Special character missing"
    elif l==0 and u!=0 and d!=0 and p==0:
        return "Lowercase character missing, Special character missing"
    elif l==0 and u!=0 and d==0 and p!=0:
        return "Lowercase character missing, Digit missing"
    elif l==0 and u==0 and d!=0 and p!=0:
        return "Lowercase character missing, Uppercase character missing"
    elif l==0 and u!=0 and d!=0 and p!=0:
        return "Lowercase character missing"
    elif l!=0 and u==0 and d!=0 and p!=0:
        return "Uppercase character missing"
    elif l!=0 and u!=0 and d==0 and p!=0:
        return "Digit missing"
    elif l!=0 and u!=0 and d!=0 and p==0:
        return "Special character missing"
        
S=input("Enter a Password: ")
L=len(S)
if L>=9:
    print(Count(S))
else:
    print("Enter at least 9 charecters")