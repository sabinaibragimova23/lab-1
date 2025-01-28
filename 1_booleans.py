print(10 > 9)
print(10 == 9)
print(10 < 9)


print(bool("Hello"))
print(bool(15))


bool("abc") #Any string is True, except empty strings.
bool(123) #Any number is True, except 0.
bool(["apple", "cherry", "banana"]) #Any list, tuple, set, and dictionary are True, except empty ones.


def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

