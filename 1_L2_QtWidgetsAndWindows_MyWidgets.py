import os
import sys

import PySide2
from PySide2 import QtWidgets, QtCore

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class MyWidgets(QtWidgets.QWidget):

    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        self.initUi()

        # self.pushButton.clicked.connect(self.print_something)  # Добавляем слот для сигнала нажатия
        print(self.layout())

    def print_something(self):
        print("Hello")

    def initUi(self):
        layout = QtWidgets.QVBoxLayout()

        # self.pushButton = QtWidgets.QPushButton("Кнопка")
        self.radioButton = QtWidgets.QRadioButton("some text")
        # self.checkBox = QtWidgets.QCheckBox("check box")
        # self.radioButton.setChecked(True)
        self.combo = QtWidgets.QComboBox()
        self.combo.addItems(["abc", "bca"])

        self.slider = QtWidgets.QSlider()
        self.slider.setOrientation(QtCore.Qt.Vertical)

        # layout.addWidget(self.pushButton)
        # layout.addWidget(self.radioButton)
        # layout.addWidget(self.combo)
        layout.addWidget(self.slider)
        self.setLayout(layout)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWidgets()
    myWindow.show()

    app.exec_()
