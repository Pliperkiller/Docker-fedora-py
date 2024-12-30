
from controllers import *

if __name__ == '__main__':
    print("TIKTAKTOE GAME STARTED")
    print("----------------------\n")
    name1 = input("Write player1 name:")
    name2 = input("Write player2 name:")
    gameManager = GameManager(GameController(name1,name2))
    controller = gameManager.gameController 


    while gameManager.inGame:
        print(f'Game start!\n\n Total games: {gameManager.gameNumber}\n {name1} wins: {gameManager.player1Score}\n {name2} wins: {gameManager.player2Score}\n')
        print("----------------------\n")
        controller.printBoard()
        while controller.gameStatus:

            controller.p1Turn = True

            while controller.p1Turn:
                p1 = input(f'\n {controller.player1.name} choose position: ')
                if controller.setPlayer1Values(int(p1)):
                    controller.p1Turn = False
                    controller.p2Turn = True

            while controller.p2Turn:
                p2 = input(f'\n {controller.player1.name} choose position: ')
                if controller.setPlayer1Values(int(p2)):

                    controller.p2Turn = False

            controller.printBoard()
            





