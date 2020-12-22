#Hard-01

def Count1(x,y):
    v=""
    l=len(x)
    for i in range(l):
        if x[i] in y:
            v=v+x[i]
    return v
def Count(x,y):
    v=""
    l=len(x)
    for i in range(l):
        if x[i] in y:
            v=v+x[i]
    return v

S1=input("Enter a String: ")
S2=input("Enter a String: ")
p=Count1(S1,S2)+Count(S2,S1)
if p!="":
    print(p)
else:
    print("Nothing in common")