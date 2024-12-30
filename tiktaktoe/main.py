
from controllers import *

if __name__ == '__main__':
    print("TIKTAKTOE GAME STARTED")
    print("----------------------\n")
    name1 = input("Write player1 name:")
    name2 = input("Write player2 name:")
    gameManager = GameManager(GameController(name1,name2))
    controller = gameManager.gameController 


    while gameManager.inGame:
        gameManager.gameNumber +=1
        controller.resetGame()
        print(f'\nGame {gameManager.gameNumber} start!\n\n Total games: {gameManager.gameNumber-1}\n {name1} wins: {gameManager.player1Score}\n {name2} wins: {gameManager.player2Score}\n')
        print("----------------------\n")
        controller.board.printBoard()
        while controller.gameStatus:

            controller.p1Turn = True

            while controller.p1Turn:
                p1 = input(f'\n {controller.player1.name} choose position: ')
                if controller.set_player_value(controller.player1,int(p1)):
                    controller.p1Turn = False
                    controller.p2Turn = True

            controller.board.printBoard()

            if controller.winChecker.checkWin(controller.player1):
                print(f'\n{controller.player1.name} wins!')
                gameManager.player1Score+=1
                break  

            if controller.board.fullBoardCheck():
                print('\nTie! game ended.')
                break

            while controller.p2Turn:
                p2 = input(f'\n {controller.player2.name} choose position: ')
                if controller.set_player_value(controller.player2,int(p2)):
                    controller.p2Turn = False
            
            controller.board.printBoard()

            if controller.winChecker.checkWin(controller.player2):  
                print(f'\n{controller.player2.name} wins!\n')
                gameManager.player2Score+=1
                break


        nextGame = input('\nNext game? y/n: ')
        if str.lower(nextGame)[0] == 'n':break

print('\nGame over')

            





