class Player:
    def __init__(self, name='', age = 12):
        self.name       = name
        self.age        = age
        self.attempt    = 0

    def playerName(self):
        return self.name

    def greetPlayer(self):
        print(f'Xin chào {self.name}!')
    
    def getPlayerName(self):
        self.name = input('Tên bạn là gì? ')

    def printPlayerDetail(self):
        print(f"""Tên người chơi: {self.name}\n{self.age} tuổi\nSố lần chơi: {self.attempt}""")

