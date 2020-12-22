#Medium-03

def Count(x):
    for i in range(len(S)): 
        if S[i].isupper(): 
            v=int(S.index(S[i]))
            return v
        pass

def Cou(y,h):
    for i in range(h+1,y+1):
        #This for loop is for identifying the next CAPITAL letter
        if S[i].isupper():
            m=S.index(S[i])
            return m

S=input("Enter a String: ")
b=Count(S)
g=len(S)
D=Cou(g,b)
if S[b+1:D]!="":
    print(S[b+1:D])
else:
    print("BLANK")