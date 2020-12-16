# Повторное использование кода при ООП-стиле

from PyQt5 import QtCore, QtWidgets
import MyWindow


class MyDialog(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        """Внутри конструктора создаем экземпляр класса MyWindow
        и сохраняем в атрибуте myWidget"""
        self.myWidget = MyWindow.MyWindow()
        """Отступы между границами контейнера и границами соседних элементов"""
        self.myWidget.vbox.setContentsMargins(0, 0, 0, 0)
        self.button = QtWidgets.QPushButton("change label")
        mainBox = QtWidgets.QVBoxLayout()
        mainBox.addWidget(self.myWidget)
        mainBox.addWidget(self.button)
        self.setLayout(mainBox)
        self.button.clicked.connect(self.on_clicked)

    def on_clicked(self):
        self.myWidget.label.setText("new label")
        self.button.setDisabled(True)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyDialog()
    window.setWindowTitle("Преимущество ООП-стиля")
    window.resize(800, 600)
    window.show()
    sys.exit(app.exec_())
