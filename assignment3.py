# to demonstrate all the string methods 
string1 = "I am learning Data Science with Python"
len(string1)
string2='Science'
#slicing to get the remaining part of the string leaving the first 5 chars
print(string1[5:])
#changing the format of the strings
print(string1.upper())
print(string2.lower())
# to capitalize the first character of the string2
print(string2.capitalize())
# to check whether the string is in lower case or upper case
print(string1.islower())
string3=string1.lower()
print(string3.islower())
print(string2.isupper()) # only first letter is upper case, so false
# separating the words from the string into a list
words_list=string3.split(" ")
print(words_list)
print(string2.center(50))
print(words_list[2].center(50,"*"))
# printing with template string 
template = " {} and {} are builtin datatypes of {}"

print(template.format("strings", "lists", "Python"))
print(template.format("pointers","structures", "C"))
# to search for a substring in a string
location= string1.find(string2)
if(location>=0):
    print(string2+" is found at",+location)
else:
    print("not found")  
location=string1.find(string3)
if(location>=0):
    print(string3+"is found at",+location)
else:
    print(string3+" is not found")
# string concatenation
string4=string2+ " and Technology"
print(string4)
# frequency count of each letter of the english alphabet in a string
alphabet=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for i in range(26):
    c=alphabet[i]
    st=string1.count(c)
    print("Frequency of "+ c +" is "+ str(st))
    
    
# Applying all List methods
list1=[30,50,110,40,300,280]
list1.append(80)
print("List elements are :", list1)
list1.append(150)
list1.append(40)
print("List elements are :", list1)
list1.extend([250,130,46,40])
print("List elements are :", list1)
# number of occurences of 40 in the list1
print(list1.count(40))
# list.insert(where to insert, what to insert)
list1.insert(0,65)
print("List elements are :", list1)
list1.insert(4,200)
print("List elements are :", list1)
# removing members at specific index of a list
list1.pop()    
print("List elements are :", list1)
list1.pop(4)    
print("List elements are :", list1)
# removing specific members of a list
list1.remove(110)
print("List elements are :", list1)
# changing the order of the members in a list
list1.reverse()
print("List elements are :", list1)
list1.sort()
print("List elements are :", list1)
list1.remove(40) # duplicates removed
print("List elements are :", list1)


# all the dictionary methods
index = {"term1": 28,"term2": 68,"term3": 25,"term4": 21,"term5": 12}
# list of keys
print(index.keys())
#  list of values
print(index.values())
# list of items
print(index.items())
# to get the valu of a specific key
print(index.get("term3"))
# removing items from the dictionary
index.pop("term1")
print(index)
# adding more data by merging without duplicates
supplement = {"term6": 58,"term8": 60,"term1": 15,"term3": 25}
index.update(supplement)
print(index)


# methods associated with sets
set1={61,22,13,10,48,30} 
set2={48,23,64,10,40}
set3={30,72,61,23}
# set operations 
set1.intersection(set2)
set4=set1.union(set2)
set4
s1=set1&set3
s2=set2 | set3
s2
set5=set1-set2
set5
set6=set1^set2 # symmmetric difference
set6
# superset checking
if (set4>=set2):
    print ("set4 is the superset of set2")
if (set2.issubset(set3)):
    print("set2 is subset of set3")
if (set2.isdisjoint(set3)):
    print("set2 is disjoint to set 3")
    








