#Modules
from os import system
#import sqlite3
#con = sqlite3.connect("PlayerData.db")
#cursor = con.cursor
#Classes
class Grid():
    def __init__(self):
        self.rows = 3
        self.columns = 3
        self.blankSymbol = "#"
        self.grid = []
        for i in range(self.rows):
            sub_grid = [self.blankSymbol]*self.columns
            self.grid.append(sub_grid)
            
    def Placement(self,player,instancePlayerID):
         placed = False
         print(f"{player.playerName}'s turn")
         while placed == False:
             row = int(input("Enter the row you want to place in (1-{self.rows}): "))
             column = int(input("Enter the column you want to place in (1-{self.columns}): "))
             if self.grid[row][column] == self.blankSymbol:
                 if instancePlayerID == 1:
                    self.grid[row-1][column-1] = "X"
                 elif instancePlayerID == 2:
                    self.grid[row-1][column-1] = "O"
                 placed = True
         return self

    def Print(self):
        system('cls')
        for self.rows in self.grid:
            print( " ".join(self.rows))

    def CheckWin(self, instancePlayerID):
         if instancePlayerID == 1:
             s = "X"
         elif instancePlayerID == 2:
             s = "O"
         if (self.grid[0][0]== s and self.grid[1][0]== s and self.grid[2][0]== s) or (self.grid[0][1]== s and self.grid[1][1]== s and self.grid[2][1]== s) or (self.grid[0][2]== s and self.grid[1][2]== s and self.grid[2][2]== s):
             return True
         elif (self.grid[0][0] == s and self.grid[0][1]== s and self.grid[0][2]== s) or (self.grid[1][0]== s and self.grid[1][1]== s and self.grid[1][2]== s) or (self.grid[2][0]== s and self.grid[2][1]== s and self.grid[2][2]== s):
             return True
         elif (self.grid[0][0] == s and self.grid[1][1] == s and self.grid[2][2] == s):
             return True
         elif (self.grid[0][2] == s and self.grid[1][1] == s and self.grid[2][0] == s):
             return True  
         else:
             draw = True
             for row in self.grid:
                 for column in row:
                     if column == "#":
                         draw = False
             if draw:
                 return "Draw"
             else:
                 return False
         
class PlayerProfile:
    def __init__(self, ID: int, name:str, password:str):
        self.playerID = ID
        self.playerName = name
        self.playerPassword = password

class GameInstance():
    def __init__(self, player1: PlayerProfile, player2: PlayerProfile):
        self.player1ID = player1
        self.player2ID = player2
        self.gird = Grid()

#Subprograms
def Login(players) -> PlayerProfile:
    loggedIn = False
    while loggedIn == False:
        username = str(input("Enter your username: "))
        for testPlayerProfile in players:
            while testPlayerProfile.playerName == username:
                password = str(input("Enter your password: "))
                if testPlayerProfile.playerPassword == password:
                    username = None
                    loggedIn = True
                    return testPlayerProfile
        if loggedIn == False:
            print("error logging in, please try again.")




#main
if __name__ == "__main__":
    print("NACModule is running as main")
