thistuple = ("grape", "orange", "peach")
print(len(thistuple))  # Output: 3

thistuple = ("grape",)
print(type(thistuple))  # Output: <class 'tuple'>


thistuple = ("grape")
print(type(thistuple))  # Output: <class 'str'>

tuple1 = ("apple", "banana", "cherry")  # Строки
tuple2 = (10, 20, 30, 40)  # Целые числа
tuple3 = (True, False, True)  # Логические значения
tuple4 = ("abc", 123, False, "xyz")  # Разные типы
print(tuple4)  # Output: ('abc', 123, False, 'xyz')

thistuple = tuple(("pear", "plum", "peach")) 
print(thistuple)  # Output: ('pear', 'plum', 'peach')


#Access Tuple Items


thistuple = ("grape", "orange", "peach", "plum", "kiwi", "melon", "mango")
print(thistuple[-4:-1])  # Output: ('plum', 'kiwi', 'melon')


thistuple = ("grape", "orange", "peach")
if "grape" in thistuple:
    print("Yes, 'grape' is in the fruits tuple")  
    # Output: Yes, 'grape' is in the fruits tuple


#Update Tuples

x = ("grape", "orange", "peach")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)  
# Output: ('grape', 'kiwi', 'peach')

thistuple = ("grape", "orange", "peach")
y = list(thistuple)
y.append("plum")
thistuple = tuple(y)
print(thistuple)  
# Output: ('grape', 'orange', 'peach', 'plum')


thistuple = ("grape", "orange", "peach")
y = ("plum",)
thistuple += y
print(thistuple)  
# Output: ('grape', 'orange', 'peach', 'plum')


thistuple = ("grape", "orange", "peach")
y = list(thistuple)
y.remove("grape")
thistuple = tuple(y)
print(thistuple)  
# Output: ('orange', 'peach')

thistuple = ("grape", "orange", "peach")
del thistuple
#print(thistuple)


#Unpack Tuples


fruits = ("grape", "orange", "peach")

(purple, yellow, pink) = fruits

print(purple)  # Output: grape
print(yellow)  # Output: orange
print(pink)    # Output: peach


fruits = ("grape", "orange", "peach", "plum", "mango")

(purple, yellow, *others) = fruits

print(purple)  # Output: grape
print(yellow)  # Output: orange
print(others)  # Output: ['peach', 'plum', 'mango']


fruits = ("grape", "orange", "kiwi", "plum", "mango")

(purple, *tropical, last) = fruits

print(purple)    # Output: grape
print(tropical)  # Output: ['orange', 'kiwi', 'plum']
print(last)      # Output: mango


#Loop Tuples

thistuple = ("grape", "orange", "peach")
for i in range(len(thistuple)): 
    print(thistuple[i])  # Output: grape orange peach  


thistuple = ("grape", "orange", "peach")
i = 0
while i < len(thistuple): 
    print(thistuple[i]); i += 1  # Output: grape orange peach  


#Join Tuples

tuple1 = ("a", "b" , "c")
tuple2 = (1, 2, 3)

tuple3 = tuple1 + tuple2
print(tuple3)


fruits = ("apple", "banana", "cherry")
mytuple = fruits * 2
print(mytuple) # Output: ('apple', 'banana', 'cherry', 'apple', 'banana', 'cherry')