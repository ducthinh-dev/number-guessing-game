import os
from random import randint

if os.name == "nt":
    clearCommand = 'cls'
else:
    clearCommand = 'clear'


LOW_NUMBER = 0
HIGH_NUMBER = 100
DEFAULT_MAX_ATTEMPT = 1000
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
def playGame(low_number = LOW_NUMBER, high_number = HIGH_NUMBER, maxAttempt = DEFAULT_MAX_ATTEMPT):
    number = randint(low_number, high_number)
    attempt = 1
    print(f'Bạn có {maxAttempt} lần đoán!')
    guessNumber = int(input(f'Hãy đoán 1 số từ {low_number} đến {high_number}: '))
    while guessNumber != number:
        if guessNumber < number:
            print('Số của bạn quá thấp!')
        else:
            print('Bạn đoán cao quá rồi')
        attempt += 1
        if attempt > maxAttempt:
            os.system(clearCommand)
            print(f'Game over! Bạn đã sử dụng quá lượt đoán!')
            print(f'Đáp án chính xác là {number}.')
            return number, -1
        print(f'Lần đoán thứ {attempt}.')
        guessNumber = int(input(f'Hãy đoán lại nào: '))
    if guessNumber == number:
        os.system(clearCommand)
        print(f'Chúc mừng! Số {guessNumber} là dự đoán chính xác!')
    return number, attempt

#============================ GAME ============================
def printMainMenu(playerName = 'Ẩn danh'):
    print('+----------Menu-----------+')
    print(f'|Xin chào, {spaceFill(playerName, 15)}|')
    print('+-------------------------+')
    print('|Nhập 1 để chơi           |')
    print('|Nhập 2 để xem bảng điểm  |')
    print('|Nhập 3 để cài đặt        |')
    print('|Nhập 0 để thoát trò chơi |')
    print('+-------------------------+')
    userChoice = int(input(f'>Nhập lựa chọn: '))
    return userChoice

def printGameOverMenu():
    print('\n')
    print('+-------GAME CLEARED------+')
    print('|Nhập 1 để chơi lại       |')
    print('|Nhập 2 để xem bảng điểm  |')
    print('|Nhập 3 để cài đặt        |')
    print('|Nhập 4 để trở lại menu   |')
    print('|Nhập 0 để thoát trò chơi |')
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
    print('|Nhập 3 để cài đặt        |')
    print('|Nhập 4 để trở lại menu   |')
    print('|Nhập 0 để thoát trò chơi |')
    print('+-------------------------+')
    userChoice = int(input(f'>Nhập lựa chọn: '))
    return userChoice

def printSettings(low_number, high_number, default_max_attempt):
    userChoice = -1
    while userChoice != 4:
        if userChoice == -1:
            print('+---------SETTINGS--------+')
            print('|Nhập 1 để cài đặt giá trị|')
            print('|Nhập 2 để cài đặt số lần |')
            print('|đoán                     |')
            print('|Nhập 4 để trở lại menu   |')
            print('+-------------------------+')
            userChoice = int(input(f'>Nhập lựa chọn: '))
            os.system(clearCommand)
        if userChoice == 1:
            print('+---------SETTINGS--------+')
            print(f'|Giá trị bé nhất: {spaceFill(low_number, 8)}|')
            print(f'|Giá trị lớn nhất: {spaceFill(high_number, 7)}|')
            print('+-------------------------+')
            low_number = int(input(f'>Nhập giá trị bé nhất: '))
            high_number = int(input(f'>Nhập giá trị lớn nhất: '))
            userChoice = -1
            os.system(clearCommand)
        if userChoice == 2:
            print('+---------SETTINGS--------+')
            print(f'|Số lần đoán: {spaceFill(default_max_attempt, 12)}|')
            print('+-------------------------+')
            default_max_attempt = int(input(f'>Nhập số lần đoán: '))
            userChoice = -1
            os.system(clearCommand)
    return userChoice, low_number, high_number, default_max_attempt

#============================ MAIN ============================
if __name__ == '__main__':
    low_number  = LOW_NUMBER
    high_number = HIGH_NUMBER
    default_max_attempt = DEFAULT_MAX_ATTEMPT
    os.system(clearCommand)
    scores = []
    playerName = input('Xin chào! Bạn tên là gì? ')
    os.system(clearCommand)
    cursor = printMainMenu(playerName)
    os.system(clearCommand)
    while cursor != 0:
        if cursor == 1:
            thisNumber, thisAttempt = playGame(low_number, high_number, default_max_attempt)
            if thisAttempt == -1:
                scores.append([thisNumber, 'Lost'])
            else:
                scores.append([thisNumber, thisAttempt])
            cursor = printGameOverMenu()
            os.system(clearCommand)
        if cursor == 2:
            cursor = printScoreBoard(scores)
            os.system(clearCommand)
        if cursor == 3:
            cursor, low_number, high_number, default_max_attempt = printSettings(low_number, high_number, default_max_attempt)
            os.system(clearCommand)
        if cursor == 4:
            cursor = printMainMenu(playerName)
            os.system(clearCommand)