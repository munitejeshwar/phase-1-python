
#1.Name and age
name=input("Enter your name:")
age=int(input("Enter you age:"))

future_age=age+10
print("Your age after 10 years:",future_age)

#2.simple calculator

a=int(input("Enter the first number:"))
b=int(input("Enter the second name:"))

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Floor Division:", a // b)
print("Remainder:", a % b)

#3.swap

a=int(input())
b=int(input())

temp=a
a=b
b=temp
print(a)
print(b)

a=int(input())
b=int(input())

a,b=b,a
print(a)
print(b)

word="python"

print(word[4])
print(len(word))
print("y" in word)
print("x" in word)