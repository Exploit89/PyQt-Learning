# Вывод заставки

from PyQt5 import QtCore, QtGui, QtWidgets
import time


class MyWindow(QtWidgets.QPushButton):

    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText("Close window")
        self.clicked.connect(QtWidgets.qApp.quit)

    def load_data(self, sp):
        for i in range(1, 11):  # имитируем процесс
            time.sleep(2)  # что-то загружаем
            sp.showMessage("Data loading... {0}%".format(i * 10), QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom,
                           QtCore.Qt.black)
            QtWidgets.qApp.processEvents()  # запускаем оборот цикла


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    splash = QtWidgets.QSplashScreen(QtGui.QPixmap("../splashscreen.jpg"))
    splash.showMessage("Data loading... 0%", QtCore.Qt.AlignHCenter | QtCore.Qt.AlignBottom, QtCore.Qt.black)
    splash.show()  # отображаем заставку
    QtWidgets.qApp.processEvents()  # запускаем оборот цикла
    window = MyWindow()
    window.setWindowTitle("Using class QSplashScreen")
    window.resize(300, 30)
    window.load_data(splash)  # загружаем данные
    window.show()
    splash.finish(window)  # скрываем заставку
    sys.exit(app.exec_())
