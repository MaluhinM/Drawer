try:  # Защита от 102-го
    print('Запуск программы...')  # Вывод информации в консоль
    print('Импорт библиотек: ', end='')  # Вывод информации в консоль
    # Импорт библиотек
    import turtle  # Рисование
    from keyboard import add_hotkey, block_key  # Управление
    from tkinter.messagebox import showerror  # Создание окон ошибок
    from os import path  # Проверка наличия путей
    from sys import exit  # Завершение работы программы
    from glob import glob  # Просмотр файлов
    from random import choices

    print('Выполнено')  # Вывод информации в консоль

    print('Расчет значений: ', end='')  # Вывод информации в консоль

    # Ошибки и их возможные причины
    causes: 'Ошибки' = {'Несуществующий путь': 'Отсутствует необходимый для работы программы файл',
                        'Несуществующие пути': 'Отсутствуют необходимые для работы программы файлы',
                        'Неверное значение': 'Программа получила недопустимое значение на вход из определенного файла',
                        'Непредвиденная ошибка': 'В работе программы произошел сбой'}
    causes_keys: 'Оглавления ошибок' = tuple(causes.keys())  # Названия ошибок

    data_folder: 'data' = 'data'  # Основная папка <data>. В ней содержится большинство данных
    hotkeys_folder: 'data/hotkeys' = f'{data_folder}\hotkeys'  # Папка <hotkeys>. Хранит клавиши или сочетание клавиш для управления
    values_folder: 'data/values' = fr'{data_folder}\values'  # Папка <values>. Хранит значения для управления
    figures_folder: 'data/figures' = fr'{data_folder}\figures'  # Папка <figures>. Хранит названия фигур и значения для их использования

    hotkeys_figures: 'data/hotkeys/figures' = fr'{hotkeys_folder}\figures'  # Папка <hotkeys\figures>. Хранит клавиши или сочетание клавиш для вызова той или иной фигуры
    values_figures: 'data/values/figures' = fr'{values_folder}\figures'  # Папка <values\figures>. Хранит значения, используемые фигурами

    base_hotkeys: 'data/hotkeys/base' = fr'{hotkeys_folder}\base'  # Папка <hotkeys\base>. Хранит клавиши или сочетание клавиш для обычного перемещения
    shift_hotkeys: 'data/hotkeys/shift' = f'{hotkeys_folder}\shift'  # Папка <hotkeys\shift>. Хранит клавиши или сочетание клавиш для перемещения с клавишей Shift
    ctrl_hotkeys: 'data/hotkeys/ctrl' = f'{hotkeys_folder}\ctrl'  # Папка <hotkeys\ctrl>. Хранит клавиши или сочетание клавиш для перемещения с клавишей Ctrl
    other_hotkeys: 'data/hotkeys/other' = f'{hotkeys_folder}\other'  # Папка <hotkeys\other>. Хранит клавиши или сочетание клавиш для прочих функций программы
    hotkeys: tuple = (base_hotkeys, shift_hotkeys, ctrl_hotkeys, other_hotkeys)  # Переменная для хранения папок <hotkeys\*>

    base_values: 'data/values/base' = fr'{values_folder}\base'  # Папка <values\base>. Хранит значения для обычного перемещения
    shift_values: 'data/values/shift' = f'{values_folder}\shift'  # Папка <values\shift>. Хранит значения для перемещения с клавишей Shift
    ctrl_values: 'data/values/ctrl' = f'{values_folder}\ctrl'  # Папка <values\ctrl>. Хранит значения для перемещения с клавишей Ctrl
    other_values: 'data/values/other' = f'{values_folder}\other'  # Папка <hotkeys\other>. Хранит значения, отвечающие за вкл.\выкл. прочих функций программы
    vls: tuple = (base_values, shift_values, ctrl_values)  # Переменная для хранения папок <values\*>

    base_keys: tuple = ('forward', 'backward', 'left', 'right')  # Функции обычного перемещения
    shift_keys: tuple = ('shift_forward', 'shift_backward', 'shift_left', 'shift_right')  # Функции для перемещения с клавишей Shift
    ctrl_keys: tuple = ('ctrl_forward', 'ctrl_backward', 'ctrl_left', 'ctrl_right')  # Функции для перемещения с клавишей Ctrl
    other_keys: tuple = ('exit', 'reset_pencolor', 'reset_bgcolor', 'reset_heading', 'reset_position', 'clear', 'reset', 'pen', 'undo', 'size+', 'size-', 'pencolor', 'bgcolor', 'fill')  # Прочие функции программы
    keys: tuple = (base_keys, shift_keys, ctrl_keys, other_keys)  # Переменная для хранения функций

    screen = turtle.getscreen()

    print('Выполнено')  # Вывод информации в консоль


    def IntegrityCheck() -> 'Проверка целостности программы':  # Проверка целостности программы
        """
        Проверка целостности программы
        """
        print('\nПроверка целостности программы...')  # Вывод информации в консоль

        print(f'Проверка папки <{data_folder}>: ', end='')  # Вывод информации в консоль
        if not path.exists(data_folder): RaiseError(causes_keys[0], f'Отсутствует папка <{data_folder}>')  # Проверка наличия папки. В случае ее отсутствия - вызывается ошибка
        print('Выполнено')  # Вывод информации в консоль

        print('Проверка файла <figures.py>: ', end='')  # Вывод информации в консоль
        if not path.exists('figures.py'):
            print('Файл <figures.py> не найден. Создание нового: ', end='')  # Вывод информации в консоль
            open('figures.py', 'w', encoding='utf-8').write('from turtle import *\n\n')  # Проверка наличия файла. В случае его отсутствия - записывается
        print('Выполнено')  # Вывод информации в консоль

        print(f'Проверка папки <{hotkeys_folder}>: ', end='')  # Вывод информации в консоль
        exist: list = [0] * len(hotkeys)  # Создание списка для отметки наличия путей
        for i in range(len(hotkeys)):  # Цикл проверки наличия путей
            if path.exists(hotkeys[i]): exist[i]: list = 1  # Наличие пути отмечается в списке
        if 0 in exist:  # Если есть отсутствующие пути
            errors: list = []  # Объявление списка с ошибками
            for i in range(len(hotkeys)):  # Цикл проверки
                if exist[i] == 0: errors.append('\n' + hotkeys[i])  # Если отсутствует, то записывает отсутствующий путь в список
            if len(errors) == 1:  # Если отсутствует всего один путь
                title: 'Оглавление ошибки' = causes_keys[0]  # Оглавление ошибки в единственном числе
                amount: str = 'Отсутствует путь: '  # Информация об ошибке в единственном числе
            else:  # Если количество отсутствующих больше одного
                title: 'Оглавление ошибки' = causes_keys[1]  # Оглавление ошибки во множественном числе
                amount: str = 'Отсутствуют пути:\n'  # Информация об ошибке во множественном числе
            RaiseError(title, amount + ', '.join(errors))  # Вызов соответствующей ошибки

        n: int = 0  # Счетчик количества путей
        for i in range(len(keys)):  # Цикл для счетчика
            for g in range(len(keys[i])): n += 1  # Счет количества путей
        exist: list = [0] * n  # Создание списка для записи несуществующих путей

        n: int = 0  # Счетчик
        for i in range(len(keys)):  # Цикл проверки
            for g in range(len(keys[i])):  # Проверка функций
                if path.exists(f'{hotkeys[i]}\\{keys[i][g]}.txt'): exist[n]: list = 1  # Если путь существует, то его присутствие отмечается в списке
                n += 1  # К счетчику прибавляется 1
        if 0 in exist:  # Если есть отсутствующие пути
            errors: list = []  # Объявление списка с ошибками
            n: int = 0  # Счетчик
            for i in range(len(keys)):  # Цикл проверки
                for g in range(len(keys[i])):  # Проверка функций
                    if exist[n] == 0: errors.append(f'\n{hotkeys[i]}\\{keys[i][g]}.txt')  # Если отсутствует, то записывает отсутствующий путь в список
                    n += 1  # К счетчику прибавляется 1
            if len(errors) == 1:  # Если ошибка всего одна
                title: 'Оглавление ошибки' = causes_keys[0]  # Имя ошибки в ед. числе
                amount: str = 'Отсутствует путь: '  # Текст ошибки в ед. числе
            else:  # Если количество ошибок больше одного
                title: 'Оглавление ошибки' = causes_keys[1]  # Имя ошибки во мн. числе
                amount: str = 'Отсутствуют пути:\n'  # Текст ошибки во мн. числе
            RaiseError(title, amount + ', '.join(errors))  # Вызов ошибки
        print('Выполнено')  # Вывод информации в консоль

        print(f'Проверка папки <{values_folder}>: ', end='')  # Вывод информации в консоль
        exist: list = [0] * len(vls)  # Создание списка для хранения информации о путях
        for i in range(len(vls)):  # Цикл проверки
            if path.exists(vls[i]): exist[i]: list = 1  # Если путь существует, то его присутствие отмечается в списке
        if 0 in exist:  # Если есть отсутствующие пути
            errors: list = []  # Объявление списка с ошибками
            for i in range(len(vls)):  # Цикл проверки
                if exist[i] == 0: errors.append('\n' + vls[i])  # Если отсутствует, то записывает отсутствующий путь в список
            if len(errors) == 1:  # Если ошибка всего одна
                title: 'Оглавление ошибки' = causes_keys[0]  # Имя ошибки в ед. числе
                amount: str = 'Отсутствует путь: '  # Текст ошибки в ед. числе
            else:  # Если количество ошибок больше одного
                title: 'Оглавление ошибки' = causes_keys[1]  # Имя ошибки во мн. числе
                amount: str = 'Отсутствуют пути:\n'  # Текст ошибки во мн. числе
            RaiseError(title, amount + ', '.join(errors))  # Вызов ошибки
        print('Выполнено')  # Вывод информации в консоль


    def FindPossibleCause(error: 'Имя ошибки', NeedReinstall: bool) -> 'Возможная причина':  # Нахождение возможной причины ошибки (принимает имя ошибки)
        if NeedReinstall: txt = '\nЕсли Вы не трогали файлы, содержащиеся в директории программы, то единственным выходом будет переустановка программы.\nВ противном случае, попробуйте откатить совершенные изменения. Если ошибка все равно остается - также переустановите программу'  # Если ошибка присутствует в списке, то вернуть причину
        else: txt = ''
        if error in causes: return causes[error] + txt
        return 'Не удалось определить причину'  # Если ошибки нет в списке, то вернуть отрицательный результат поиска
    def RaiseError(title: 'Оглавление ошибки', txt: 'Текст ошибки', NeedReinstall: bool = True) -> None:  # Вызов ошибки (принимает имя и текст ошибки)
        print('Программа столкнулась с ошибкой\n\nОшибка:', title)  # Вывод информации в консоль
        print('Возможная причина:', FindPossibleCause(title, NeedReinstall))  # Вывод информации в консоль
        win = showerror(title, f'{txt}\n\nПереустановите программу') if NeedReinstall else showerror(title, txt)  # Создание окна с ошибкой с соответствующим оглавлением и содержанием
        add_hotkey('Esc', lambda: win.destroy())  # Назначение клавиши Esc на закрытие окна с ошибкой (завершение работы программы)
        exit()  # Завершение работы программы


    def add_hk(x: 'Имя функции', key: 'Клавиша вызова функции', value: 'Что будет делать функция') -> 'Добавление функции': add_hotkey(key, lambda: eval(f'{x}({value})'))  # Добавление горячей клавиши для управления


    def GoBack():
        if turtle.isdown(): down = True
        else: down = False
        turtle.penup()
        turtle.goto(0, 0)
        if down: turtle.pendown()
    def Reset():
        old_pensize = turtle.pensize()
        old_color = turtle.pencolor()
        old_speed = turtle.speed()
        turtle.reset()
        turtle.color(old_color)
        turtle.pensize(old_pensize)
        turtle.speed(old_speed)
    fill_value = False
    def Fill():
        global fill_value
        if fill_value:
            fill_value = False
            turtle.end_fill()
        else:
            fill_value = True
            turtle.begin_fill()


    def start() -> None:  # Основная программа
        """
        Запуск основной программы
        """
        print('\nЗагрузка и распределение значений...')  # Вывод информации в консоль
        title_path: 'data/title.txt' = fr'{data_folder}\title.txt'  # Объявление пути до файла имени окна
        if path.exists(title_path): title_name: 'Имя окна' = open(title_path, 'r', encoding='utf-8').read().strip()  # Проверка присутствия пути и запись имени окна в переменную
        if not path.exists(title_path) or title_name in {''}:  # Если путь отсутствует или оно пустое
            print(f'Файл <{title_path}> не найден или его значение не соответствует ожидаемому. Создание нового: ', end='')  # Вывод информации в консоль
            title_name: 'Имя окна' = 'Drawer'  # Запись стандартного имени окна в переменную
            open(title_path, 'w', encoding='utf-8').write(title_name)  # Запись информации в файл
            print('Выполнено')  # Вывод информации в консоль
        turtle.title(title_name)  # Применение имени окна
        print('Имя окна:', title_name)  # Вывод информации в консоль

        speed_path: 'data/speed.txt' = fr'{data_folder}\speed.txt'  # Объявление пути до файла скорости
        if path.exists(speed_path): speed: 'Скорость' = open(speed_path, 'r', encoding='utf-8').read()  # Проверка присутствия пути и запись скорости в переменную
        if not path.exists(speed_path) or not speed.isdigit():  # Если путь отсутствует или значение скорости не число
            print(f'Файл <{speed_path}> не найден или его значение не соответствует ожидаемому. Создание нового: ', end='')  # Вывод информации в консоль
            speed: 'Скорость' = '6'  # Запись стандартной скорости в переменную
            open(speed_path, 'w', encoding='utf-8').write(speed)  # Запись информации в файл
            print('Выполнено')  # Вывод информации в консоль
        turtle.speed(int(speed))  # Применение скорости
        print('Установлена скорость:', speed)  # Вывод информации в консоль

        print('Распределение значений движения: ', end='')  # Вывод информации в консоль
        v: dict = {}  # Объявление словаря для хранения значений функций
        for i in vls:  # Цикл записи информации в словарь
            v[i.replace(f'{values_folder}\\', '')]: dict = {}  # Создание отдельных словарей внутри словаря
            for file in glob(f'{i}\*'): v[i.replace(f'{values_folder}\\', '')][file.replace(f'{i}\\', '').replace('.txt', '')]: int = int(open(file, 'r', encoding='utf-8').read())  # Запись значений функций в словари
        base: dict = v['base']  # Применение значений для функций стандартного передвижения
        shift: dict = v['shift']  # Применение значений для функций передвижения с клавишей Shift
        ctrl: dict = v['ctrl']  # Применение значений для функций передвижения с клавишей Ctrl
        print('Выполнено')  # Вывод информации в консоль

        print('Распределение клавиш: ', end='')  # Вывод информации в консоль
        hk: dict = {}  # Объявление словаря для хранения горячих клавиш
        for i in range(len(hotkeys)):  # Цикл записи клавиш в словарь
            if list(hotkeys)[i].replace(f'{hotkeys_folder}\\', '') == 'other':  # Если разделом клавиш является 'Прочее'
                for g in keys[i]:  # Цикл проверки состояния функций
                    hk[g]: 'Клавиши' = open(f'{hotkeys[i]}\\{g}.txt', 'r', encoding='utf-8').read()  # Запись клавиши для вызова функции
                    if not path.exists(f'{other_values}\\{g}.txt') or not open(f'{other_values}\\{g}.txt', 'r', encoding='utf-8').read() == '1':  # Если путь отсутствует или значением файла не является '1'
                        block_key(open(f'{hotkeys[i]}\\{g}.txt', 'r', encoding='utf-8').read())  # Блокировка клавиши
                        print(f'Функция <{g}> отключена; ', end='')  # Вывод информации в консоль
                continue  # Продолжить
            for g in keys[i]: hk[g]: 'Клавиши' = open(f'{hotkeys[i]}\\{g}.txt', 'r', encoding='utf-8').read()  # Запись клавиш для вызова функций
        print('Выполнено')  # Вывод информации в консоль

        print(f'Настройка функций: ', end='')  # Вывод информации в консоль
        # Применение параметров функций
        add_hotkey(hk['forward'], lambda: turtle.forward(base['forward']))  # Стандартное движение вперед
        add_hotkey(hk['backward'], lambda: turtle.backward(base['backward']))  # Стандартное движение назад
        add_hotkey(hk['left'], lambda: turtle.left(base['left']))  # Стандартный поворот влево
        add_hotkey(hk['right'], lambda: turtle.right(base['right']))  # Стандартный поворот вправо
        add_hotkey(hk['shift_forward'], lambda: turtle.forward(shift['shift_forward']))  # Движение вперед с клавишей Shift
        add_hotkey(hk['shift_backward'], lambda: turtle.backward(shift['shift_backward']))  # Движение назад с клавишей Shift
        add_hotkey(hk['shift_left'], lambda: turtle.left(shift['shift_left']))  # Поворот влево с клавишей Shift
        add_hotkey(hk['shift_right'], lambda: turtle.right(shift['shift_right']))  # Поворот вправо с клавишей Shift
        add_hotkey(hk['ctrl_forward'], lambda: turtle.forward(ctrl['ctrl_forward']))  # Движение вперед с клавишей Ctrl
        add_hotkey(hk['ctrl_backward'], lambda: turtle.backward(ctrl['ctrl_backward']))  # Движение назад с клавишей Ctrl
        add_hotkey(hk['ctrl_left'], lambda: turtle.left(ctrl['ctrl_left']))  # Поворот влево с клавишей Ctrl
        add_hotkey(hk['ctrl_right'], lambda: turtle.right(ctrl['ctrl_right']))  # Поворот вправо с клавишей Ctrl

        add_hotkey(hk['exit'], lambda: turtle.bye())  # Завершение работы программы
        add_hotkey(hk['reset_pencolor'], lambda: turtle.color('#000000'))
        add_hotkey(hk['reset_bgcolor'], lambda: screen.bgcolor('#ffffff'))
        add_hotkey(hk['reset_heading'], lambda: turtle.setheading(0))  # Сброс поворота
        add_hotkey(hk['reset_position'], GoBack)
        add_hotkey(hk['clear'], lambda: turtle.clear())  # Очистка
        add_hotkey(hk['reset'], Reset)
        add_hotkey(hk['undo'], lambda: turtle.undo())  # Вернуть
        add_hotkey(hk['pen'], lambda: turtle.penup() if turtle.isdown() else turtle.pendown())  # Поднятие/опускание 'ручки'
        add_hotkey(hk['size+'], lambda: turtle.pensize(turtle.pensize()+1))
        add_hotkey(hk['size-'], lambda: turtle.pensize(turtle.pensize()-1) if not turtle.pensize() else turtle.pensize(1))
        add_hotkey(hk['pencolor'], lambda: turtle.color('#' + ''.join(choices('abcdef0123456789', k = 6))))
        add_hotkey(hk['bgcolor'], lambda: screen.bgcolor('#' + ''.join(choices('abcdef0123456789', k = 6))))
        add_hotkey(hk['fill'], Fill)
        print('Выполнено')  # Вывод информации в консоль

        print('Запись фигур: ', end='')  # Вывод информации в консоль
        figures: list = []  # Объявление списка фигур
        for file in glob(f'{figures_folder}\*'):  # Цикл записи фигур в список
            if open(file, 'r', encoding='utf-8').read() == '1': figures.append(file.replace(f'{figures_folder}\\', '').replace('.txt', ''))  # Если значением у фигуры является '1', то записать фигуру в список
            else: print('Фигура <%s> отключена; ' % file.replace(f"{figures_folder}\\", "").replace(".txt", ""), end='')  # Вывод информации в консоль
        print('Выполнено')  # Вывод информации в консоль

        if len(figures) > 0:

            print('Распределение клавиш вызова фигур: ', end='')  # Вывод информации в консоль
            figures_keys: dict = {}  # Объявление словаря для хранения клавиш фигур
            for file in glob(f'{hotkeys_figures}\*'): figures_keys[file.replace(f'{hotkeys_figures}\\', '').replace('.txt', '')]: 'Клавиши фигур' = open(file, 'r', encoding='utf-8').read()  # Запись клавиш фигур в словарь
            print('Выполнено')  # Вывод информации в консоль

            print('Распределение значений фигур: ', end='')  # Вывод информации в консоль
            values: dict = {}  # Объявление словаря для хранения значений фигур
            for file in glob(fr'{values_figures}\*'):  # Цикл просмотра фигур
                a: dict = {}  # Объявление вспомогательного словаря
                for n in glob(f'{file}\*'):  # Цикл просмотра значений фигур
                    if (data := open(n, 'r', encoding='utf-8').read()).isdigit(): data: int = int(data)  # Если значение является числом, то записать его в виде целого числа
                    a[n.replace(f'{file}\\', '').replace('.txt', '')]: dict = data  # Запись значения во вспомогательный словарь
                values[file.replace(f'{values_figures}\\', '')]: dict = a  # Запись вспомогательного словаря в словарь значений
            print('Выполнено')  # Вывод информации в консоль

            print('Применение параметров фигур: ', end='')  # Вывод информации в консоль
            for i in figures: add_hk(i, figures_keys[i], values[i])  # Применение параметров фигур
            print('Выполнено')  # Вывод информации в консоль

            if len(figures) == 1:
                print(f'Была активирована фигура <{figures[0].replace("figure_", "")}> на клавишу <{figures_keys[figures[0]]}>')
            else:
                print(f'Были активированы фигуры ({len(figures)}):')
                print('\n'.join(sorted([f'<{figures_keys[x]}> - <{x.replace("figure_", "")}>' for x in figures], key=lambda x: x[1])))

        else: print('Фигуры не обнаружены')

        print('\nЗапуск...')  # Вывод информации в консоль
        turtle.mainloop()  # Ожидание закрытия окна
        print('Завершение работы программы...')  # Вывод информации в консоль
        exit()  # Завершение работы программы

    if __name__ == '__main__':
        IntegrityCheck()  # Проверка целостности программы
        exec(open('figures.py', 'r', encoding='utf-8').read())  # Применение алгоритмов фигур

        start()  # Если все пути существуют, то запускаем основную программу
except Exception as error: RaiseError(causes_keys[3], f'Ошибка: {error}')  # Если защита от 102-го сработала, то вызов ошибки
