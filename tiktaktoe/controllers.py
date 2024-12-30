
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

class GameController:

    def __init__(self, name1 = 'Player1', name2 = 'Player2'):
        self.player1 = player(name1)
        self.player2 = player(name2)
        self.board = [0]*9
        self.winConditions = [[1,1,1,0,0,0,0,0,0],
                            [0,0,0,1,1,1,0,0,0],
                            [0,0,0,0,0,0,1,1,1],
                            [1,0,0,1,0,0,1,0,0],
                            [0,1,0,0,1,0,0,1,0],
                            [0,0,1,0,0,1,0,0,1],
                            [1,0,0,0,1,0,0,0,1],
                            [0,0,1,0,1,0,1,0,0]]
        self.gameStatus = False

    def printBoard(self):
        for i in range(0, len(self.board), 3):
            print(self.board[i:i+3])
    
    def updateBoard(self):
        for i in range(len(self.board)):
            if self.player1.locs[i] !=0:
                self.board[i] = 1
            elif self.player2.locs[i] !=0:
                self.board[i] = 2

    def setPlayer1Values(self,index):
        if self.player2.locs[index] == 1:
            print("Unable to set this position since player2 is already using it")
            return False
        
        if self.player1.locs[index] == 1:
            print("Unable to set this position since player1 is already using it")
            return False
        else:
            self.player1.setLoc(index)
            return True
        
    def setPlayer2Values(self,index):
        if self.player1.locs[index] == 1:
            print("Unable to set this position since player1 is already using it")
            return False
        
        if self.player2.locs[index] == 1:
            print("Unable to set this position since player2 is already using it")
            return False
        
        else:
            self.player2.setLoc(index)
            return True

    def checkPlayer1Win(self):
        for row in self.winConditions:
            if sum(1 for x, y in zip(self.player1.locs, row) if x == y) ==3:
                self.player1.winStatus = True
                return True
        return False
            
    def checkPlayer2Win(self):
        for row in self.winConditions:
            if sum(1 for x, y in zip(self.player2.locs, row) if x == y) ==3:
                self.player2.winStatus = True
                return True
        return False
        
    def checkGameStatus(self):
        if self.player1 or self.player2:
            self.gameStatus = True

        return self.gameStatus
    
    def resetGame(self):
        self.board = [0]*9
        self.gameStatus = False
        self.player1.resetLoc()
        self.player2.resetLoc()