"""
    Демонстрация работы с переменными (принципы python, ключ. слова, операторы)
        и не только
"""
from my_package.logging import logger


class VariablesDemonstration:
    def __init__(self):
        """
            Конструктор, функция срабатывающая при создании проекта;
            self - обращение к объекту из его методов
        """
        self.start_demonstrations()

    def start_demonstrations(self):
        """
            Список всех предоставляющих методов
        :return:
        """

        self.tuple_logic()
        self.type_converting()
        self.slicing()
        self.mutable_and_not_mutable_vars()
        self.magic_operators()
        self.references()
        self.operators()
        VariablesDemonstration.static_method()  # не self, так как метод - статичный

    def method_will_be_create(self):
        """
            coming soon...
        """
        pass    # pass для уведомления программиста о реализации функционала функции в будущем

    def type_converting(self):
        """
            Представление привидения типо
        """

        tuple([1, 2, 3])
        tuple(x for x in range(1, 10))
        tuple('Hi')

        a = tuple(str(x) for x in range(1, 10))
        str(a)       # в старых версиях не работает
        ''.join(a)   # работает во всех версиях

    def slicing(self):
        """
            Демонстрация работы со срезами
        """

        a = 'Hi world!'
        a[:2]    # output Hi
        a[:3]    # output world!
        a[::-1]  # output !dlrow iH
        a[::2]   # output H ol!
        tuple(range(1, 11))[1:-1:2]  # (2, 4, 6, 8)
        try:
            (x for x in [1, 2, 3])[1:2]
        except TypeError:
            logger.error('Генератор НЕ ОБРЕЗАЕТСЯ')

    def mutable_and_not_mutable_vars(self):
        """
            Демонстрация изменяемых и неизменяемых типов в Python
        """

        try:
            a = 'string'
            new_string_part = 'abc'
            a[1] = new_string_part

        except TypeError:
            logger.error('Строка неизменяема.')
            a = a[:1] + new_string_part + a[1:]     # правильное изменение строки
            a   # sabctring

        list_ = [1, 2, 3]   # нейминг переменных которые имеют
        # тот же корень что и ключ слова помечается нижним подчеркиванием в конце

        list_[1] = 3

        tuple_ = (1, 2, 3)

        try:
            tuple_[1] = 3
        except TypeError:
            logger.error('Кортежи неизменяемы.')

    def tuple_logic(self):
        """
            Представление кортежной логики в пайтоне
        """

        a, b = 1, 2     # 1, 2

        def test_func():
            return 1, 2, 3

        a, b, c = test_func()   # 1, 2, 3

    def magic_operators(self):
        a, b, c, *args = range(1, 10)      # распаковка остальной части генератора через *
        args    # [4, 5, 6, 7, 8, 9]

        def test_func(*args, **kwargs):    # область видимости функции внутри функции, извне она не доступна
            return args, kwargs

        test_func(1, 2, 3,
                  first_var=1,
                  second_var=2)            # для более читаемого кода функции с множеством аргументов пишутся лесенкой
        # output args = [1, 2, 3], kwargs = {'first_var': 1, 'second_var': 2}

        test_func(**{'first_var': 1, 'second_var': 2})     # распаковка словаря через **

    def references(self):
        """
            Представление работы ссылок (!)
        """

        a = [1, 2, 3]
        b = a
        a.append(1)
        a   # [1, 2, 3, 1]
        b   # [1, 2, 3, 1] так как b и а это ссылки на один и тот же список

        a = (1, 2, 3)
        b = a
        a = (1, 2, 3, 4)
        a   # (1, 2, 3, 4)
        b   # (1, 2, 3) так как ссылки на кортежи не работают,
        # а работают ТОЛЬКО на изменяемые объекты (list, dict, object)

    def operators(self):
        True and 5 and 'dfg'     # dfg, так как это последний истинный аргумент
        'abc' or 'dfg'           # abc так как abc истиный аргумент и дальше не стоит идти
        55 and [] and 5          # [] / None так как он отрицательный аргумент (может быть False, [], None и т. д.)
        None is None             # оператор is проверят изначально по типу И адресу* (после привидения)
        [1, 2, 3] is [1, 2, 3]   # False

    @staticmethod
    def static_method():
        """
            Статический метод (или метод, который можно вызывать без создания объекта)
        :return:
        """
        print('I\'m static')

    def __del__(self):
        """
            Деструктор класса, вызывается при удалении класса
        """

    def __enter__(self):    # вызывается при создании объекта через with as
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """
            Вызывается при выходе класса, будь то через ошибку или нет
        :param exc_type:
        :param exc_val:
        :param exc_tb:
        :return:
        """
