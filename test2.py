from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import *


class DescriptionView(QtWidgets.QVBoxLayout):

    def __init__(self, parent=None):
        QtWidgets.QVBoxLayout.__init__(self, parent)

        self.data1 = int(0)
        self.data2 = int(100)

        self.power = QtWidgets.QHBoxLayout()
        self.powerlabel = QLabel("Power: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.power_data = QLabel(str(self.data1) + "/" + str(self.data2), alignment=Qt.AlignLeft | Qt.AlignTop)

        self.powervalue = QtWidgets.QProgressBar(self.powerlabel)
        self.powervalue.setFixedSize(280, 5)
        self.powervalue.setTextVisible(False)
        self.powervalue.setMaximum(self.data2)
        self.powervalue.setValue(self.data1)


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_tree_view = DescriptionView()

        main_layout = QHBoxLayout()
        main_layout.addLayout(self.my_tree_view)
        self.my_tree_view.addWidget(self.my_tree_view.powerlabel)
        self.my_tree_view.addWidget(self.my_tree_view.power_data)
        self.my_tree_view.addWidget(self.my_tree_view.powervalue)

        self.setLayout(main_layout)

        a = 10

        if a > 5:
            self.my_tree_view.data2 = 50
            print(self.my_tree_view.data2)
        else:
            pass


if __name__ == '__main__':
    app = QApplication([])

    mw = MainWindow()
    mw.show()

    app.exec()