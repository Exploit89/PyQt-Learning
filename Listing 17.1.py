# First app on PyQt

from PyQt5 import QtWidgets
import sys
"""Модуль QtWidgets, содержащий классы, реализующие компоненты графического интерфейса"""
"""Модуль sys, из которого получаем список параметров, переданных командной строке (argv),
а также функция exit(), завершающая выполнение программы"""

"""Выражение создает экземпляр класса QApplication.
Конструктор этого класса принимает параметры, переданные в командной строке.
В программе должен быть объект приложения и только один!
Получить доступ к объекту можно через атрибут qApp из модуля QtWidgets.
Вывести список параметров:
print(QtWidgets.qApp.argv())"""
app = QtWidgets.QApplication(sys.argv)
"""Создает объект окна в виде экземпляра класса QWidget.
Наследует почти все классы, реализующие окмпоненты графического интерфейса.
Любой компонент, не имеющий родителя, обладает собственным окном"""
window = QtWidgets.QWidget()
"""Задает заголовок окна методом setWindowTitle()"""
window.setWindowTitle("First app on PyQt")
"""Задает минимальные размеры окна(ширина, высота), без учета заголовка и рамки.
Если компоненты не влезут - окно увеличится"""
window.resize(800, 600)
"""Создает объект надписи. Текст в качестве параметра в конструкторе класса QLabel.
Внутри HTML-теги - для центрирования надписи"""
label = QtWidgets.QLabel("<center>Hi, man!</center>")
"""Создает объект кнопки. Текст в качестве параметра QPushButton.
Амперсанд задает клавишу быстрого доступа"""
btnQuit = QtWidgets.QPushButton("&Close window")
"""Создает вертикальный контейнер. Все компоненты в контейнере будут
помещаться вертикально сверху вниз. Размеры будут подогнанны под размер контейнера.
При изменении размера контейнера - изменятся все компоненты."""
vbox = QtWidgets.QVBoxLayout()
"""Метод addWidget() добавляет ранее созданные объекты надписи и кнопки.
При добавлении объектов - они автоматом становятся потомками контейнера"""
vbox.addWidget(label)
vbox.addWidget(btnQuit)
"""Добавляет контейнер в основное окно с помощью метода setLayout()
Контейнер становится потомком основного окна"""
window.setLayout(vbox)
"""Назначает обработчик сигнала clicked() кнопки.
Поддерживает метод connect(), передаваемый первым параметром.
Обработчик представляет метод quit() объекта приложения,
закрывающий приложенмие. Этот метод называют слотом"""
btnQuit.clicked.connect(app.quit)
"""Выводит окно"""
window.show()
"""Запускает бесконечный цикл обработки событий в приложении"""
sys.exit(app.exec_())
