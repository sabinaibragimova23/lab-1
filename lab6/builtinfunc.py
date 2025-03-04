#1
from functools import reduce

numbers = input().split()
numbers = map(float, numbers)
product = reduce(lambda x, y: x * y, numbers)
print(f"Product: {product}")




#2
text = input()

upper_count = sum(1 for char in text if char.isupper())
lower_count = sum(1 for char in text if char.islower())

print(f"lower: {upper_count}")
print(f"upper: {lower_count}")




#3
text = input()

cleaned_text = ''.join(char.lower() for char in text if char.isalnum())
is_palindrome = cleaned_text == cleaned_text[::-1]

if is_palindrome:
    print("YES")
else:
    print("NO")





#4
import time
import math

number = float(input())
delay = int(input())

time.sleep(delay / 1000.0)
sqrt_result = math.sqrt(number)

print(f"Square root of {number} after {delay} miliseconds is {sqrt_result}")





#5

elements = input().split()
elements = tuple(map(int, elements))

all_true = all(elements)

if all_true:
    print("All True")
else:
    print("All False")

