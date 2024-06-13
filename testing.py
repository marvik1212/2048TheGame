from GameField import GameField
from pyfiglet import figlet_format
g = GameField()
g.initField()
s = ''
for i in g.field:
    s += str(i)
print(figlet_format("[  4  ]     [  2  ]     [  128  ]", font="big"))
input()



