import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic


class UI(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle('ok')
        self.setGeometry(300, 300, 601, 600)

        self.button = QPushButton("Нарисовать круг", self)
        self.button.resize(161, 60)
        self.button.move(220, 480)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.interface = UI()
        self.interface.show()
        self.interface.button.clicked.connect(self.paint)
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.drawEllipse(qp)
            qp.end()

    def drawEllipse(self, qp):
        diameter = randint(10, 250)

        qp.setPen(QPen(Qt.yellow, 5, Qt.SolidLine))
        qp.drawEllipse((self.width() - diameter) // 2, (self.height() - 160 - diameter) // 2, diameter, diameter)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())