from GameField import GameField
from pyfiglet import figlet_format
g = GameField()
#g.initField()
g.field[0] = 0
g.field[4] = 0
g.field[8] = 2
g.field[12] = 2

g.field[1] = 4
g.field[5] = 2
g.field[9] = 2
g.field[13] = 4

g.field[2] = 2
g.field[6] = 4
g.field[10] = 2
g.field[14] = 4
g.printField()
g.up()
print()
print()
g.printField()
g.up()
g.printField()




