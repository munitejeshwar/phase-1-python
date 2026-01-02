# #printing 1 to 100
# for i in range(1,101):
#     print(i)
# #sum od nums from 1 to 100:
# total=0
# for i in range(1,101):
#     total+=i
#     print(total)

# #Multiplication Table:
# a=int(input())
# b=int(input())

# print(a,"x",b,"=",a*b)

#counting vowels

text=input("enter text:")
count=0
for ch in text:
    if ch in "aeiouAEIOU":
        count+=1
print(count)