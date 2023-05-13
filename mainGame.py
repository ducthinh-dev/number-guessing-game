import random

class numberGuessGame:
    def __init__(self, low = 0, high = 100):
        self.low     = low
        self.high    = high
        self.number  = random.randint(self.low, self.high)
        self.attempt = 0

    def playGame(self):
        guessNumber = int(input(f'Hãy đoán 1 số từ {self.low} đến {self.high}: '))
        self.attempt += 1
        while guessNumber != self.number:
            if guessNumber < self.number:
                print('Số của bạn quá thấp!')
            else:
                print('Bạn đoán cao quá rồi')
            guessNumber = int(input(f'Hãy đoán lại nào: '))
            self.attempt += 1
        if guessNumber == self.number:
            print(f'Chúc mừng! Số {guessNumber} là dự đoán chính xác!')
        return self.attempt