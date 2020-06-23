import sys
import re
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *


class Button:
    def __init__(self, text, display):
        self.b = QPushButton(str(text))
        self.text = text
        self.display = display
        self.b.clicked.connect(lambda: self.handleinput(self.text))

    def handleinput(self, v):
        if v == "=":
            if self.display.text() == "":
                pass
            else:
                final = eval(self.display.text())
                self.display.setText(str(final))
        elif v == "AC":
            self.display.setText("")
        elif v == "DEL":
            self.display.setText(self.display.text()[:-1])
        elif v == "PV":
            cur_value1 = self.display.text()
            new_value1 = re.findall('\\d+', cur_value1)
            pv = new_value1[0]
            self.pv = pv
            print("PV = " + pv)
            self.display.setText("PV=" + new_value1[0])
        elif v == "FV":
            cur_value1 = self.display.text()
            new_value2 = re.findall('\\d+', cur_value1)
            fv = new_value2[0]
            print("FV = " + fv)
            self.display.setText("FV=" + new_value2[0])

        elif v == "I":
            cur_value1 = self.display.text()
            new_value1 = re.findall('\\d+', cur_value1)
            i = new_value1[0]
            print("I = " + i)
            self.display.setText("I=" + new_value1[0])
        elif v == "N":
            cur_value1 = self.display.text()
            new_value1 = re.findall('\\d+', cur_value1)
            n = new_value1[0]
            print("N = " + n)
            self.display.setText("N=" + new_value1[0])

        else:
            cur_value = self.display.text()
            new_value = cur_value + str(v)
            self.display.setText(new_value)


class Application(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Calculator")
        self.falculator()

    def falculator(self):

        grid = QGridLayout()
        display = QLineEdit()
        buttons = ["AC", "DEL", "PV", "FV",
                   7, 8, 9, "*",
                   4, 5, 6, "-",
                   1, 2, 3, "+",
                   0, ".", "=", "I",
                   "N", "CPT"]

        row = 1
        col = 0
        grid.addWidget(display, 0, 0, 1, 4)
        for button in buttons:
            if col > 3:
                col = 0
                row += 1
            F = Button(button, display)
            if button == "N":
                grid.addWidget(F.b, row, col, 1, 3)
                col += 2
            else:
                grid.addWidget(F.b, row, col, 1, 1)
            col += 1

        self.setLayout(grid)
        self.show()


if __name__ == "__main__" :
    app = QApplication(sys.argv)
    window = Application()
    sys.exit(app.exec_())




