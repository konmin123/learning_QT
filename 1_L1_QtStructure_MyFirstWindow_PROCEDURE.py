import os
import sys

import PySide2
from PySide2 import QtWidgets  # Импорт класса, который содержит элементы окна

dirname = os.path.dirname(PySide2.__file__)
plugin_path = os.path.join(dirname, 'plugins', 'platforms')
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = plugin_path

app = QtWidgets.QApplication()  # Создаем  объект приложения
# app = QtWidgets.QApplication(sys.argv)  # Если PyQt

myWindow = QtWidgets.QWidget()  # Создаём объект окна
myWindow.setWindowTitle("Моя первая программа на PySide")
myWindow.resize(300, 150)

label = QtWidgets.QLabel("<center><strong>!!!ПРИВЕТ!!!</strong></center>")

btn_close = QtWidgets.QPushButton("Закрыть окно")
btn_close.clicked.connect(app.quit)

v_layout = QtWidgets.QVBoxLayout()
v_layout.addWidget(label)
v_layout.addWidget(btn_close)

myWindow.setLayout(v_layout)
print(myWindow.layout())

myWindow.show()  # Показываем окно

sys.exit(app.exec_())  # Если exit, то код дальше не исполняется
