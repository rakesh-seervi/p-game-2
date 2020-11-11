import random

you = input("enter your choice heads or tails: ")
print(f"you have chosen {you}")
if you == 'heads':
    print("computer have chosen tails")
else:
    print("computer have chosen heads")

ran = random.randint(1,2)
if ran == 1:
    result = 'heads' 
elif ran == 2:
    result = 'tails'

print(f"the result is {result}")

if result == you :
    print("Congrats! you won the toss")
else:
    print("Computer have won the toss")  