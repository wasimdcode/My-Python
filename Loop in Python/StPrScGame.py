import random
i = 0
user_point=0
computer_point=0
print("------------------------")
print("| Type 'S' for Stone   |")
print("| Type 'P' for Paper   |")
print("| Type 'C' for Scissor |")
print("------------------------")
chances = int(input("| Choose how Many Chances You want to Play --> "))
while i < chances:
    User = input("Please Type Your Answer --> ")
    Computer = random.choice(["Stone","Paper","Scissor"])
    if User == "s" or User == "S":
        User = "Stone"
    elif User == "p" or User == "P" :
        User = "Paper"
    elif User == "c" or User == "C":
        User = "Scissor"
    else:
        print("!! Please Enter Correct Value !!")
    if User == Computer :
        print(f"You --> {User}")
        print(f"Computer --> {Computer}")
        print("--------")
        print("| Draw | !! Both are Same !!")
        print("--------")
    elif User == "Stone" and Computer == "Paper":
        print(f"Your --> {User}")
        print(f"Computer --> {Computer} ")
        print("--------------")
        print("|  You Wins  |")
        print("--------------")
        user_point+=1
    elif User == "Paper" and Computer == "Stone":
        print(f"Your --> {User}")
        print(f"Computer --> {Computer} ")
        print("-----------------")
        print("| Computer Wins |")
        print("-----------------")
        computer_point+=1
    elif User == "Stone" and Computer == "Scissor":
        print(f"Your --> {User}")
        print(f"Computer --> {Computer} ")
        print("--------------")
        print("|  You Wins  |")
        print("--------------")
        user_point+=1
    elif User == "Scissor" and Computer == "Stone":
        print(f"Your --> {User}")
        print(f"Computer --> {Computer} ")
        print("-----------------")
        print("| Computer Wins |")
        print("-----------------")
        computer_point+=1
    elif User == "Paper" and Computer == "Scissor":
        print(f"Your --> {User}")
        print(f"Computer --> {Computer} ")
        print("-----------------")
        print("| Computer Wins |")
        print("-----------------")
        computer_point+=1
    elif User == "Scissor" and Computer == "Paper":
        print(f"Your --> {User}")
        print(f"Computer --> {Computer} ")
        print("--------------")
        print("|  You Wins  |")
        print("--------------")
        user_point+=1
    i += 1
print()
if user_point == computer_point:
    print("--------------------------------------")
    print("| !!! Draw Both Have Same Points !!! |")
    print("--------------------------------------")
    print(f"User's Point -> {user_point} || Computer's Point -> {computer_point}")
elif user_point > computer_point:
    print("-----------------------")
    print("| You Win the Game !! |")
    print("-----------------------")
    print(f"User's Point -> {user_point} || Computer's Point -> {computer_point}")
else:
    print("----------------------------")
    print("| Computer Win the Game !! |")
    print("| You Lose !!!!!!!!!!!!!!! |")
    print("----------------------------")
    print(f"User's Point -> {user_point} || Computer's Point -> {computer_point}")