# Глава 18.2 Указание типа окна
"""
QWidget - окно по умолчанию. (свернуть, закрыть, заголовок, меню и т.д.)

setWindowFlags() - метод для указания другого типа окна.
или
flags - как параметр в конструкторе класса QWidget.

Формат метода:
setWindowFlags(<Тип окна>)
В параметре <Тип окна> можно указать следующие атрибуты класса QtCore.Qt:
Widget - тип по умолчанию для класса QWidget.

Window - указывает, что компонент является окном, вне зависимости от того, имеет он родителя или нет.
По умолчанию размеры окна можно изменить мышкой.

Dialog - диалоговое окно. Есть кнопки Справка и Закрыть. Это значение по умолчанию для класса QDialog.
По умолчанию размеры окна можно изменить мышкой.
Пример:
window.setWindowFlags(QtCore.Qt.Dialog)

Sheet и Drawer - окна в стиле apple.

Popup - вплывающее меню.

Tool - панель инструментов.
По умолчанию размеры окна можно изменить мышкой.

ToolTip - всплывающая подсказка.

SplashScreen - заставка. Это значение по умолчанию для класса QSplashScreen.

Desktop - рабочий стол. Не отображается на экране.

SubWindow - дочерний компонент, вне зависимости от наличия родителя. Без кнопок.

ForeignWindow - окно, созданное другим процессом.

CoverWindow - минимизированное приложение на некоторых мобильных платформах.

Получить тип окна в программе позволяет метод windowType().

Для окон верхнего уровня можно через оператор | дополнительно указать следующие атрибуты класса QtCOre.Qt (некторые):
MSWindowsFixedSizeDialogHint - запрещает изменение размеров окна. Кнопка "развернуть" становится неактивна.



"""