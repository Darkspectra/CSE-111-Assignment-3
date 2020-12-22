#Medium-04

def Count(string):
  store1 = string.find('too') # This only finds the index of 't'
  store2 = string.find('good') # index of 'g'
  if store2 > store1:
    v = string[store1:(store2+4)]  # Slicing: Store "too good" in v
    string = string.replace(v, 'excellent')
    return string
  else:
    return string

String=input("Enter a String: ")
print(Count(String))

# Another Way
'''S = input()
if 'too good' in S:
    S = S.replace('too good','excellent')
    print(S)
else:
    print(S)'''