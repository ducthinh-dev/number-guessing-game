import os
from playerDetail import Player
from mainGame import numberGuessGame


if __name__ == '__main__':
    player = Player()
    player.getPlayerName()
    os.system('cls')
    player.greetPlayer()
    game = numberGuessGame()
    attempts = game.mainGame()
    print(f'Bạn đã đoán {attempts} lần!')