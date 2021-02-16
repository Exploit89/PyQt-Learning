# ООП-стиль создания окна
"""Модуль QtCore, в котором объявлены атрибуты, задающие в том числе
режим выравнивания текста в объекте надписи"""
from PyQt5 import QtCore, QtWidgets


"""Определяем класс MyWindow, который наследует класс QWidget"""
class MyWindow(QtWidgets.QWidget):

    """Определяет конструктор класса. В качестве параметров принимает ссылки
    на экземпляр класса(self) и на родительский компонент(parent).
    Если родительского компонента нет - принимается значение по умолчанию(None).
    Внутри метода __Init__() вызывается конструктор базового класса
    и передается ссылка на родительский компонент QtWidgets.QWidget..."""
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self, parent)
        """Создаются объекты, контейнер, помещаются в окно
        Объекты надписи и кнопки сохраняются в атрибутах экземпляра класса.
        Из методов класса можно управлять объектами"""
        self.label = QtWidgets.QLabel("Hi, Man!")
        self.label.setAlignment(QtCore.Qt.AlignHCenter)
        self.btnQuit = QtWidgets.QPushButton("&Close window")
        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.label)
        self.vbox.addWidget(self.btnQuit)
        self.setLayout(self.vbox)
        """Выражение назначает обработчик сигнала"""
        self.btnQuit.clicked.connect(QtWidgets.qApp.quit)


"""Внутри условия создаются объекты приложения и экземпляра класса MyWindow.
Атрибут модуля __name__ будет содержать значение __main__ только в случе запуска модуля
как главной программы"""
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("ООП-стиль создания окна")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
