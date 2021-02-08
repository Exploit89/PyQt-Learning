#  Использование класса QMutex
"""
Конструктор класса QMutex создает мьютекс и имеет следующий формат:
<Объект> = QMutex([mode=QtCore.QMutex.NonRecursive])
mode может принимать следующие значения:
NonRecursive - поток может запросить блокировку единожды, затем только после разблокировки  - снова.
Recursive - поток может запросить блокировку несколько раз и, чтобы полностью снять блокировку, необходимо вызвать
метод unlock() соответствующее кол-во раз.

Класс Mutex поддерживает следующие методы:
lock() - устанавливает блокировку. Если ресурс заблокирован другим потоком, работа текущего приостанавливается до
снятия блокировки.
tryLock([timeout=0]) - устанавливает блокировку. Если блокировка была успешно установлена - возвращает True, если нет -
False без ожидания возможности установить блокировку.
Максимальное время ожидания (мс) можно установить с помощью необязательного параметра timeout. Если в параметре
отрицательное значение, то метод ведет себя как lock().
unlock() - снимает блокировку
isRecursive() - возвращает True, если конструктору было передано Recursive.
"""

from PyQt5 import QtCore, QtWidgets


class MyThread(QtCore.QThread):
    x = 10  # атрибут класса
    mutex = QtCore.QMutex()  # Мьютекс

    def __init__(self, id, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.id = id

    def run(self):
        self.change_x()

    def change_x(self):
        MyThread.mutex.lock()  # блокируем
        print("x =", MyThread.x, "id =", self.id)
        MyThread.x += 5
        self.sleep(2)
        print("x= ", MyThread.x, "id =", self.id)
        MyThread.x += 34
        print("x= ", MyThread.x, "id =", self.id)
        MyThread.mutex.unlock()  # снимаем блокировку


class MyWindow(QtWidgets.QPushButton):

    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText("Start")
        self.thread1 = MyThread(1)
        self.thread2 = MyThread(2)
        self.clicked.connect(self.on_start)

    def on_start(self):
        if not self.thread1.isRunning():
            self.thread1.start()
        if not self.thread2.isRunning():
            self.thread2.start()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Using class Mutex")
    window.resize(300, 30)
    window.show()
    sys.exit(app.exec_())
