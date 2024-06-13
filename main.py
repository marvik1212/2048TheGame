from GameField import GameField


def main():
    print("ПРИВЕТСТВУЮ В ИГРУ 2048!!!! ГОТОВЫ НАЧАТЬ????? (Y/N): ", end='')
    answer = input()
    if answer.lower() == 'n':
        print('ну и иди нахуй отсюда, дура')
        exit()
    while answer.lower() != 'y' and answer.lower() != 'n':
        print('еблан тупорылый здесь только два ответа - Y или N, а теперь нормально: ', end='')
        answer = input()

    if answer.lower() == 'n':
        print('ну и иди нахуй отсюда, дура')
        exit()

    if answer.lower() == 'y':
        g = GameField()
        g.initField()
        while g.getGameField():
            g.printField()
            print('ХОД: ', end='')
            move = input()










if __name__ == '__main__':
    main()
