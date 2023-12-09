import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QPen, QColor


class UI:
    def __init__(self, main):
        main.setWindowTitle('ok')
        main.setGeometry(300, 300, 601, 600)

        self.button = QPushButton("Нарисовать круг", main)
        self.button.resize(161, 60)
        self.button.move(220, 480)


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()

        self.interface = UI(self)
        self.show()
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
        diameter = randint(10, 300)

        color = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
        qp.setPen(QPen(color, 5))
        qp.drawEllipse((self.width() - diameter) // 2, (self.height() - 160 - diameter) // 2, diameter, diameter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())