def squres(n):
    for i in range(n+1):
        yield i**2

n=int(input())
for num in squres(n):
    print(num,end=" ")



def even(n):
    for i in range(0,n+1,2):
        yield  i

n =int(input())
for num in even(n):
    print(num,ens=" ")



def divisible(n):
    for i in range(n + 1):
        if i % 3 == 0 and i % 4 == 0:
            yield i


n = int(input("Enter a number: "))
for num in divisible(n):
    print(num, end=" ")




def squares(a, b):
    for i in range(a, b + 1):
        yield i ** 2


a = int(input("Enter start number: "))
b = int(input("Enter end number: "))

for square in squares(a, b):
    print(square)




def countdown(n):
    for i in range(n, -1, -1):
        yield i


n = int(input("Enter a number: "))
for num in countdown(n):
    print(num, end=" ")
    

