import sys
import random
from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.uic import loadUi


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        loadUi("UI.ui", self)
        self.pushButton.clicked.connect(self.add_circle)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        for circle in self.circles:
            painter.setBrush(QtGui.QColor(255, 255, 0))
            painter.drawEllipse(circle)

    def add_circle(self):
        diameter = random.randint(20, 100)
        x = random.randint(0, self.width() - diameter)
        y = random.randint(0, self.height() - diameter)
        circle = QtCore.QRect(x, y, diameter, diameter)
        self.circles.append(circle)
        self.update()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.circles = []
    window.show()
    sys.exit(app.exec())
