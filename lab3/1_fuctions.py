#1
def incredients(grams):
    ounces=28.3495231 * grams
    return ounces



#2
def fahrenheit_to_celsius(fahrenheit):
    celsius = (5 / 9) * (fahrenheit - 32)
    return celsius


#3
def solve(numheads, numlegs):
    for chickens in range(numheads + 1):
        rabbits = numheads - chickens
        if (2 * chickens + 4 * rabbits) == numlegs:
            return chickens, rabbits
    return None, None  


numheads = int(input())
numlegs = int(input())
chickens, rabbits = solve(numheads, numlegs)
if chickens is not None:
    print(f"chickens: {chickens},rabbits: {rabbits}")
else:
    print("No")



#4
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def filter_prime(numbers):
    return [num for num in numbers if is_prime(num)]




#5
def get_permutations(s, step=0):
    if step == len(s):
        print("".join(s))  
        return
    
    for i in range(step, len(s)):
        s_copy = [c for c in s]  
        s_copy[step], s_copy[i] = s_copy[i], s_copy[step]  
        get_permutations(s_copy, step + 1)  

user_input = input("Enter a string: ")
get_permutations(list(user_input))




#6
def reverse_sentence(sentence):
    words = sentence.split()  
    reversed_words = ' '.join(reversed(words))  
    return reversed_words


user_input = input("Enter a sentence: ")
print(reverse_sentence(user_input))



#7
def has_33(nums):
    for i in range(len(nums) - 1):  
        if nums[i] == 3 and nums[i + 1] == 3:  
            return True  
    return False  

print(has_33([1, 3, 3]))  # True
print(has_33([1, 3, 1, 3]))  # False
print(has_33([3, 1, 3]))  # False



#8
def spy_game(nums):
    sequence = [0, 0, 7]
    for num in nums:
        if num == sequence[0]:  
            sequence.pop(0) 
        if not sequence:  
            return True
    return False  

spy_game([1,2,4,0,0,7,5])  #True
spy_game([1,0,2,4,0,5,7])  #True
spy_game([1,7,2,0,4,5,0])  #False



#9
import math

def sphere_volume(radius):
    volume = (4/3) * math.pi * radius**3
    return volume


radius = int(input())
print (sphere_volume(radius))




#10
def unique(nlist):
    unique_list = []
    for item in nlist:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


input_list = input()
result = unique(input_list)
print(result)  
    


#11
def palindrome():
    s = input("Enter a word or phrase: ")
    s = s.replace(" ", "").lower()
    return s == s[::-1]

if palindrome():
    print("It is a palindrome!")
else:
    print("Not a palindrome.")



#12
def histogram(numbers):
    for num in numbers:
        print("*" * num)

numbers=int(input())
print(histogram)



#13
import random

def guess():
    numbers = random.randint(1, 20)
    guesses_count = 0

    name = input("Hello! What is your name?\n")
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")

    while True:
        guess = int(input("Take a guess.\n"))
        guesses_count += 1

       
        if guess < numbers:
            print("Your guess is too low.")
        elif guess > numbers:
            print("Your guess is too high.")
        else:
            print(f"Good job, {name}! You guessed my number in {guesses_count} guesses!")
            break

guess()

