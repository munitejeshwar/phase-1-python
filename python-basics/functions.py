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

def palindrome(s):
    return s==s[::-1]
s=input()
print(palindrome(s))