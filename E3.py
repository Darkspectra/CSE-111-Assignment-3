#Easy-03

def come(x):
    L=len(x)
    if L<4:
        return x
    else:
        if "ful" in x:
            return x+"ly"
        if "ful" not in x:
            return x+"ful"
string=input("Enter a String: ")
print(come(string))