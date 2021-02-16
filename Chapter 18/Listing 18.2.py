# Вывод окна приблизительно по центру экрана
"""
Задать местоположение окна позволяют следующие методы:

move(<X>, <Y>) - задает местоположение относительно родителя с учетом заголовка и границ.
В качестве параметра можно указать экземпляр класса QPoint из модуля QtCore.
Пример вывода в левом верхнем углу:
>>> window.move(0, 0)
>>> window.move(QtCOre.QPoint(0, 0))

setGeometry(<X>, <Y>, <Ширина>, <Высота>) - изменяет положение и размер одновременно.
Метод не учитывает высоту заголовка и границы.
В качестве параметра можно указать экземпляр класса QRect из модуля QtCore:
>>> window.setGeometry(100, 100, 100, 70)
>>> window.setGeometry(QtCore.QRect(100, 100, 100, 70))

Получить позицию окна позволяют следующие методы:

x() и y() - возвращают координаты верхнего левого угла. Методы учитывают заголовок и границы.
>>> window.move(10, 10)
>>> print(window.x(), window.y())  # 10 10

pos() - возвращает экземпляр класса QPoint, содержащий координаты верхнего левого угла, относительно родителя.
Метод учитывает высоту заголовка и границы.
>>> window.move(10, 10)
>>> print(window.pos().x(), window.pos().y())  # 10 10

geometry() - Возвращает экземпляр класса QRect, содержащий координаты относительно родительского компонента.
Метод не учитывает высоту заголовка и границы.
>>> window.resize(300, 100)
>>> window.move(10, 10)
>>> rect = window.geometry()
>>> print(rect.left(), rect.top())  # 14 40
>>> print(rect.width(), rect.height())  # 300 100

frameGeometry() - возвращает экземпляр класса QRect, содержащий координаты с учетом заголовка и границ. Полные размеры
доступны только после отображения окна.
>>> window.resize(300, 100)
>>> window.move(10, 10)
>>> rect = window.frameGeometry()
>>> print(rect.left(), rect.top())  # 10 10
>>> print(rect.width(), rect.height())  # 308 134

Для отображения окна по центру, у правой или нижней границы необходимо задать размеры экрана. Для получения размеров
экрана следует вызвать статический метод QApplication.desktop(), который возвращает ссылку на компонент рабочего стола,
представленный экземпляром класса QDesktopWidget из модуля QtWidgets.
Получить размеры позволяют следующие методы этого класса:

width() - ширина экрана в пикселях

height() - высота экрана в пикселях

Примеры:
>>> desktop = QtGui.QApplication.desktop()
>>> print(desktop.width(), desktop.height())  # 1440 900

screenGeometry() - возвращает экземпляр класса QRect, содкржащий координаты всего экрана:
>>> desktop = QtGui.QApplication.desktop()
>>> rect = desktop.screenGeometry()
>>> print(rect.left(), rect.top())  # 0 0
>>> print(rect.width(), rect.height())  # 1440 900

availableGeometry() - возвращает экземпляр класса QRect, содержащий координаты только доступной части экрана, без
размера панели задач:
>>> desktop = QtGui.QApplication.desktop()
>>> rect = desktop.availableGeometry()
>>> print(rect.left(), rect.top())  # 0 0
>>> print(rect.width(), rect.height())  # 1440 818
"""

from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()
window.setWindowTitle("Вывод окна по центру экрана")
window.resize(300, 100)
desktop = QtWidgets.QApplication.desktop()
x = (desktop.width() - window.width()) // 2
y = (desktop.height() - window.height()) // 2
window.move(x, y)
window.show()
sys.exit(app.exec_())
