# #function to add numbers

# def add(a,b):
#     return a+b
# a=int(input())
# b=int(input())
# print(add(a,b))

# #reverse tring

# def reverse(s):
#     return s[::-1]
# s=input()
# print(reverse(s))

# def palindrome(s):
#     return s==s[::-1]
# s=input()
# print(palindrome(s))
import random

def play_game():
    secret=random.randint(1,100)
    attempts=0

    while True:
        guess=int(input("guess the number:"))
        attempts += 1

        if guess>secret:
            print("Too high")
        elif guess<secret:
            print("Too low")
        else:
            print("correct the secret number is ",secret,"attempts are",attempts)
play_game()