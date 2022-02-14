"""
    Реализация декоратора* логирования*
"""

import functools

from loguru import logger


logger.add('logs.txt')


def logging(*, entry=True, exit=True, level="DEBUG"):
    """
        Реализация собственного декоратора для логирования
    :param entry: логировать входные данные
    :param exit: логировать выходные данные
    :param level: уровень логирования входа и выхода
    :return:
    """

    def wrapper(func):
        name = func.__name__

        @functools.wraps(func)
        def wrapped(*args, **kwargs):
            logger_ = logger.opt(depth=1)
            if entry:
                logger_.log(level, "Entering '{}' (args={}, kwargs={})", name, args, kwargs)

            result = func(*args, **kwargs)
            if exit:
                logger_.log(level, "Exiting '{}' (result={})", name, result)
            return result

        return wrapped

    return wrapper


@logging()
def print_hello_world():
    """
        Демонстрация логирования без параметров
    """
    print('Hello World')


@logging()
def print_hello_world_with_args(a: int, b: str, c: list = None) -> tuple:
    """
        Демонстрация логирования с параметрами
    :param a:
    :param b:
    :param c:
    :return:
    """

    if isinstance(a, int):
        print(f'{a}')
    else:
        logger.error('{a} not int')

    if isinstance(b, str):
        print('{}'.format(b))
    else:
        logger.error('{b} not str')

    print(f'{c=}')

    logger.success('Green output =)')

    return a, b, c
