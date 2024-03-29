#qgz3eyr33u9wvn
#!/usr/bin/python

import sys
from PySide6.QtWidgets import QApplication, QWidget, QPushButton, QGridLayout
from PySide6 import QtGui

class GameButton(QPushButton):
    def __init__(self, status):
        super(GameButton, self).__init__()
        self.status = status
        self.setFont(QtGui.QFont('Arial', 40))
        self.clicked.connect(self.__click)

    def set_buttons(self, buttons):
        self.buttons = buttons

    def __click(self):
        # import pdb; pdb.set_trace()
        if len(self.text()) == 0:
            self.setText(self.status["text"])
            self.__check_win()
            if self.status["text"] == "○":
                self.status["text"] = "×"
            else:
                self.status["text"] = "○"

    def __check_win(self):
        my_index = self.buttons.index(self)
        print(my_index)

        patterns = [
            [0,1,2],
            [3,4,5],
            [6,7,8],
            [0,3,6],
            [1,4,7],
            [2,5,8],
            [0,4,8],
            [2,4,6]
        ]

        for pattern_count  in range(len(patterns)):
            btns : list[GameButton] = [self.buttons[i] for i in patterns[pattern_count]]
            # print(btns)
            result = [btn.text() for btn in btns]
            print(result)
            if result[0] == result[1] == result[2] == "○":
                print("○の勝ち")
                [btn.setStyleSheet("color : #ff0000;") for btn in btns]
                # ボタンの入力を無効にする
                for btn in self.buttons:
                    btn.setEnabled(False)
                # exit()
                # return

        # btns : list[GameButton] = [self.buttons[i] for i in patterns[0]]
        # # print(btns)
        # result = [btn.text() for btn in btns]
        # print(result)
        # if result[0] == result[1] == result[2] == "○":
        #     print("○の勝ち")
        #     [btn.setStyleSheet("color : #ff0000;") for btn in btns]

class MainWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.game_status={}
        self.game_status["text"]="○"
        self.buttons = [GameButton(self.game_status) for _ in range(9)]
        [btn.set_buttons(self.buttons) for btn in self.buttons]
        #self.button.clicked.connect(lambda x: print("Button Clicked, Hello!"))
        layout = QGridLayout()
        for i in range(3):
            for j in range(3):
                layout.addWidget(self.buttons[i*3+j], i, j)
        self.setLayout(layout)

app = QApplication(sys.argv)
mw = MainWidget()
mw.show()
app.exec()