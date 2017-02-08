'''
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s in which the letters occur in alphabetical order. For example, if s = 'azcbobobegghakl', then your program should print

Longest substring in alphabetical order is: beggh

In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
'''
lista=[]
list1=[]
lista.append(s[0])
for i in range(1,len(s)):
    if ord(s[i]) >= ord(s[i-1]):
        lista.append(s[i])
    else :
        list1.append(lista)
        lista=[]
        lista.append(s[i])
list1.append(lista)
high=0;
length=0;
for i in range(len(list1)):
    if len(list1[i]) > length:
        high=i
        length=len(list1[i])
        
subs="".join(list1[high])
print("Longest substring in alphabetical order is: " +subs)
