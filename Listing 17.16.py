#  Использование модуля queue
"""Queue - очередь (FIFO).

Формат конструктора:
<Объект> = Queue([maxsize=0])
Пример:
>>> import queue
>>> q = queue.Queue()
>>> q.put_nowait("elem1")
>>> q.put_nowait("elem2")
>>> q.get_nowait()
'elem'
>>> q.get_nowait()
'elem'

LifoQueue - стек (LIFO).

Формат конструктора:
<Объект> = LifoQueue([maxsize=0])
Пример:
>>> q = queue.LifoQueue()
>>> q.put_nowait("elem1")
>>> q.put_nowait("elem2")
>>> q.get_nowait()
'elem2'
>>> q.get_nowait()
'elem1'

PriorityQueue - очередь с приоритетами.Элементы очереди должны быть кортежами, в которых первый элемент - число,
означающее приоритет, а второе - значение элемента.

Формат конструктора класса:
<Объект> = PriorityQueue([maxsize=0])
Пример:
>>> q = queue.PriorityQueue()
>>> q.put_nowait((10, "elem1"))
>>> q.put_nowait((3, "elem2"))
>>> q.put_nowait((12, "elem3"))
>>> q.get_nowait()
(3, 'elem2')
>>> q.get_nowait()
(10, 'elem1')
>>> q.get_nowait()
(12, 'elem3')

Параметр maxsize задает максимальное кол-во элементов, которое может содержать очередь.
Если параметр равен нулю или отрицательный - значит размер очереди не ограничен.

Эти классы поддерживают следующие методы:

put(<Элемент>[, block=True][, timeout=None]) - добавляет элемент в очередь.
Если block=True, поток будет ожидать возможности добавления элемента, timeout - максимальное время ожидания в секундах.
Если элемент не удалось добавить - вызывается исключение queue.Full.
Если block=False - очередь не будет ждать возможности добавления элемента, следствие - исключение queue.Full сразу.

put_nowait(<Элемент>) - добавление элемента без ожидания, эквивалентно put(<Элемент>, False)

get([block=True][, timeout=None]) - возвращает элемент, при этом удаляя его из очереди.
Если block=True, поток будет ожидать возможности извлечения элемента, timeout - максимальное время ожидания в секундах.
Если элемент не удалось добавить - вызывается исключение queue.Empty.
Если block=False - очередь не будет ждать возможности извлечения элемента, следствие - исключение queue.Empty сразу.

get_nowait() - извлечение элемента без ожидания. Эквивалентно get(False)

join() - блокирует поток, пока не будут обработаны все задания в очереди.
Другие потоки должны вызвать метод task_done(). Когда все задания будут выполнены - поток будет разблокирован.

task_done() - этот метод должны вызывать потоки после обработки задания.

qsize() - возвращает примерное кол-во элементов в очереди. (доверять этому значению не следует)

empty() - возвращает True, если очередь пуста, и False - в противном случае.

full() -  возвращает True, если очередь содержит элементы, и False - в противном случае.
"""

from PyQt5 import QtCore, QtWidgets
import queue


class MyThread(QtCore.QThread):
    task_done = QtCore.pyqtSignal(int, int, name = 'taskDone')

    def __init__(self, id, queue, parent=None):
        QtCore.QThread.__init__(self, parent)
        self.id = id
        self.queue = queue

    def run(self):
        while True:
            task = self.queue.get() #  Получаем задание
            self.sleep(5) #  Имитируем обработку
            self.task_done.emit(task, self.id) #  Передаем данные обратно
            self.queue.task_done()


class MyWindow(QtWidgets.QPushButton):

    def __init__(self):
        QtWidgets.QPushButton.__init__(self)
        self.setText("Раздать задания")
        self.queue = queue.Queue() #  Создаем очередь
        self.threads = []
        for i in range(1, 3): #  Создаем потоки и запускаем
            thread = MyThread(i, self.queue)
            self.threads.append(thread)
            thread.task_done.connect(self.on_task_done, QtCore.Qt.QueuedConnection)
            thread.start()
        self.clicked.connect(self.on_add_task)

    def on_add_task(self):
        for i in range(0, 11):
            self.queue.put(i) #  Добавляем задания в очередь

    def on_task_done(self, data, id):
        print(data, "- id =", id) #  Выводим обработанные данные

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MyWindow()
    window.setWindowTitle("Использование модуля queue")
    window.resize(300, 30)
    window.show()
    sys.exit(app.exec_())
