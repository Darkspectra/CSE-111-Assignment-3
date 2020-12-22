#Hard-02

# WITH FUNCTION
def Count(x,y):
    if x==y:
        if x in S[3:(L-3)]:
            return x
        else:
            return "Not Palindrome Substring"
        
S=input("Enter a String: ")
L=len(S)
St1=S[-3:]
St2=S[0:3]
print(Count(St1,St2))


# WITHOUT FUNCTION
'''S=input()
L=len(S)
S_store=""
S_rev=S[::-1]
for i in range(len(S)):
    if S[0]!=S_rev[i]:
        S_store=S_store+S_rev[i]
    elif S[0]==S_rev[i]:
        S_store=S_store+S_rev[i]
        break
    
First_S = S_store[::-1]
F=len(First_S)
if First_S==S[0:F]:
    if First_S in S[F:(L-F)]:
        print(First_S)
    else:
        print("Not Palindrome Substring")'''