#advice from S.nick

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QProgressBar, \
    QVBoxLayout, QApplication


class DescriptionView(QWidget):                # - QtWidgets.QVBoxLayout):
    def __init__(self):
        super().__init__()

        self.data1 = 0
        self.data2 = 100

# ?        self.power = QHBoxLayout()
        self.powerlabel = QLabel("Power: ", alignment=Qt.AlignLeft | Qt.AlignTop)
        self.power_data = QLabel(str(self.data1) + "/" + str(self.data2), alignment=Qt.AlignLeft | Qt.AlignTop)

        self.powervalue = QProgressBar(self.powerlabel)
        self.powervalue.setFixedSize(280, 5)
        self.powervalue.setTextVisible(False)
        self.powervalue.setMaximum(self.data2)
        self.powervalue.setValue(self.data1)
# +++
        layout = QVBoxLayout(self)
        layout.addWidget(self.powerlabel)
        layout.addWidget(self.power_data)
        layout.addWidget(self.powervalue)
# +++


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_tree_view = DescriptionView()

        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.my_tree_view)
#        self.my_tree_view.addWidget(self.my_tree_view.powerlabel)
#        self.my_tree_view.addWidget(self.my_tree_view.power_data)
#        self.my_tree_view.addWidget(self.my_tree_view.powervalue)
#        self.setLayout(main_layout)

        a = 10
        if a > 5:
            self.my_tree_view.data2 = 50
            print(self.my_tree_view.data2)
            self.my_tree_view.powervalue.setValue(self.my_tree_view.data2)           # +++ !!!
        else:
            pass


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())

