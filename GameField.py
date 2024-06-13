import random

class GameField:
    field: list
    gameFlag: bool
    bigNumsCounter: int
    choiceList: list
    choiceListTwo: list

    def __init__(self):
        temp = []
        for i in range(16):
            temp.append(0)
            '''
            temp = [0, 0, 0, 0   0 1 2 3
                    0, 0, 0, 0   4 5 6 7
                    0, 0, 0, 0   8 9 10 11
                    0, 0, 0, 0]  12 13 14 15
            '''
        self.field = temp
        self.choiceList = [2, 4]
        self.choiceListTwo = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
        self.bigNumsCounter = 0
        self.gameFlag = True


    def isFieldFilled(self) -> bool:
        counter = 0
        for i in range(4):
            for j in range(4):
                if self.field != 0:
                    counter += 1
        return True if counter == 16 else False

    def getBigNumsOnBoard(self) -> int:
        return self.bigNumsCounter

    def incrementBigNumsOnBoard(self) -> None:
        self.bigNumsCounter += 1

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

    def printField(self):
        tempStr = ''
        tempList = [3, 7, 11, 15]
        for i in range(16):
            if self.getGameField()[i] == 0:
                tempStr += '[ ] '
            else:
                tempStr += f'[{self.getGameField()[i]}] '
            if i in tempList:
                print(tempStr.ljust(5))
                tempStr = ''
        print()

    def moveFunc(self, a, b, c, d): # 0 = f[a], 1 = f[b], 2 = f[c], 3 = f[d], ГДЕ a - клетка притяжения
        f = self.getGameField()
        # Логика функции - линейная обработка всех кейсов. Сначала рассматриваются случаи, когда есть что складывать
        while True:
            if f[a] == f[b] and f[a] != 0 and f[b] != 0:  #1
                f[a] = f[b] * 2
                f[b] = 0
                if f[c] == f[d] and f[c] != 0 and f[d] != 0:
                    f[b] = f[c] * 2
                    f[c] = 0
                    f[d] = 0
                    break
                else:
                    f[b] = f[c]
                    f[c] = f[d]
                    f[d] = 0
                    break

            if f[a] == f[c] and f[a] != 0 and f[c] != 0: #2
                if f[b] == 0:
                    f[a] = f[c] * 2
                    f[b] = f[d]
                    f[c] = 0
                    f[d] = 0
                    break

            if f[a] == f[d] and f[a] != 0 and f[d] != 0: #3
                if f[b] == 0 and f[c] == 0:
                    f[a] = f[d] * 2
                    f[d] = 0
                    break

            if f[b] == f[c] and f[b] != 0 and f[c] != 0: #4
                if f[a] != 0:
                    f[b] = f[c] * 2
                    f[c] = f[d]
                    f[d] = 0
                    break
                else:
                    f[a] = f[c] * 2
                    f[b] = f[d]
                    f[d] = 0
                    break

            if f[b] == f[d] and f[b] != 0 and f[d] != 0: #5
                if f[c] == 0:
                    if f[a] != 0:
                        f[b] = f[d] * 2
                        f[d] = 0
                        break
                    else:
                        f[a] = f[d] * 2
                        f[d] = 0
                        break

            if f[c] == f[d] and f[c] != 0 and f[d] != 0: #6
                if f[a] != 0 and f[b] != 0:
                    f[c] = f[d] * 2
                    f[d] = 0
                    break
                if f[a] != 0 and f[b] == 0:
                    f[b] = f[d] * 2
                    f[d] = 0
                    f[b] = 0
                    break
                if f[a] == 0 and f[b] != 0:
                    f[a] = f[b]
                    f[b] = f[d] * 2
                    f[c] = 0
                    f[d] = 0
                    break
                if f[a] == 0 and f[b] == 0:
                    f[a] = f[d] * 2
                    f[c] = 0
                    f[d] = 0
                    break
                # Далее идут кейсы, когда складывать нечего и нужно просто сделать сдвиг
            else:
                # One zero (amount of bitches rn)
                if f[a] == 0 and f[b] != 0 and f[c] != 0 and f[d] != 0: #1
                    f[a] = f[b]
                    f[b] = f[c]
                    f[c] = f[d]
                    f[d] = 0
                    break
                if f[a] != 0 and f[b] == 0 and f[c] != 0 and f[d] != 0: #2
                    f[b] = f[c]
                    f[c] = f[d]
                    f[d] = 0
                    break
                if f[a] != 0 and f[b] != 0 and f[c] == 0 and f[d] != 0: #3
                    f[c] = f[d]
                    f[d] = 0
                    break
                if f[a] != 0 and f[b] != 0 and f[c] != 0 and f[d] != 0: #4
                    break
                # Two zeros
                if f[a] == 0 and f[b] == 0 and f[c] != 0 and f[d] != 0: #5
                    f[a] = f[c]
                    f[b] = f[d]
                    f[c] = 0
                    f[d] = 0
                    break
                if f[a] == 0 and f[b] != 0 and f[c] != 0 and f[d] == 0: #6
                    f[a] = f[b]
                    f[b] = f[c]
                    f[c] = 0
                    break
                if f[a] != 0 and f[b] != 0 and f[c] == 0 and f[d] == 0: #7
                    break
                if f[a] != 0 and f[b] == 0 and f[c] != 0 and f[d] == 0: #8
                    f[b] = f[c]
                    f[c] = 0
                    break
                if f[a] == 0 and f[b] != 0 and f[c] == 0 and f[d] != 0: #9
                    f[a] = f[b]
                    f[b] = f[d]
                    f[d] = 0
                    break
                if f[a] != 0 and f[b] == 0 and f[c] == 0 and f[d] != 0: #10
                    f[b] = f[d]
                    f[d] = 0
                    break
                # Three zeros
                if f[a] == 0 and f[b] == 0 and f[c] == 0 and f[d] != 0: #11
                    f[a] = f[d]
                    f[d] = 0
                    break
                if f[a] == 0 and f[b] == 0 and f[c] != 0 and f[d] == 0: #12
                    f[a] = f[c]
                    f[c] = 0
                    break
                if f[a] == 0 and f[b] != 0 and f[c] == 0 and f[d] == 0: #13
                    f[a] = f[b]
                    f[b] = 0
                    break
                if f[a] != 0 and f[b] == 0 and f[c] == 0 and f[d] == 0: #14
                    break
                # Four zeros
                elif f[a] == 0 and f[b] == 0 and f[c] == 0 and f[d] == 0: #15
                    break
                break

    def up(self):
        self.moveFunc(0, 4, 8, 12)
        self.moveFunc(1, 5, 9, 13)
        self.moveFunc(2, 6, 10, 14)
        self.moveFunc(3, 7, 11, 15)







