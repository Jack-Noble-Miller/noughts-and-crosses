from NACModule import *

# variables
statusVariables = {
    "gamePlaying":True,
    "playersLoggingIn": True ,
    "inGame": False
    }

players = [PlayerProfile(1, "Jack", "Noble-Miller"), PlayerProfile(2, "Layla", "Saunders")]



#main
while statusVariables["gamePlaying"]:
    player1 = None
    player2 = None
    while statusVariables["playersLoggingIn"]:
        player1 = Login(players)
        player2 = Login(players)
        statusVariables["playersLoggingIn"] = False
        statusVariables["inGame"] = True
        newGameInstance = GameInstance(player1,player2) 
    while statusVariables["inGame"]:
        grid = newGameInstance.gird
        grid.Print()
        newGameInstance.grid = grid.Placement(player1, 1)
        result = grid.CheckWin(1)
        if result == True:
            grid.Print()
            print(f"{player1.playerName} has won")
            statusVariables["inGame"] = False
            statusVariables["playersLoggingIn"] = True
            break
        elif result == "Draw":
            grid.Print()
            print("The Game is a draw")
            statusVariables["inGame"] = False
            statusVariables["playersLoggingIn"] = True
            break

        grid.Print()
        newGameInstance.grid = grid.Placement(player2, 2)
        result = grid.CheckWin(2)
        if result == True:
            grid.Print()
            print(f"{player2.playerName} has won")
            statusVariables["inGame"] = False
            statusVariables["playersLoggingIn"] = True
            break
        elif result == "Draw":
            grid.Print()
            print("The Game is a draw")
            statusVariables["inGame"] = False
            statusVariables["playersLoggingIn"] = True
            break
            



