# Использование контейнера QGridLayout
"""
Иерархия наследования:
(QObject, QLayoutItem) - QLayout - QGridLayout

Создание экземпляра класса:
<Объект> = QGridLayout([<Родитель>])

Добавить компоненты позволяют следующие методы:

addWidget() - добавляет компонент в указанную ячейку сетки.
Метод имеет следующие форматы:
addWidget(<Компонент>, <Строка>, <Столбец>[, alignment=0])
addWidget(<Компонент>, <Строка>, <Столбец>, <Кол-во строк>, <Кол-во столбцов>[, alignment=0])

Пример:
>>> grid = QtGui.QGridLayout()
>>> grid.addWidget(button1, 0, 0, alignment=QtCore.Qt.Alignleft)
>>> grid.addWidget(button2, 0, 1, QtCore.Qt.AlignRight)
>>> grid.addWidget(button3, 1, 0, 1, 2)

addLayout() - добавляет контейнер в указанную ячейку сетки.
Метод имеет следующие форматы:
addLayout(<Контейнер>, <Строка>, <Столбец>[, alignment=0])
addLayout(<Контейнер>, <Строка>, <Столбец>, <Кол-во строк>, <Кол-во столбцов>[, alignment=0])

Для удаления и замены компонентов следует пользоваться методами removeWidget() и replaceWidget()

Класс QGridLayout поддерживает следующием методы:

setRowMinimumHeight(<Индекс>, <Высота>) - задает минимальную высоту строки

setColumnMinimumWidth(<Индекс>, <Ширина>) - задает минимальную ширину столбца

setRowStretch(<Индекс>, <Фактор растяжения>) - задает фактор растяжения по вертикали для строки

setColumnStretch(<Индекс>, <Фактор растяжения>) - задает фактор растяжения по горизонтали для столбца

setContentsMargins(<Слева>, <Сверху>, <Справа>, <Снизу>) - задает отсутпы от границ сетки до компонентов
setContentsMargins(<QMargins>)

setSpacing(<Значение>) - задает расстояние между компонентами по горизонтали и вертикали
setVerticalSpacing()
setHorizontalSpacing()

rowCount() - возвращает кол-во строк сетки

columnCount() - возвращает кол-во столбцов сетки

cellRect(<Индекс строки>, <Индекс колонки>) - возвращает экземпляр класса QRect, который хранит координаты и размеры
ячейки, расположенной на пересечении строки и колонки с указанными индексами

"""
from PyQt5 import QtWidgets
import sys


app = QtWidgets.QApplication(sys.argv)
window = QtWidgets.QWidget()  # Родительский компонент - окно
window.setWindowTitle("QGridLayout")
window.resize(150, 100)
button1 = QtWidgets.QPushButton("1")
button2 = QtWidgets.QPushButton("2")
button3 = QtWidgets.QPushButton("3")
button4 = QtWidgets.QPushButton("4")
grid = QtWidgets.QGridLayout()  # Создаем сетку
grid.addWidget(button1, 0, 0)  # Добавляем компоненты
grid.addWidget(button2, 0, 1)
grid.addWidget(button3, 1, 0)
grid.addWidget(button4, 1, 1)
window.setLayout(grid)  # Передаем ссылку родителю
window.show()
sys.exit(app.exec_())
