import random
randomnumber = random.randint(1,100)
userguess = None
guess = 0
while(userguess != randomnumber):
    userguess = int(input("enter the guess number"))
    guess += 1
    if(randomnumber == userguess):
        print("you guessed it right!")
    else:
        if(userguess>randomnumber):
            print("you guessed it wrong! enter smaller number") 
        else:
             print("you guessed it wrong! enter larger number")        

print(f"you guessed the number in {guess} guesses!")
with open("hiscore.txt","r") as f:
    hiscore = int(f.read())
if(guess<hiscore):
    print("you broken the high score!")
    with open("hiscore.txt","w") as f:
        f.write(str(guess))

