#Easy-02

'''def palindromeCheck(x):
    if x==x[::-1]:
        return "True"
    else:
        return "False"
        
store1=input("Enter a name: ")
print(palindromeCheck(store1))'''

# Another way_
def reverse(s): 
  str = "" 
  for i in s: 
    str = i + str
  return str
  
s = input() 
Z = reverse(s)
if s==Z:
    print("Palindrome")
else:
    print("Not Palindrome")