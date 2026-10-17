import random

jackpot=random.randint(1,100)
guess=int(input("ENter your guessing number:"))

counter=1
while guess !=jackpot:
    if guess < jackpot:
        print('guess higer')
    else:
        print("guess lower")
    guess=int(input("Enter your guessing number:"))
    counter+=1

print("jackpot number is:",jackpot)
print("you guess number is :",guess)
print("correct guess")
print("your guessing attempt is ",counter)

