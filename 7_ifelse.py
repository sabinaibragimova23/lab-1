
a = 300
b = 100
if b > a:
    print("b is greater than a")
elif a == b:
    print("a and b are equal")
else:
    print("a is greater than b")  # Output: a is greater than b





a = 10
b = 5
if a > b: print("a is greater than b")  # Output: a is greater than b


 
#  Short Hand If ... Else
a = 10
b = 20
print("A") if a > b else print("B")  # Output: B


# Multiple conditions in one line
a = 100
b = 100
print("A") if a > b else print("=") if a == b else print("B")  # Output: =



a = 150
b = 50
c = 200
if a > b and c > a:
    print("Both conditions are True")  # Output: Both conditions are True



a = 50
b = 150
c = 10
if a > b or a > c:
    print("At least one of the conditions is True")  # Output: At least one of the conditions is True



a = 50
b = 100
if not a > b:
    print("a is NOT greater than b")  # Output: a is NOT greater than b



x = 25
if x > 10:
    print("Above ten,")  # Output: Above ten,
    if x > 20:
        print("and also above 20!")  # Output: and also above 20!
    else:
        print("but not above 20.")



a = 10
b = 20
if b > a:
    pass  # No error
