import random

user = input("Please enter your name: ")

matchPlayed = 0
userWin = 0
computerWin = 0
drawMaches = 0
while userWin < 3 and computerWin < 3:
    randomChoice = random.randint(1,3)
    UserInput = input("rock, paper or scissors?: ")
    if UserInput == "rock" and randomChoice == 1:
        drawMaches += 1
        matchPlayed += 1
        print(f"{user}: {userWin}\nComputer: {computerWin}\nDraw matches: {drawMaches}\nMathes played: {matchPlayed}")
    elif UserInput == "rock" and randomChoice == 2:
        computerWin += 1
        matchPlayed += 1
        print(f"{user}: {userWin}\nComputer: {computerWin}\nDraw matches: {drawMaches}\nMathes played: {matchPlayed}")
    elif UserInput == "rock" and randomChoice == 3:
        userWin += 1
        matchPlayed += 1
        print(f"{user}: {userWin}\nComputer: {computerWin}\nDraw matches: {drawMaches}\nMathes played: {matchPlayed}")
        
    if UserInput == "paper" and randomChoice == 1:
        userWin += 1 
        matchPlayed += 1
        print(f"{user}: {userWin}\nComputer: {computerWin}\nDraw matches: {drawMaches}\nMathes played: {matchPlayed}")
    elif UserInput == "paper" and randomChoice == 2:
        drawMaches += 1
        matchPlayed += 1
        print(f"{user}: {userWin}\nComputer: {computerWin}\nDraw matches: {drawMaches}\nMathes played: {matchPlayed}")
    elif UserInput == "paper" and randomChoice == 3:
        computerWin += 1
        matchPlayed += 1
        print(f"{user}: {userWin}\nComputer: {computerWin}\nDraw matches: {drawMaches}\nMathes played: {matchPlayed}")
        
    if UserInput == "scissors" and randomChoice == 1:
        computerWin += 1 
        matchPlayed += 1
        print(f"{user}: {userWin}\nComputer: {computerWin}\nDraw matches: {drawMaches}\nMathes played: {matchPlayed}")
    elif UserInput == "scissors" and randomChoice == 2:
        userWin += 1 
        matchPlayed += 1
        print(f"{user}: {userWin}\nComputer: {computerWin}\nDraw matches: {drawMaches}\nMathes played: {matchPlayed}")
    elif UserInput == "scissors" and randomChoice == 3:
        drawMaches += 1
        matchPlayed += 1
        print(f"{user}: {userWin}\nComputer: {computerWin}\nDraw matches: {drawMaches}\nMathes played: {matchPlayed}")