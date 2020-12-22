#Easy-01

def vowel(string):
    count=0
    vowels = ('a', 'e', 'i', 'o', 'u')  
    for x in string: 
        if x in vowels: 
            string = string.replace(x, "") 
            count+=1 
    print(string+str(count))
  

string =input("Enter a String: ")
vowel(string.lower())