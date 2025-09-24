'''
1 for stone
-1 for paper
0 for scissors
'''
import random
computer = random.choice([-1 ,0 ,1])
youstr =input("Enter your choice :")
youDict={"s": 1, "p": -1, "c":0}
reverseDict ={1:"stone", -1:"paper", 0:"scissors"}
you = youDict[youstr]

print(f"You chose {reverseDict[you]}\ncomputer chose {reverseDict[computer]}")
if(computer==you):
    print("It's a Draw!")
else:
    if(computer ==-1 and you ==1):
        print("You win!")

    elif(computer ==-1 and you ==0):
        print("You win")

    elif (computer==1 and you==-1):
        print("You win!")

    elif(computer==1 and you==0):
        print("You win!")

    elif(computer ==0 and you ==-1):
        print("You win!")

    elif(computer==0 and you ==1):
        print("You win!")


    else:
        print("Something Went Wrong!")
