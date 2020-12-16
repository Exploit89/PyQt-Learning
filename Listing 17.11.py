# Выполнение длительной операции
from PyQt5 import QtWidgets
import sys
import time


def on_clicked():
    time.sleep(10)  # Засыпаем на 10 секунд


app = QtWidgets.QApplication(sys.argv)
button = QtWidgets.QPushButton("Start process")
button.resize(200, 40)
button.clicked.connect(on_clicked)
button.show()
sys.exit(app.exec_())
