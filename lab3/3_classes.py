#1
class Strings:
    def __init__(self):
        self.input_string = ""  

    def getString(self):
        self.input_string = input("Enter a string: ")

    def printString(self):
        print(self.input_string.upper())

sm = Strings()  
sm.getString()  
sm.printString() 



#2
class Shape:
    def area(self):
        return 0  

class Square(Shape):
    def __init__(self):
        self.length = float(input())

    def area(self):
        return self.length ** 2  

sq = Square()
print(sq.area())




#3
class Rectangle(Shape):
    def __init__(self):
        self.length = float(input("Length"))
        self.width = float(input("Width"))

    def area(self):
        return self.length * self.width  

rect = Rectangle()
print(rect.area())




#4
import math  

class Point:
    def __init__(self):
        self.x = float(input("Enter X coordinate: "))
        self.y = float(input("Enter Y coordinate: "))

    def show(self):
        print(f"({self.x}, {self.y})")

    def move(self):
        self.x = float(input("New X: "))
        self.y = float(input("New Y: "))

    def dist(self, other):
        return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

p1 = Point()
p1.show()

p2 = Point()
p2.show()

print(f"Distance: {p1.dist(p2)}")



#5
class Account:
    def __init__(self):
        self.owner = input("Owner name: ")
        self.balance = float(input("Initial balance: "))

    def deposit(self):
        amount = float(input("Deposit amount: "))
        self.balance += amount
        print(f"New balance: {self.balance}")

    def withdraw(self):
        amount = float(input("Withdraw amount: "))
        if amount <= self.balance:
            self.balance -= amount
            print(f"New balance: {self.balance}")
        else:
            print("Insufficient funds!")

acc = Account()
acc.deposit()
acc.withdraw()

#6
def is_prime(n):
    if n < 2:
        return False
    return all(n % i != 0 for i in range(2, int(n ** 0.5) + 1))

numbers = list(map(int, input("Enter numbers: ").split()))
primes = list(filter(lambda x: is_prime(x), numbers))
print(f"Primes: {primes}")






