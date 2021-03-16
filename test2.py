# UPD advice from S. Nick
from PyQt5.QtCore import Qt, QTimer
from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QProgressBar, \
    QVBoxLayout, QApplication


class DescriptionView(QWidget):  # - QtWidgets.QVBoxLayout):
    def __init__(self):
        super().__init__()
        self.value = 0
        self.minValue = 0
        self.maxValue = 100

        self.power_data = QLabel(
            f"Power: {self.value} / {self.maxValue}",
            alignment=Qt.AlignLeft | Qt.AlignTop
        )

        self.progressBar = QProgressBar()
        self.progressBar.setProperty("value", 0)
        self.progressBar.setFixedHeight(7)
        self.progressBar.setTextVisible(False)
        self.progressBar.setRange(self.minValue, self.maxValue)

        layout = QVBoxLayout(self)
        layout.addWidget(self.power_data)
        layout.addWidget(self.progressBar)
        layout.addStretch()


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.my_tree_view = DescriptionView()
        main_layout = QHBoxLayout(self)
        main_layout.addWidget(self.my_tree_view)

        self.timer = QTimer()
        self.timer.setInterval(100)
        self.timer.timeout.connect(self.update_time)
        self.timer.start()

    def update_time(self):
        if self.my_tree_view.value > self.my_tree_view.maxValue:
            self.timer.stop()
        elif self.my_tree_view.value > 15:
            self.my_tree_view.progressBar.setValue(self.my_tree_view.value)
            text = f"Power: {self.my_tree_view.value} / {self.my_tree_view.maxValue}"
            self.my_tree_view.power_data.setText(text)
        self.my_tree_view.value += 1


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    mw = MainWindow()
    mw.show()
    sys.exit(app.exec_())