class Player:
    def __init__(self, name='player', age = 12):
        self.name       = name
        self.age        = age
        self.attempt    = 0

    def greetPlayer(self):
        print(f'Xin chào {self.name}!')

    def printPlayerDetail(self):
        print(f"""Tên người chơi: {self.name}\n{self.age} tuổi\nSố lần chơi: {self.attempt}""")

    def getPlayerName(self):
        self.name = input('Tên bạn là gì? ')