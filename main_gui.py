import sys
from GameField import GameField
from PyQt5.QtWidgets import QGridLayout, QPushButton, QMessageBox
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget


class KeyboardEventApp(QMainWindow):

    def generateButtonWidget(self) -> QPushButton:
        temp = QPushButton()
        temp.setStyleSheet('QPushButton {background-color: #808080;}')
        temp.setFont(QFont('Times', 40))
        temp.setFixedSize(250, 250)
        return temp

    def __init__(self):
        super().__init__()

        self.gameField = GameField()
        self.gameField.initField()
        self.setWindowTitle("2048. WASD To Move")
        self.setWindowIcon(QIcon('logo.jpg'))
        self.setFixedSize(1000, 1000)
        layout = QGridLayout()

        self.w1 = self.generateButtonWidget()
        self.w2 = self.generateButtonWidget()
        self.w3 = self.generateButtonWidget()
        self.w4 = self.generateButtonWidget()
        self.w5 = self.generateButtonWidget()
        self.w6 = self.generateButtonWidget()
        self.w7 = self.generateButtonWidget()
        self.w8 = self.generateButtonWidget()
        self.w9 = self.generateButtonWidget()
        self.w10 = self.generateButtonWidget()
        self.w11 = self.generateButtonWidget()
        self.w12 = self.generateButtonWidget()
        self.w13 = self.generateButtonWidget()
        self.w14 = self.generateButtonWidget()
        self.w15 = self.generateButtonWidget()
        self.w16 = self.generateButtonWidget()

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
        if self.gameField.isGameOver():
            self.popup_defeat()

        if self.gameField.checkFor2048():
            self.popup_win()

        if event.text() == 'w' or event.text() == 'ц':
            self.gameField.up()
            self.gameField.generateNumOnBoard()
        elif event.text() == 's' or event.text() == 'ы':
            self.gameField.down()
            self.gameField.generateNumOnBoard()
        elif event.text() == 'a' or event.text() == 'ф':
            self.gameField.left()
            self.gameField.generateNumOnBoard()
        elif event.text() == 'd' or event.text() == 'в':
            self.gameField.right()
            self.gameField.generateNumOnBoard()
        self.connectToGameField()


    def popup_defeat(self):
        msg = QMessageBox()
        msg.setWindowTitle("Yo")
        msg.setText("You lost!")
        msg.setIcon(QMessageBox.Critical)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()
        exit()

    def popup_win(self):
        msg = QMessageBox()
        msg.setWindowTitle("Yo")
        msg.setText("Congratulations!! You won!")
        msg.setIcon(QMessageBox.Information)
        msg.setStandardButtons(QMessageBox.Ok)
        msg.exec_()

def main():
    app = QApplication(sys.argv)
    window = KeyboardEventApp()
    window.show()
    sys.exit(app.exec_())
main()

