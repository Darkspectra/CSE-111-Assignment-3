#Medium-01

'''def Count(string): 
    upper, lower = 0, 0
    for i in range(len(string)): 
        if string[i].isupper(): 
            upper += 1
        elif string[i].islower(): 
            lower += 1
    if upper>lower:
        return string.upper()
    elif lower>=upper:
        return string.lower()


string=input("Enter a String: ")
print(Count(string))'''

# Another Way_
N = input()
l = len(N)
upper = 0
lower = 0
for i in N:
    if i>="A" and i<="Z":
        upper += 1
    else:
        lower += 1

if upper>lower:
    print(N.upper())
elif lower>=upper:
    print(N.lower())