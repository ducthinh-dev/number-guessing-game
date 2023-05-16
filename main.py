import os
from random import randint

#============================ FUNC ============================
def spaceFill(value, space):
    value = str(value)
    valueLen = len(value)
    result = ''
    for index in range(space):
        if index < valueLen:
            result += value[index]
        else:
            result += ' '
    return result

#============================ MENU ============================
LOW_NUMBER  = 0
HIGH_NUMBER = 100
DEFAULT_MAX_ATTEMPT = 1000
def playGame(maxAttempt = DEFAULT_MAX_ATTEMPT):
    number = randint(LOW_NUMBER, HIGH_NUMBER)
    attempt = 1
    guessNumber = int(input(f'Hãy đoán 1 số từ {LOW_NUMBER} đến {HIGH_NUMBER}: '))
    while guessNumber != number:
        if guessNumber < number:
            print('Số của bạn quá thấp!')
        else:
            print('Bạn đoán cao quá rồi')
        attempt += 1
        if attempt > maxAttempt:
            print(f'Game over! Bạn đã sử dụng quá lượt đoán!')
            return number, -1
        print(f'Lần đoán thứ {attempt}.')
        guessNumber = int(input(f'Hãy đoán lại nào: '))
    if guessNumber == number:
        os.system('cls')
        print(f'Chúc mừng! Số {guessNumber} là dự đoán chính xác!')
    return number, attempt

#============================ GAME ============================
def printMainMenu(playerName = 'Ẩn danh'):
    nameLen = len(playerName)
    print('+----------Menu-----------+')
    for index in range(26):
        if index == 0:
            print('|',end='')
        if index == 25:
            print('|')
            continue
        if index < nameLen:
            print(playerName[index],end='')
        else:
            print(' ',end='')
    print('+-------------------------+')
    print('|Nhập 1 để chơi           |')
    print('|Nhập 2 để xem bảng điểm  |')
    print('|Nhập 3 để cài đặt        |')
    print('|Nhập 0 để thoát          |')
    print('+-------------------------+')
    userChoice = int(input(f'>Nhập lựa chọn: '))
    return userChoice

def printGameOverMenu():
    print('+-------GAME CLEARED------+')
    print('|Nhập 1 để chơi lại       |')
    print('|Nhập 2 để xem bảng điểm  |')
    print('|Nhập 3 để cài đặt        |')
    print('|Nhập 4 để trở lại menu   |')
    print('|Nhập 0 để thoát          |')
    print('+-------------------------+')
    userChoice = int(input(f'>Nhập lựa chọn: '))
    return userChoice

def printScoreBoard(scores):
    records = []
    for index, score in enumerate(scores):
        record = '|' + spaceFill(index + 1, 3) + '|' + spaceFill(score[0], 6) + '|' + spaceFill(score[1], 14) + '|'
        records.append(record)
        
    print('+---+----SCORE BOARD------+')
    print('|   |Đáp án|Số lần đoán   |')
    print('+---+---------------------+')
    for record in records:
        print(record)
    print('+---+---------------------+')
    print('+-------------------------+')
    print('|Nhập 3 để trở lại menu   |')
    print('|Nhập 0 để thoát          |')
    print('+-------------------------+')
    userChoice = int(input(f'>Nhập lựa chọn: '))
    return userChoice

def printSetting():
    print('+---------SETTING---------+')
    print('+-------------------------+')
    userChoice = int(input(f'>Nhập lựa chọn: '))
    return userChoice

#============================ MAIN ============================
if __name__ == '__main__':
    os.system('cls')
    scores = []
    cursor = printMainMenu()
    os.system('cls')
    while cursor != 0:
        if cursor == 1:
            thisNumber, thisAttempt = playGame()
            if thisAttempt == -1:
                scores.append([thisNumber, 'Lost'])
            else:
                scores.append([thisNumber, thisAttempt])
            cursor = printGameOverMenu()
            os.system('cls')
        if cursor == 2:
            cursor = printScoreBoard(scores)
            os.system('cls')
        if cursor == 3:
            pass
        if cursor == 4:
            cursor = printMainMenu()
            os.system('cls')