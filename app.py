from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import numpy as np
from copy import deepcopy
import random
from sorts import *
import cv2

def toPixmap(img):
    h, w, ch = img.shape
    img = QImage(img.tobytes(), w, h, ch*w, QImage.Format_RGB888)
    return QPixmap.fromImage(img)

class VisualLabel(QLabel):
    def __init__(self):
        super().__init__()
        self.setMinimumSize(600, 600)
        self.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter)

        self.algo = bubble
        self.datagen(20)
        self.create_animation(self.algo)
        self.setPixmap(QPixmap())

    def datagen(self, n):
        self.data = [[i+1, (255, 255, 255)] for i in range(n)]
        random.shuffle(self.data)
        self.create_animation(self.algo)

    def create_animation(self, algo):
        self.algo = algo
        self.animation = self.algo(deepcopy(self.data))

    def run(self):
        while True:
            try:
                frame = next(self.animation)
            except StopIteration:
                self.animation = self.algo(deepcopy(self.data))
                continue

            n = len(frame)
            img = np.zeros((n, n, 3), dtype=np.uint8)
            for i in range(n):
                cv2.rectangle(img, (i, n-frame[i][0]), (i, n-1), frame[i][1])

            pixmap = toPixmap(img)
            pixmap = pixmap.scaled(self.width(), self.height())
            self.setPixmap(pixmap)

            loop = QEventLoop()
            speed = self.parent().parent().tools_label.speed.value()
            QTimer.singleShot(1000//speed, loop.quit)
            loop.exec_()

class ToolsLabel(QWidget):
    def __init__(self):
        super().__init__()
        self.setMinimumWidth(100)
        self.setMaximumWidth(200)
        self.setLayout(QGridLayout())
        self.layout().setAlignment(Qt.AlignTop)

        combo = QComboBox()
        combo.addItems(['bubble', 'selection', 'insertion'])
        combo.currentTextChanged.connect(
            lambda x: self.parent().parent().visual_label.create_animation(globals()[combo.currentText()])
        )
        self.layout().addWidget(QLabel('Algorithm'), 0, 0)
        self.layout().addWidget(combo, 0, 1)

        n_box = QSpinBox()
        n_box.setRange(2, 500)
        n_box.setValue(20)
        n_box.textChanged.connect(
            lambda: self.parent().parent().visual_label.datagen(n_box.value())
        )
        self.layout().addWidget(QLabel('Items'), 1, 0)
        self.layout().addWidget(n_box, 1, 1)

        self.speed = QSlider()
        self.speed.setRange(1, 100)
        self.speed.setValue(5)
        self.layout().addWidget(QLabel('Speed'), 2, 0)
        self.layout().addWidget(self.speed, 2, 1)

class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Sorting Visualizer')

        self.visual_label = VisualLabel()
        self.tools_label = ToolsLabel()

        wid = QWidget()
        wid.setLayout(QHBoxLayout())
        wid.layout().addWidget(self.visual_label, stretch=75)
        wid.layout().addWidget(self.tools_label, stretch=25)

        self.setCentralWidget(wid)
        self.show()
        self.visual_label.run()

    def closeEvent(self, event):
        super().closeEvent(event)
        exit()
