import os
from random import randint

#============================ MENU ============================
LOW_NUMBER  = 0
HIGH_NUMBER = 100
def playGame():
    number = randint(LOW_NUMBER, HIGH_NUMBER)
    guessNumber = int(input(f'Hãy đoán 1 số từ {LOW_NUMBER} đến {HIGH_NUMBER}: '))
    attempt = 1
    while guessNumber != number:
        if guessNumber < number:
            print('Số của bạn quá thấp!')
        else:
            print('Bạn đoán cao quá rồi')
        guessNumber = int(input(f'Hãy đoán lại nào: '))
        attempt += 1
    if guessNumber == number:
        print(f'Chúc mừng! Số {guessNumber} là dự đoán chính xác!')
    return number, attempt

#============================ GAME ============================
def printMainMenu(playerName = 'Ẩn danh'):
    nameLen = len(playerName)
    print('+----------Menu-----------+')
    for index in range(26):
        if index == 0:
            print('+',end='')
        if index == 25:
            print('+')
            continue
        if index < nameLen:
            print(playerName[index],end='')
        else:
            print(' ',end='')
    print('+-------------------------+')
    print('|Nhập 1 để chơi           |')
    print('|Nhập 2 để xem bảng điểm  |')
    print('|Nhập 0 để thoát          |')
    print('+-------------------------+')
    userChoice = int(input(f'+Nhâp lựa chọn: '))
    return userChoice

def printGameOverMenu():
    print('+----------Menu-----------+')
    print('|Nhập 1 để chơi lại       |')
    print('|Nhập 2 để xem bảng điểm  |')
    print('|Nhập 3 để trở lại menu   |')
    print('|Nhập 0 để thoát          |')
    print('+-------------------------+')
    userChoice = int(input(f'+Nhâp lựa chọn: '))
    return userChoice

#============================ MAIN ============================
if __name__ == '__main__':
    os.system('cls')
    scoreBoard = []
    cursor = printMainMenu()
    os.system('cls')
    while cursor != 0:
        if cursor == 1:
            thisNumber, thisAttempt = playGame()
            scoreBoard.append([thisNumber, thisAttempt])
            cursor = printGameOverMenu()
            os.system('cls')
        if cursor == 3:
            cursor = printMainMenu()
            os.system('cls')