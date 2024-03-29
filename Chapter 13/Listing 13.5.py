# Метод __init--()
"""
При создании экземпляра класса интерпретатор автоматически вызывает метод инициализации __init__().
Такой метод принято называть конструктором класса.
Формат метода:
def __init__(self[, <Значение1>[, ..., <Значение N>]]):
    <Инструкции>

С помощью этого метода атрибутам класса можно присвоить начальные значения.
При создании экземпляра класса параметры этого метода указываются после имени класа в круглых скобках:
<Экземпляр класса> = <Имя класса>([<Значение1>[, ..., <Значение N>]])
"""


class MyClass:
    def __init__(self, value1, value2):  # Конструктор
        self.x = value1
        self.y = value2

c = MyClass(100, 300)  # Создаем экзкмпляр класса
print(c.x, c.y)  # Выведет: 100 300