import random


class GameField:
    field: list
    gameFlag: bool
    bigNums: int
    choiceList: list
    choiceListTwo: list

    def __init__(self):
        temp = []
        for i in range(16):
            temp.append(0)
            '''
            temp = [[], [], [], []  0 1 2 3
                    [], [], [], []  4 5 6 7
                    [], [], [], []  8 9 10 11
                    [], [], [], []] 12 13 14 15
            '''
        self.field = temp
        self.choiceList = [2, 4]
        self.choiceListTwo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.bigNums = 0
        self.gameFlag = True


    def isFieldFilled(self) -> bool:
        counter = 0
        for i in range(4):
            for j in range(4):
                if self.field != 0:
                    counter += 1
        return True if counter == 16 else False

    def getBigNumsOnBoard(self) -> int:
        return self.bigNums

    def incrementBigNumsOnBoard(self) -> None:
        self.bigNums += 1

    def getGameField(self) -> list:
        return self.field

    def initField(self) -> None:
        firstplace = random.choice(self.choiceListTwo)
        secondplace = random.choice(self.choiceListTwo)
        firstnum = random.choice(self.choiceList)
        secondnum = random.choice(self.choiceList)
        while firstplace == secondplace:
            firstplace = random.choice(self.choiceListTwo)
            secondplace = random.choice(self.choiceListTwo)
        self.field[firstplace] = firstnum
        self.field[secondplace] = secondnum

    def printField(self) -> str:
        tempList = [3, 7, 11, 15]
        for i in range(16):
            if self.getGameField()[i] == 0:
                print('[] '.ljust(5), end='')
            else:
                print(f'[{self.getGameField()[i]}] '.ljust(5), end='')
            if i in tempList:
                print()
        print()


