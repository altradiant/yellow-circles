from PyQt6 import QtWidgets as QtW
from PyQt6 import QtGui as QtG
from PyQt6 import QtCore as QtC
from PyQt6 import uic

from pathlib import Path as plpath

from random import randint

import os, sys


def rpath(obj):
    return os.fspath(plpath(__file__).parent / obj)


class Widget(QtW.QWidget):
    def paintEvent(self, event):
        painter = QtG.QPainter(self)

        painter.setRenderHint(QtG.QPainter.RenderHint.Antialiasing)
        painter.setPen(QtG.QPen(QtG.QColor(255, 255, 0), 1))
        painter.setBrush(QtG.QColor(255, 255, 255, 255))

        def n(mn, mx):
            return randint(mn, mx)
        
        if self.drawArcs:
            for i in range(0, 333):
                r = n(10, 69)
                x, y = n(0, self.width()), n(0, self.width())
                painter.drawArc(x - r, y - r, r, r, 0, 180 * 16 * 2)
        else:
            painter.drawRect(self.rect())

    def __init__(self):
        super().__init__()

        uic.loadUi(rpath('UI.ui'), self)
        self.setWindowTitle('yellow balls')

        self.drawArcs = False

        self.setStyleSheet('background-color: rgb(255, 255, 255);')
        self.setAutoFillBackground(True)
        
        def ok():
            if not self.drawArcs:
                self.drawArcs = True
                self.update()
            else:
                self.drawArcs = False
                self.update()
                self.drawArcs = True
                self.update()

        self.pushButton.clicked.connect(ok)


if __name__ == '__main__':
    app = QtW.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec())