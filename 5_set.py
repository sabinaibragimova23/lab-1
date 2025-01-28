
thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)  # Output: {'banana', 'cherry', 'apple'}


thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)  # Output: {'banana', 'cherry', 1, 2, 'apple'}

 
thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)  # Output: {False, 'banana', 'cherry', True, 'apple'}


thisset = {"apple", "banana", "cherry"}
print(len(thisset))  # Output: 3

  
set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}
print(type(set1))  # Output: <class 'set'>


thisset = set(("apple", "banana", "cherry"))
print(thisset)  # Output: {'banana', 'cherry', 'apple'}


#Access Set Items

thisset = {"apple", "banana", "cherry"}
for x in thisset:
  print(x)  # Output:cherry banana apple


thisset = {"apple", "banana", "cherry"}
print("banana" in thisset)  # Output: True


thisset = {"apple", "banana", "cherry"}
print("banana" not in thisset)  # Output: False


#Add Set Items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)  # Output: {'apple', 'banana', 'cherry', 'orange'}


thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)  # Output: {'apple', 'banana', 'cherry', 'pineapple', 'mango', 'papaya'}


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)  # Output: {'apple', 'banana', 'cherry', 'kiwi', 'orange'}



#Remove Set Items

thisset = {"apple", "banana", "cherry"}
thisset.remove("banana")
print(thisset)  # Output: {'apple', 'cherry'}


thisset = {"apple", "banana", "cherry"}
thisset.discard("banana")
print(thisset)  # Output: {'apple', 'cherry'}


thisset = {"apple", "banana", "cherry"}
x = thisset.pop() 
print(x)  # Output: (например) 'apple'
print(thisset)  # Output: {'banana', 'cherry'} 


thisset = {"apple", "banana", "cherry"}
thisset.clear()
print(thisset)  # Output: set()


thisset = {"apple", "banana", "cherry"}
del thisset
#print(thisset) 



#Loop Sets

thisset = {"apple", "banana", "cherry"}

for x in thisset:
  print(x) #apple cherry banana


#Join Sets

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1.union(set2)
print(set3)  # Output: {'a', 'b', 'c', 1, 2, 3}


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = set1 | set2
print(set3)  # Output: {'a', 'b', 'c', 1, 2, 3}


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1.union(set2, set3, set4)
print(myset)  # Output: {'a', 'b', 'c', 1, 2, 3, 'John', 'Elena', 'apple', 'bananas', 'cherry'}


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set3 = {"John", "Elena"}
set4 = {"apple", "bananas", "cherry"}
myset = set1 | set2 | set3 | set4
print(myset)  # Output: {'a', 'b', 'c', 1, 2, 3, 'John', 'Elena', 'apple', 'bananas', 'cherry'}


set1 = {"a", "b", "c"}
set2 = {1, 2, 3}
set1.update(set2)
print(set1)  # Output: {'a', 'b', 'c', 1, 2, 3}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.intersection(set2)
print(set3)  # Output: {'apple'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 & set2
print(set3)  # Output: {'apple'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.intersection_update(set2)
print(set1)  # Output: {'apple'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.difference(set2)
print(set3)  # Output: {'banana', 'cherry'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 - set2
print(set3)  # Output: {'banana', 'cherry'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.difference_update(set2)
print(set1)  # Output: {'banana', 'cherry'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1.symmetric_difference(set2)
print(set3)  # Output: {'banana', 'cherry', 'google', 'microsoft'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set3 = set1 ^ set2
print(set3)  # Output: {'banana', 'cherry', 'google', 'microsoft'}


set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}
set1.symmetric_difference_update(set2)
print(set1)  # Output: {'banana', 'cherry', 'google', 'microsoft'}
