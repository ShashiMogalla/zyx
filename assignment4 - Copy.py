# frequency count of each letter in a string using dictionary
string = input("Enter any string :")
print(string)
l=len(string)
dict={}
for j in range(l):
    letter=string[j]
    dict.update({letter:string.count(letter)})
print(dict)
# to check a list is empty or not
list1 = [23,56,7,26,18,60]
list2=[]
def empty_list(list):
      print(list)
      if(len(list)==0):
          print("The list is empty")
      else:
          print("The list has ", str(len(list)), " elements and it is not empty.")
empty_list(list1)
empty_list(list2)
# function to find biggest number in 3 numbers

def largest(first,second,third):
    if(first>second):
        if(first>third):
            print(str(first), " is the biggest of all")
        else:
            print(str(third), " is the biggest of all")
            # return first
    elif(second>third):
        print(str(second), " is the biggest of all")
    else:
        print(str(third), " is the biggest of all")
# calling the function
f=99
s=458
t=91
largest(f,s,t)
largest(20,61,15)           
#  to display all the UNIQUE elements of the list.
list=[34,53,11,22,"string", 34,11]
print(set(list))
# to count the number of even and odd numbers from the provided list.
alist = [ 56,34,23,56,4,43,6,7,5,34,5,7645,573,23,6,7,5,4,6,7,5634,3454,345,67,32,45]
print("the list has ",len(alist), " elements" )
def count_odd(list):
    count=0
    total=len(list)
    for ind in range(total):
        if(((list[ind])%2) ==1):
            count=count+1
    return count

odds= count_odd(alist)
evens=len(alist)-odds
print("The list has ", odds, " odd numbers and ", evens, " even numbers")

# to display all the numbers from 50 to 1
print(list(range(50,0,-1)))
#  to display all the odd numbers from 20 to 10
print(list(range(20-1,9,-2))) 