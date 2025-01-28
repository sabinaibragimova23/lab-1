#Arithmetic Operators

x = 10
y = 3

print(x + y)  # Addition: 13
print(x - y)  # Subtraction: 7
print(x * y)  # Multiplication: 30
print(x / y)  # Division: 3.3333...
print(x % y)  # Modulus: 1 
print(x ** y) # Exponentiation: 1000 
print(x // y) # Floor Division: 3 

#Assignment Operators

x = 5

x += 3   # Same as x = x + 3
print(x) # 8

x -= 2   # Same as x = x - 2
print(x) # 6

x *= 4   # Same as x = x * 4
print(x) # 24

x /= 6   # Same as x = x / 6
print(x) # 4.0

x %= 3   # Same as x = x % 3
print(x) # 1.0

x //= 2  # Same as x = x // 2
print(x) 

x **= 2  # Same as x = x ** 2
print(x) 

x = 7
x &= 3   # Bitwise AND
print(x) # 3

x |= 4   # Bitwise OR
print(x) # 7

x ^= 1   # Bitwise XOR
print(x) # 6

x >>= 1  # Right Shift
print(x) # 3

x <<= 2  # Left Shift
print(x) # 12


#Comparison Operators 

a = 10
b = 20

print(a == b)  # Equal: False
print(a != b)  # Not equal: True
print(a > b)   # Greater than: False
print(a < b)   # Less than: True
print(a >= b)  # Greater than or equal to: False
print(a <= b)  # Less than or equal to: True

#Logical Operators

x = 5
y = 10

print(x > 3 and y < 15)  # True 
print(x > 6 or y < 15)   # True 
print(not (x > 3))       # False

#Identity Operator

a = [1, 2, 3]
b = [1, 2, 3]
c = a

print(a is c)        # True 
print(a is b)        # False 
print(a is not b)    # True
