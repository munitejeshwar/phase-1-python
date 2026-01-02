import random
secret_num=random.randint(1,10)

guess = int(input())

if guess== secret_num : 
    print("correct")
else:
    print("the corrrect number is ",secret_num)