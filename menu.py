class Menu:
    def __init__(self, status = False):
        self.playStatus = status
        self.userChoice = None

    def printMainMenu(self, playerName = 'Ẩn danh'):
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
        self.userChoice = int(input(f'+Nhâp lựa chọn: '))
        return self.userChoice
    
    def printGameOverMenu(self):
        print('+----------Menu-----------+')
        print('+Nhập 1 để chơi lại       +')
        print('+Nhập 2 để trở lại menu   +')
        print('+Nhập 0 để thoát           +')
        print('+-------------------------+')
        self.userChoice = int(input(f'+Nhâp lựa chọn: '))
        return self.userChoice
