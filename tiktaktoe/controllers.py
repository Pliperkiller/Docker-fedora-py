
class player:

    def __init__(self, name):
        self.name = name
        self.winStatus = False
        self.locs = [0]*9

    def setLoc(self,index):
        self.locs[index] = 1

    def resetLoc(self):
        self.locs = [0]*9

    def setWin(self):
        self.winStatus = True
    
    def resetWinStatus(self):
        self.winStatus = False


class WinChecker:
    def __init__(self):
        self.winConditions = [[1,1,1,0,0,0,0,0,0],
                            [0,0,0,1,1,1,0,0,0],
                            [0,0,0,0,0,0,1,1,1],
                            [1,0,0,1,0,0,1,0,0],
                            [0,1,0,0,1,0,0,1,0],
                            [0,0,1,0,0,1,0,0,1],
                            [1,0,0,0,1,0,0,0,1],
                            [0,0,1,0,1,0,1,0,0]]

    def checkWin(self,player):
        for row in self.winConditions:
            if sum(1 for x, y in zip(player.locs, row) if x == y and y==1) ==3:
                player.winStatus = True
                return True
        return False



class Board:
    def __init__(self):
        self.cells = [0]*9
    
    def update(self, player1, player2):
        for i in range(len(self.cells)):
            if player1.locs[i] !=0:
                self.cells[i] = 1
            if player2.locs[i] !=0:
                self.cells[i] = 2
    
    def printBoard(self):
        for i in range(0, len(self.cells), 3):
            print(self.cells[i:i+3])

    def fullBoardCheck(self):
        if len([cell for cell in self.cells if cell !=0]) == 9: return True
        return False


class GameController:

    def __init__(self, name1 = 'Player1', name2 = 'Player2'):
        self.player1 = player(name1)
        self.player2 = player(name2)
        self.board = Board()
        self.winChecker = WinChecker()
        self.gameStatus = True
        self.p1Turn = False
        self.p2Turn = False

    def updateBoard(self):
        self.board.update(self.player1,self.player2)

    def set_player_value(self, player, index):
        opponent = self.player2 if player == self.player1 else self.player1
        if opponent.locs[index] == 1 or player.locs[index] == 1:
            print(f"Unable to set this position as it is already selected.")
            return False
        player.setLoc(index)
        self.board.update(self.player1, self.player2)
        return True

    def checkWin(self,player):
        return self.winChecker.checkWin(player)
          
    
    def resetGame(self):
        self.board = Board()
        self.gameStatus = True
        self.player1.winStatus = False
        self.player2.winStatus = False
        self.player1.resetLoc()
        self.player2.resetLoc()


class GameManager:
    def __init__(self, gameController):
        self.player1Score = 0
        self.player2Score = 0
        self.gameNumber = 0
        self.gameController = gameController
        self.inGame = True