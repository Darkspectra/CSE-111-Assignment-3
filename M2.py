#Medium-02

'''def Count(x):
        if x.isalpha(): 
            return "WORD"
        elif x.isdigit():
            return "NUMBER"
        else:
            return "MIXED"
  
string = input("Enter a String: ")
print(Count(string))'''

# Another Way_
S = input()
l = len(S)
C=0
for i in S:
    if i>="A" and i<="Z" or i>="a" and i<="z":
        C+=1
if C==l:
    print("WORD")
elif C==0:
    print("NUMBER")
else:
    print("MIXED")