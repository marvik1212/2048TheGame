import random

from GameField import GameField
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QPushButton
from PyQt5.QtGui import QPalette, QColor, QPainter, QPainterPath, QIcon, QFont
from PyQt5.QtCore import Qt
g = GameField()
g.initField()
# g.field[0] = 0
# g.field[4] = 0
# g.field[8] = 2
# g.field[12] = 2
#
# g.field[1] = 4
# g.field[5] = 2
# g.field[9] = 2
# g.field[13] = 4
#
# g.field[2] = 2
# g.field[6] = 4
# g.field[10] = 2
# g.field[14] = 4
# g.printField()
# g.up()
# print()
# print()
# g.printField()
# g.up()
# g.printField()

# class Color(QWidget):
#
#     def __init__(self, color):
#         super(Color, self).__init__()
#         self.setAutoFillBackground(True)
#
#         palette = self.palette()
#         palette.setColor(QPalette.Window, QColor(color))
#         self.setPalette(palette)
#
#
# class MainWindow(QMainWindow):
#
#     def __init__(self):
#         super(MainWindow, self).__init__()
#
#         self.setWindowTitle("My app")
#
#         layout = QGridLayout()
#         obj = Color('grey')
#         w1 = layout.addWidget(obj, 0, 0)
#         layout.addWidget(Color('grey'), 0, 0)
#         layout.addWidget(Color('grey'), 0, 1)
#         layout.addWidget(Color('grey'), 0, 2)
#         layout.addWidget(Color('grey'), 0, 3)
#         layout.addWidget(Color('grey'), 1, 0)
#         layout.addWidget(Color('grey'), 1, 1)
#         layout.addWidget(Color('grey'), 1, 2)
#         layout.addWidget(Color('grey'), 1, 3)
#         layout.addWidget(Color('grey'), 2, 0)
#         layout.addWidget(Color('grey'), 2, 1)
#         layout.addWidget(Color('grey'), 2, 2)
#         layout.addWidget(Color('grey'), 2, 3)
#         layout.addWidget(Color('grey'), 3, 0)
#         layout.addWidget(Color('grey'), 3, 1)
#         layout.addWidget(Color('grey'), 3, 2)
#         layout.addWidget(Color('grey'), 3, 3)
#
#         widget = QWidget()
#         widget.setLayout(layout)
#         self.setCentralWidget(widget)
#
#
# app = QApplication(sys.argv)
#
# window = MainWindow()
# window.show()
# app.exec()

import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget
from PyQt5.QtGui import QKeyEvent


class KeyboardEventApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.gameField = GameField()
        self.gameField.initField()
        self.setWindowTitle("2048")
        self.setWindowIcon(QIcon('logo.jpg'))
        self.setFixedSize(850, 850)
        layout = QGridLayout()
        self.w1 = QPushButton()
        self.w1.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w1.setFont(QFont('Times', 30))
        self.w1.setFixedSize(200, 200)
        self.w2 = QPushButton()
        self.w2.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w2.setFont(QFont('Times', 30))
        self.w2.setFixedSize(200, 200)
        self.w3 = QPushButton()
        self.w3.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w3.setFont(QFont('Times', 30))
        self.w3.setFixedSize(200, 200)
        self.w4 = QPushButton()
        self.w4.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w4.setFont(QFont('Times', 30))
        self.w4.setFixedSize(200, 200)
        self.w5 = QPushButton()
        self.w5.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w5.setFont(QFont('Times', 30))
        self.w5.setFixedSize(200, 200)
        self.w6 = QPushButton()
        self.w6.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w6.setFont(QFont('Times', 30))
        self.w6.setFixedSize(200, 200)
        self.w7 = QPushButton()
        self.w7.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w7.setFont(QFont('Times', 30))
        self.w7.setFixedSize(200, 200)
        self.w8 = QPushButton()
        self.w8.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w8.setFont(QFont('Times', 30))
        self.w8.setFixedSize(200, 200)
        self.w9 = QPushButton()
        self.w9.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w9.setFont(QFont('Times', 30))
        self.w9.setFixedSize(200, 200)
        self.w10 = QPushButton()
        self.w10.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w10.setFont(QFont('Times', 30))
        self.w10.setFixedSize(200, 200)
        self.w11 = QPushButton()
        self.w11.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w11.setFont(QFont('Times', 30))
        self.w11.setFixedSize(200, 200)
        self.w12 = QPushButton()
        self.w12.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w12.setFont(QFont('Times', 30))
        self.w12.setFixedSize(200, 200)
        self.w13 = QPushButton()
        self.w13.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w13.setFont(QFont('Times', 30))
        self.w13.setFixedSize(200, 200)
        self.w14 = QPushButton()
        self.w14.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w14.setFont(QFont('Times', 30))
        self.w14.setFixedSize(200, 200)
        self.w15 = QPushButton()
        self.w15.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w15.setFont(QFont('Times', 30))
        self.w15.setFixedSize(200, 200)
        self.w16 = QPushButton()
        self.w16.setStyleSheet('QPushButton {background-color: #808080; color: White;}')
        self.w16.setFont(QFont('Times', 30))
        self.w16.setFixedSize(200, 200)

        layout.addWidget(self.w1, 0, 0)
        layout.addWidget(self.w2, 0, 1)
        layout.addWidget(self.w3, 0, 2)
        layout.addWidget(self.w4, 0, 3)
        layout.addWidget(self.w5, 1, 0)
        layout.addWidget(self.w6, 1, 1)
        layout.addWidget(self.w7, 1, 2)
        layout.addWidget(self.w8, 1, 3)
        layout.addWidget(self.w9, 2, 0)
        layout.addWidget(self.w10, 2, 1)
        layout.addWidget(self.w11, 2, 2)
        layout.addWidget(self.w12, 2, 3)
        layout.addWidget(self.w13, 3, 0)
        layout.addWidget(self.w14, 3, 1)
        layout.addWidget(self.w15, 3, 2)
        layout.addWidget(self.w16, 3, 3)
        self.widgList = [self.w1, self.w2, self.w3, self.w4, self.w5, self.w6, self.w7, self.w8, self.w9, self.w10, self.w11, self.w12, self.w13, self.w14, self.w15, self.w16]
        self.numAndColor = {'0': '#808080', '2': '#D3D3D3', '4': '#FFD7B5', '8': '#FFB38A',
                            '16': '#FF9248', '32': '#FF6700', '64': '#BE302B', '128': '#F7E948',
                            '256': '#C5BA39', '512': '#7B7424', '1024': '#4A4515', '2048': '#650076'}


        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.connectToGameField()

    def connectToGameField(self):
        tempList1 = self.widgList
        tempList2 = self.gameField.getGameField()
        for i in range(16):
            if tempList2[i] == 0:
                tempList1[i].setText('')
                tempList1[i].setStyleSheet(f"background-color: {self.numAndColor['0']}")
            else:
                tempList1[i].setText(f'{tempList2[i]}')
                tempList1[i].setStyleSheet(f"background-color: {self.numAndColor[str(tempList2[i])]}")

    def keyPressEvent(self, event):
        if event.text() == 'w' or event.text() == 'ц':
            self.gameField.up()
            self.gameField.generateNumOnBoard()
            self.connectToGameField()
        elif event.text() == 's' or event.text() == 'ы':
            self.gameField.down()
            self.gameField.generateNumOnBoard()
            self.connectToGameField()
        elif event.text() == 'a' or event.text() == 'ф':
            self.gameField.left()
            self.gameField.generateNumOnBoard()
            self.connectToGameField()
        elif event.text() == 'd' or event.text() == 'в':
            self.gameField.right()
            self.gameField.generateNumOnBoard()
            self.connectToGameField()


def main():
    app = QApplication(sys.argv)
    window = KeyboardEventApp()
    window.show()
    sys.exit(app.exec_())
main()

