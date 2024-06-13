from GameField import GameField

g = GameField()
g.initField()
s = ''
for i in g.field:
    s += str(i)
print(s)