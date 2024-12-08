import sys
import random
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QWidget
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect


class Circle:
    def __init__(self, x, y, diameter, color):
        self.x = x
        self.y = y
        self.diameter = diameter
        self.color = color


class CircleDrawer(QWidget):
    def __init__(self):
        super().__init__()
        self.circles = []

    def paintEvent(self, event):
        painter = QPainter(self)
        for circle in self.circles:
            painter.setBrush(circle.color)
            painter.drawEllipse(QRect(circle.x, circle.y, circle.diameter, circle.diameter))

    def add_circle(self):
        x = random.randint(0, self.width() - 50)
        y = random.randint(0, self.height() - 50)
        diameter = random.randint(20, 100)
        color = QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

        new_circle = Circle(x, y, diameter, color)
        self.circles.append(new_circle)

        self.update()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Random Circles")
        self.setGeometry(100, 100, 800, 600)

        self.circle_drawer = CircleDrawer()
        self.setCentralWidget(self.circle_drawer)

        button = QPushButton("Кнопка", self)
        button.clicked.connect(self.circle_drawer.add_circle)
        button.setGeometry(10, 10, 120, 40)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())