from GameField import GameField
import sys

def main():
    print("Welcome to 2048. Ready to start? (Y/N): ", end='')
    answer = input()
    if answer.lower() == 'n':
        print('ok then')
        exit()
    while answer.lower() != 'y' and answer.lower() != 'n':
        print('Invalid answer, try again (Y/N): ', end='')
        answer = input()

    if answer.lower() == 'n':
        print('ok then')
        exit()

    if answer.lower() == 'y':
        g = GameField()
        g.initField()
        while g.getGameFlag():
            print(g.printField())
            print('Move: ', end='')
            move = input()

            if move.lower() == 'up':
                g.up()
            elif move.lower() == 'down':
                g.down()
            elif move.lower() == 'left':
                g.left()
            elif move.lower() == 'right':
                g.right()
            else:
                print('Invalid move, try again')
                continue

            if g.checkFor2048():
                print('Gratz, you won!')
                g.setGameFlag(False)

            elif g.isGameOver():
                print('game over')
                g.setGameFlag(False)

            g.generateNumOnBoard()

main()
