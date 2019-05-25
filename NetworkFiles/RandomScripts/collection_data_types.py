

# A list is an ordered collection of zero or more references to Python 
# data objects. Lists are written as comma-delimited values enclosed in 
# square brackets. The empty list is simply [ ]. Lists are heterogeneous, 
# meaning that the data objects need not all be from the same class and the 
# collection can be assigned to a variable as below.

myList = [1,2,3,4]
print("list values is equal to ", myList)

#creates a new list of the original list repeated 3 times
print ("this is the output of [list]*3 stored in variable A")
A = [myList]*3  
print ("value of A is ", A)

#Changes the value of list index 2 to 45.
myList[2]=45
print ("changed the value of index 2 in the list. new list values is ", myList)

#Output of A is alse changed since A p
print ("values of A is also changed due to the change done on current list. Value of A is ", A)

myList = [1024, 3, True, 6.5]
print ("New values of list = ", myList)

#append method adds a value to the list
myList.append(False)
print("The value 'false' is added to the list ", myList)

#insert method adds a value in the specified index
myList.insert(2,4.5)
print("the value '4.5' is inserted at index 2 on the list ", myList)

#pop method with empty parameters returns the last value on the list
print("pop the last value on the list - ", myList.pop())
print("this is the updated list values after using pop - ", myList)

#pop method with a parameter returns the value with that index
print(myList.pop(1))
print(myList)
myList.pop(2)
print(myList)
myList.sort()
print(myList)
myList.reverse()
print(myList)
print(myList.count(6.5))
print(myList.index(4.5))
myList.remove(6.5)
print(myList)
del myList[0]
print(myList)