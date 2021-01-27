import sys

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton
from random import randint


class Example(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 1920, 1080)
        self.setWindowTitle('кто прочитал - тот здохнет')
        self.is_drawing = False
        self.btn = QPushButton('Кнопка', self)
        self.btn.resize(self.btn.sizeHint())
        self.btn.move(960, 590)
        self.qp = QPainter()
        self.btn.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.is_drawing:
            qp = QPainter()
            qp.begin(self)
            self.drawcircle(qp)
            qp.end()

    def paint(self):
        self.is_drawing = True
        self.repaint()

    def drawcircle(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 255), randint(0, 255)))
        a = randint(200, 400)
        qp.drawEllipse(randint(0, 200), randint(0, 200), a, a)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.excepthook = except_hook
    ex.show()
    sys.exit(app.exec())
