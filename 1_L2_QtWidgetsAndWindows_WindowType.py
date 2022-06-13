import os
import sys

import PySide2
from PySide2 import QtCore, QtWidgets, QtGui

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path


class MyWindowType(QtWidgets.QMainWindow):

    def __init__(self, parent=None):
        super(MyWindowType, self).__init__(parent)

        # ссылка на документацию https://doc.qt.io/qt-5/qt.html#WindowType-enum

        self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint)  # Неизменяемое окно
        # self.setWindowFlags(QtCore.Qt.MSWindowsFixedSizeDialogHint | QtCore.Qt.FramelessWindowHint)  # Неизменяемое окно без рамок
        # self.setWindowFlags(QtCore.Qt.FramelessWindowHint)  # Окно без полей
        # self.setWindowFlags(QtCore.Qt.WindowTitleHint)  # Окно со строкой заголовка


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    myWindow = MyWindowType()
    # myWindow.setWindowFlag(QtCore.Qt.Popup)
    # myWindow.move(100, 100)
    myWindow.show()

    app.exec_()
