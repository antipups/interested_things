import os


def create_virtualenv():
    """
        Создание виртуальной среды для запуска всего кода
    """
    try:
        # импортим необходимые либы для проверки настройки окружающей среды
        import loguru

    except ModuleNotFoundError:

        separator = '\n' + '=' * 100 + '\n'
        print(separator + '\nVenv not setup, creating venv...\n' + separator)
        os.system('python -m venv venv')

        activate_this = 'venv/Scripts/activate_this.py'
        with open(activate_this) as f:
            code = compile(f.read(), activate_this, 'exec')
            exec(code, dict(__file__=activate_this))

        print(separator + '\nInstall requirements...\n' + separator)
        os.system('pip install -r requirements.txt')

        from loguru import logger
        print('\n\n')
        logger.success('Установка и настройка venv успешно завершена.')
