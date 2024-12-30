
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

        print(f'Game {gameManager.gameNumber} start!\n\n Total games: {gameManager.gameNumber}\n {name1} wins: {gameManager.player1Score}\n {name2} wins: {gameManager.player2Score}\n')
        print("----------------------\n")
        controller.printBoard()
        while controller.gameStatus:

            controller.p1Turn = True

            while controller.p1Turn:
                p1 = input(f'\n {controller.player1.name} choose position: ')
                if controller.setPlayer1Values(int(p1)):
                    controller.p1Turn = False
                    controller.p2Turn = True

            controller.updateBoard()
            controller.printBoard()

            if controller.checkPlayer1Win():
                print(f'\n{controller.player1.name} wins!')
                gameManager.player1Score+=1
                break  

            while controller.p2Turn:
                p2 = input(f'\n {controller.player2.name} choose position: ')
                if controller.setPlayer2Values(int(p2)):

                    controller.p2Turn = False

            controller.updateBoard()
            controller.printBoard()

            if controller.checkPlayer2Win(): 
                print(f'\n{controller.player2.name} wins!')
                gameManager.player2Score+=1
                break

        

        nextGame = input('Next game? y/n')
        if str.lower(nextGame)[0] == 'n':break



            





