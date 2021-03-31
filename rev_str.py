#reverse a given string

print("Enter any string : ")
str=input()
l=len(str)
print("Length of string : ",l)
print("Reversed string : ")
rev=''
for ch in range(0,len(str)):
    rev=rev+str[l-(ch+1)]
print(rev)
       