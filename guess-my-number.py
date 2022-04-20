import random
playing = "y"
startGame = True
while playing != "n":
    if startGame:
        bottomRange = input("Enter Bottom Range: ")
        topRange = input("Enter Top Range: ")
    startGame = False
    randomNum = random.randint(int(bottomRange), int(topRange))
    userNum = int(input("Guess the number between " +
                  bottomRange + " and " + topRange + " : "))
    if userNum == randomNum:
        print("Winner ! yay u win nothing :) ")
        playing = input("Keep Playing ? (y/n) : ")
        if playing == "y":
            startGame = True
    else:
        print("Nope ! try again :( ")
