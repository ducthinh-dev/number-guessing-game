import os
from playerDetail import Player
from mainGame import numberGuessGame
from menu import Menu

if __name__ == '__main__':
    menu = Menu()
    cursor = menu.printMainMenu()
    while cursor != 0:
        game = numberGuessGame()
        if cursor == 1:
            thisAttempt = game.playGame()
            cursor = menu.printGameOverMenu()
        if cursor == 2:
            cursor = menu.printMainMenu()