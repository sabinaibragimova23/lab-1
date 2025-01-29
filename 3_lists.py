thislist = ["apple", "banana", "cherry", "apple", "cherry"]
print(thislist)

thislist = ["apple", "banana", "cherry"]
print(len(thislist))#number of elements

list1 = ["abc", 34, True, 40, "male"]


mylist = ["apple", "banana", "cherry"]
print(type(mylist))


thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)


#Access Items

thislist = ["apple", "banana", "cherry"]
print(thislist[-1])


thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:5])#"cherry", "orange", "kiwi"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[:4])#"apple", "banana", "cherry", "orange"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[2:])#"cherry", "orange", "kiwi", "melon", "mango"

thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(thislist[-4:-1])#"orange", "kiwi", "melon"


thislist = ["apple", "banana", "cherry"]
if "apple" in thislist: #Check if "apple" is present in the list:
  print("Yes, 'apple' is in the fruits list")


#Change Item Value

list1 = ["apple", "banana", "cherry"]
list1[1] = "blueberry"
print(list1)  # ['apple', 'blueberry', 'cherry']

list2 = ["apple", "banana", "cherry", "orange", "kiwi"]
list2[2:4] = ["grape", "pear"]
print(list2)  # ['apple', 'banana', 'grape', 'pear', 'kiwi']


list3 = ["apple", "banana", "cherry"]
list3[1:2] = ["blackcurrant", "watermelon"]
print(list3)  # ['apple', 'blackcurrant', 'watermelon', 'cherry']


list4 = ["apple", "banana", "cherry"]
list4[1:3] = ["watermelon"]
print(list4)  # ['apple', 'watermelon', 'cherry']


list5 = ["apple", "banana", "cherry"]
list5.insert(3, "watermelon")
print(list5)  # ['apple', 'banana', 'cherry', 'watermelon']



#Add List Items
list1 = ["grape", "pear", "plum"]
list1.append("watermelon")  # ['grape', 'pear', 'plum', 'watermelon']


list2 = ["grape", "pear", "plum"]
list2.insert(2, "pineapple")  # ['grape', 'pear', 'pineapple', 'plum']


list3 = ["grape", "pear", "plum"]
berries = ["strawberry", "blueberry", "raspberry"]
list3.extend(berries)  # ['grape', 'pear', 'plum', 'strawberry', 'blueberry', 'raspberry']

list4 = ["grape", "pear", "plum"]
fruit_tuple = ("fig", "dragonfruit")
list4.extend(fruit_tuple)  # ['grape', 'pear', 'plum', 'fig', 'dragonfruit']


# Remove List Items

list1 = ["grape", "orange", "peach"]
list1.remove("orange")  # ['grape', 'peach']
print(list1)

list3 = ["grape", "orange", "peach"]
list3.pop(2)  # ['grape', 'orange']
print(list3)

list5 = ["grape", "orange", "peach"]
del list5[1]  # ['grape', 'peach']
print(list5)

list7 = ["grape", "orange", "peach"]
list7.clear()  # []
print(list7)


#Loop Lists

thislist = ["grape", "melon", "peach"]
for x in thislist:
    print(x)  # grape melon peach


thislist = ["grape", "melon", "peach"]
for i in range(len(thislist)):
    print(thislist[i])  # grape melon peach


thislist = ["grape", "melon", "peach"]
i = 0
while i < len(thislist):
    print(thislist[i])  #  grape melon peach
    i += 1


thislist = ["grape", "melon", "peach"]
[print(x) for x in thislist]  # grape melon peach



#List Comprehension


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)


numbers = list(range(11))
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [0, 2, 4, 6, 8, 10]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
upper_case_fruits = [x.upper() for x in fruits]
print(upper_case_fruits)  # Output: ['APPLE', 'BANANA', 'CHERRY', 'KIWI', 'MANGO']


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
replaced_fruits = [x if x != "banana" else "orange" for x in fruits]
print(replaced_fruits)  # Output: ['apple', 'orange', 'cherry', 'kiwi', 'mango']


squares = [x**2 for x in range(1, 6)]
print(squares)  # Output: [1, 4, 9, 16, 25]


numbers = range(1, 8)
modified_numbers = [x**2 if x % 2 == 0 else x for x in numbers]
print(modified_numbers)  # Output: [1, 4, 3, 16, 5, 36, 7]


tuples = [(x, x**2) for x in range(1, 6)]
print(tuples)  # Output: [(1, 1), (2, 4), (3, 9), (4, 16), (5, 25)]


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if x != "apple"]
print(newlist) #['banana', 'cherry', 'kiwi', 'mango']


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist) #['apple', 'orange', 'cherry', 'kiwi', 'mango']


#Sort Lists


fruits = ["pear", "apple", "grape", "peach", "banana"]
fruits.sort()
print(fruits)  # Output: ['apple', 'banana', 'grape', 'peach', 'pear']


numbers = [45, 10, 78, 32, 5]
numbers.sort()
print(numbers)  # Output: [5, 10, 32, 45, 78]


fruits = ["pear", "apple", "grape", "peach", "banana"]
fruits.sort(reverse=True)
print(fruits)  # Output: ['pear', 'peach', 'grape', 'banana', 'apple']


def close_to_30(n):
    return abs(n - 30)

numbers = [40, 10, 25, 35, 5]
numbers.sort(key=close_to_30)
print(numbers)  # Output: [25, 35, 40, 10, 5]


words = ["Zebra", "apple", "Orange", "banana"]
words.sort(key=str.lower)
print(words)  # Output: ['apple', 'banana', 'Orange', 'Zebra']


#Copy

thislist = ["pear", "grape", "peach"]
mylist = thislist.copy()
print(mylist)  # Output: ['pear', 'grape', 'peach']


thislist = ["pear", "grape", "peach"]
mylist = list(thislist)
print(mylist)  # Output: ['pear', 'grape', 'peach']


thislist = ["pear", "grape", "peach"]
mylist = thislist[:]
print(mylist)  # Output: ['pear', 'grape', 'peach']


#Join Lists

list1 = ["x", "y", "z"]
list2 = [10, 20, 30]

for item in list2:
    list1.append(item)

print(list1)  # Output: ['x', 'y', 'z', 10, 20, 30]


list1 = ["x", "y", "z"]
list2 = [10, 20, 30]

list1.extend(list2)

print(list1)  # Output: ['x', 'y', 'z', 10, 20, 30]


