try: # Защита от 102-го
    print('Запуск программы...') # Вывод информации в консоль
    print('Импорт библиотек: ', end='') # Вывод информации в консоль
    # Импорт библиотек
    import turtle # Рисование
    import keyboard # Управление
    from tkinter import Tk, Label, mainloop # Создание окон ошибок
    from os import path # Проверка наличия путей
    from sys import exit # Завершение работы программы
    from glob import glob # Просмотр файлов
    print('Выполнено') # Вывод информации в консоль

    print('Расчет значений: ', end='') # Вывод информации в консоль

    # Ошибки и их возможные причины
    causes = {'Несуществующий путь': 'Отсутствует необходимый для работы программы файл',
              'Несуществующие пути': 'Отсутствуют необходимые для работы программы файлы',
              'Неверное значение': 'Программа получила недопустимое значение на вход из определенного файла',
              'Непредвиденная ошибка': 'В работе программы произошел сбой'}
    causes_keys = tuple(causes.keys()) # Названия ошибок

    data_folder = 'data' # Основная папка <data>. В ней содержится большинство данных
    hotkeys_folder = f'{data_folder}\hotkeys' # Папка <hotkeys>. Хранит клавиши или сочетание клавиш для управления
    values_folder = fr'{data_folder}\values' # Папка <values>. Хранит значения для управления
    figures_folder = fr'{data_folder}\figures' # Папка <figures>. Хранит названия фигур и значения для их использования

    hotkeys_figures = fr'{hotkeys_folder}\figures' # Папка <hotkeys\figures>. Хранит клавиши или сочетание клавиш для вызова той или иной фигуры
    values_figures = fr'{values_folder}\figures' # Папка <values\figures>. Хранит значения, используемые фигурами

    base_hotkeys = fr'{hotkeys_folder}\base' # Папка <hotkeys\base>. Хранит клавиши или сочетание клавиш для обычного перемещения
    shift_hotkeys = f'{hotkeys_folder}\shift' # Папка <hotkeys\shift>. Хранит клавиши или сочетание клавиш для перемещения с клавишей Shift
    ctrl_hotkeys = f'{hotkeys_folder}\ctrl' # Папка <hotkeys\ctrl>. Хранит клавиши или сочетание клавиш для перемещения с клавишей Ctrl
    other_hotkeys = f'{hotkeys_folder}\other' # Папка <hotkeys\other>. Хранит клавиши или сочетание клавиш для прочих функций программы
    hotkeys = (base_hotkeys, shift_hotkeys, ctrl_hotkeys, other_hotkeys) # Переменная для хранения папок <hotkeys\*>

    base_values = fr'{values_folder}\base' # Папка <values\base>. Хранит значения для обычного перемещения
    shift_values = f'{values_folder}\shift' # Папка <values\shift>. Хранит значения для перемещения с клавишей Shift
    ctrl_values = f'{values_folder}\ctrl' # Папка <values\ctrl>. Хранит значения для перемещения с клавишей Ctrl
    other_values = f'{values_folder}\other' # Папка <hotkeys\other>. Хранит значения, отвечающие за вкл.\выкл. прочих функций программы
    vls = (base_values, shift_values, ctrl_values) # Переменная для хранения папок <values\*>

    base_keys = ('forward', 'backward', 'left', 'right') # Функции обычного перемещения
    shift_keys = ('shift_forward', 'shift_backward', 'shift_left', 'shift_right') # Функции для перемещения с клавишей Shift
    ctrl_keys = ('ctrl_forward', 'ctrl_backward', 'ctrl_left', 'ctrl_right') # Функции для перемещения с клавишей Ctrl
    other_keys = ('exit', 'clear', 'reset_heading', 'pen', 'undo') # Прочие функции программы
    keys = (base_keys, shift_keys, ctrl_keys, other_keys) # Переменная для хранения функций

    print('Выполнено') # Вывод информации в консоль

    def integrity_check(): # Проверка целостности программы
        print('\nПроверка целостности программы...') # Вывод информации в консоль

        print(f'Проверка папки <{data_folder}>: ', end='') # Вывод информации в консоль
        if not path.exists(data_folder): raise_error(causes_keys[0], f'Отсутствует папка <{data_folder}>') # Проверка наличия папки. В случае ее отсутствия - вызывается ошибка
        print('Выполнено') # Вывод информации в консоль

        print('Проверка файла <figures.py>: ', end='') # Вывод информации в консоль
        if not path.exists('figures.py'): raise_error(causes_keys[0], 'Отсутствует файл <figures.py>') # Проверка наличия папки. В случае ее отсутствия - вызывается ошибка
        print('Выполнено') # Вывод информации в консоль

        print(f'Проверка папки <{hotkeys_folder}>: ', end='') # Вывод информации в консоль
        exist = [0] * len(hotkeys) # Создание списка для отметки наличия путей
        for i in range(len(hotkeys)): # Цикл проверки наличия путей
            if path.exists(hotkeys[i]): exist[i] = 1 # Наличие пути отмечается в списке
        if 0 in exist: # Если есть отсутствующие пути
            errors = [] # Объявление списка с ошибками
            for i in range(len(hotkeys)): # Цикл проверки
                if exist[i] == 0: errors.append('\n' + hotkeys[i]) # Если отсутствует, то записывает отсутствующий путь в список
            if len(errors) == 1: # Если отсутствует всего один путь
                txt = causes_keys[0] # Оглавление ошибки в единственном числе
                amount = 'Отсутствует путь: ' # Информация об ошибке в единственном числе
            else: # Если количество отсутствующих больше одного
                txt = causes_keys[1] # Оглавление ошибки во множественном числе
                amount = 'Отсутствуют пути:\n' # Информация об ошибке во множественном числе
            raise_error(txt, amount + ', '.join(errors)) # Вызов соответствующей ошибки

        n = 0 # Счетчик количества путей
        for i in range(len(keys)): # Цикл для счетчика
            for g in range(len(keys[i])): n += 1 # Счет количества путей
        exist = [0] * n # Создание списка для записи несуществующих путей

        n = 0 # Счетчик
        for i in range(len(keys)): # Цикл проверки
            for g in range(len(keys[i])): # Проверка функций
                if path.exists(f'{hotkeys[i]}\\{keys[i][g]}.txt'): exist[n] = 1 # Если путь существует, то его присутствие отмечается в списке
                n += 1 # К счетчику прибавляется 1
        if 0 in exist: # Если есть отсутствующие пути
            errors = [] # Объявление списка с ошибками
            n = 0 # Счетчик
            for i in range(len(keys)): # Цикл проверки
                for g in range(len(keys[i])): # Проверка функций
                    if exist[n] == 0: errors.append(f'\n{hotkeys[i]}\\{keys[i][g]}.txt') # Если отсутствует, то записывает отсутствующий путь в список
                    n += 1 # К счетчику прибавляется 1
            if len(errors) == 1: # Если ошибка всего одна
                txt = causes_keys[0] # Имя ошибки в ед. числе
                amount = 'Отсутствует путь: ' # Текст ошибки в ед. числе
            else: # Если количество ошибок больше одного
                txt = causes_keys[1] # Имя ошибки во мн. числе
                amount = 'Отсутствуют пути:\n' # Текст ошибки во мн. числе
            raise_error(txt, amount + ', '.join(errors)) # Вызов ошибки
        print('Выполнено') # Вывод информации в консоль

        print(f'Проверка папки <{values_folder}>: ', end='') # Вывод информации в консоль
        exist = [0] * len(vls) # Создание списка для хранения информации о путях
        for i in range(len(vls)): # Цикл проверки
            if path.exists(vls[i]): exist[i] = 1 # Если путь существует, то его присутствие отмечается в списке
        if 0 in exist: # Если есть отсутствующие пути
            errors = [] # Объявление списка с ошибками
            for i in range(len(vls)): # Цикл проверки
                if exist[i] == 0: errors.append('\n' + vls[i]) # Если отсутствует, то записывает отсутствующий путь в список
            if len(errors) == 1: # Если ошибка всего одна
                txt = causes_keys[0] # Имя ошибки в ед. числе
                amount = 'Отсутствует путь: ' # Текст ошибки в ед. числе
            else: # Если количество ошибок больше одного
                txt = causes_keys[1] # Имя ошибки во мн. числе
                amount = 'Отсутствуют пути:\n' # Текст ошибки во мн. числе
            raise_error(txt, amount + ', '.join(errors)) # Вызов ошибки
        print('Выполнено') # Вывод информации в консоль
    def FindPossibleCause(error): # Нахождение возможной причины ошибки (принимает имя ошибки)
        if error in causes: return causes[error] + '\nЕсли Вы не трогали файлы, содержащиеся в директории программы, то единственным выходом будет переустановка программы.\nВ противном случае, попробуйте откатить совершенные изменения. Если ошибка все равно остается - также переустановите программу' # Если ошибка присутствует в списке, то вернуть причину
        return 'Не удалось определить причину' # Если ошибки нет в списке, то вернуть отрицательный результат поиска
    def raise_error(title, txt): # Вызов ошибки (принимает имя и текст ошибки)
        print('Программа столкнулась с ошибкой\nОшибка:', title) # Вывод информации в консоль
        print('Возможная причина:', FindPossibleCause(title)) # Вывод информации в консоль
        win = Tk() # Создание окна для сообщения о проблеме с целостностью программы
        win.resizable(False, False) # Отключение возможности изменения размера
        win.title(title) # Имя окна
        Label(win, text=f'{txt}\n\nПереустановите программу', font='Arial 15', bg='black', fg='red').pack() # Создание и отрисовка лейбла с найденными ошибками и призыву к переустановке программы
        keyboard.add_hotkey('Esc', lambda: win.destroy()) # Назначение клавиши Esc на завершение работы программы
        win.mainloop() # Ждем закрытия окна
        exit() # Завершение работы программы

    def add_hotkey(x, figures_keys, values): keyboard.add_hotkey(figures_keys[x], lambda: eval(f'{x}({values[x]})')) # Добавление горячей клавиши для управления

    def start(): # Основная программа
        print('\nЗагрузка и распределение значений...') # Вывод информации в консоль
        title_path = fr'{data_folder}\title.txt' # Объявление пути до файла имени окна
        if path.exists(title_path): title_name = open(title_path, 'r', encoding='utf-8').read().strip() # Проверка присутствия пути и запись имени окна в переменную
        if not path.exists(title_path) or title_name in {''}: # Если путь отсутствует или оно пустое
            title_name = 'The Minigame by Malukhin Miron -2024 ©️' # Запись стандартного имени окна в переменную
            open(title_path, 'w', encoding='utf-8').write(title_name) # Запись информации в файл
        turtle.title(title_name) # Применение имени окна
        print('Имя окна:', title_name) # Вывод информации в консоль

        speed_path = fr'{data_folder}\speed.txt' # Объявление пути до файла скорости
        if path.exists(speed_path): speed = open(speed_path, 'r', encoding='utf-8').read() # Проверка присутствия пути и запись скорости в переменную
        if not path.exists(speed_path) or not speed.isdigit(): # Если путь отсутствует или значение скорости не число
            speed = '6' # Запись стандартной скорости в переменную
            open(speed_path, 'w', encoding='utf-8').write(speed) # Запись информации в файл
        turtle.speed(int(speed)) # Применение скорости
        print('Установлена скорость:', speed) # Вывод информации в консоль

        print('Распределение значений движения: ', end='') # Вывод информации в консоль
        v = {} # Объявление словаря для хранения значений функций
        for i in vls: # Цикл записи информации в словарь
            v[i.replace(f'{values_folder}\\', '')] = {} # Создание отдельных словарей внутри словаря
            for file in glob(f'{i}\*'): v[i.replace(f'{values_folder}\\', '')][file.replace(f'{i}\\', '').replace('.txt', '')] = int(open(file, 'r', encoding='utf-8').read()) # Запись значений функций в словари
        base = v['base'] # Применение значений для функций стандартного передвижения
        shift = v['shift'] # Применение значений для функций передвижения с клавишей Shift
        ctrl = v['ctrl'] # Применение значений для функций передвижения с клавишей Ctrl
        print('Выполнено') # Вывод информации в консоль

        print('Распределение клавиш: ', end='') # Вывод информации в консоль
        hk = {} # Объявление словаря для хранения горячих клавиш
        for i in range(len(hotkeys)): # Цикл записи клавиш в словарь
            if list(hotkeys)[i].replace(f'{hotkeys_folder}\\', '') == 'other': # Если разделом клавиш является 'Прочее'
                for g in keys[i]: # Цикл проверки состояния функций
                    hk[g] = open(f'{hotkeys[i]}\\{g}.txt', 'r', encoding='utf-8').read() # Запись клавиши для вызова функции
                    if not path.exists(f'{other_values}\\{g}.txt') or not open(f'{other_values}\\{g}.txt', 'r', encoding='utf-8').read() == '1': # Если путь отсутствует или значением файла не является '1'
                        keyboard.block_key(open(f'{hotkeys[i]}\\{g}.txt', 'r', encoding='utf-8').read()) # Блокировка клавиши
                        print(f'Функция <{g}> отключена; ', end='') # Вывод информации в консоль
                continue # Продолжить
            for g in keys[i]: hk[g] = open(f'{hotkeys[i]}\\{g}.txt', 'r', encoding='utf-8').read() # Запись клавиш для вызова функций
        print('Выполнено') # Вывод информации в консоль

        print('Запись фигур: ', end='') # Вывод информации в консоль
        figures = [] # Объявление списка фигур
        for file in glob(f'{figures_folder}\*'): # Цикл записи фигур в список
            if open(file, 'r', encoding='utf-8').read() == '1': figures.append(file.replace(f'{figures_folder}\\', '').replace('.txt', '')) # Если значением у фигуры является '1', то записать фигуру в список
            else: print('Фигура <%s> отключена; ' % file.replace(f"{figures_folder}\\", "").replace(".txt", ""), end='') # Вывод информации в консоль
        print('Выполнено') # Вывод информации в консоль

        print('Распределение клавиш вызова фигур: ', end='') # Вывод информации в консоль
        figures_keys = {} # Объявление словаря для хранения клавиш фигур
        for file in glob(f'{hotkeys_figures}\*'): figures_keys[file.replace(f'{hotkeys_figures}\\', '').replace('.txt', '')] = open(file, 'r', encoding='utf-8').read() # Запись клавиш фигур в словарь
        print('Выполнено') # Вывод информации в консоль

        print('Распределение значений фигур: ', end='') # Вывод информации в консоль
        values = {} # Объявление словаря для хранения значений фигур
        for file in glob(fr'{values_figures}\*'): # Цикл просмотра фигур
            a = {} # Объявление вспомогательного словаря
            for n in glob(f'{file}\*'): # Цикл просмотра значений фигур
                if (data:=open(n, 'r', encoding='utf-8').read()).isdigit(): data = int(data) # Если значение является числом, то записать его в виде целого числа
                a[n.replace(f'{file}\\', '').replace('.txt', '')] = data # Запись значения во вспомогательный словарь
            values[file.replace(f'{values_figures}\\', '')] = a # Запись вспомогательного словаря в словарь значений
        print('Выполнено') # Вывод информации в консоль

        print('Применение параметров фигур: ', end='') # Вывод информации в консоль
        for i in figures: add_hotkey(i, figures_keys, values) # Применение параметров фигур
        print('Выполнено') # Вывод информации в консоль

        print(f'Настройка функций: ', end='') # Вывод информации в консоль
        # Применение параметров функций
        keyboard.add_hotkey(hk['forward'], lambda: turtle.forward(base['forward'])) # Стандартное движение вперед
        keyboard.add_hotkey(hk['backward'], lambda: turtle.backward(base['backward'])) # Стандартное движение назад
        keyboard.add_hotkey(hk['left'], lambda: turtle.left(base['left'])) # Стандартный поворот влево
        keyboard.add_hotkey(hk['right'], lambda: turtle.right(base['right'])) # Стандартный поворот вправо
        keyboard.add_hotkey(hk['shift_forward'], lambda: turtle.forward(shift['shift_forward'])) # Движение вперед с клавишей Shift
        keyboard.add_hotkey(hk['shift_backward'], lambda: turtle.backward(shift['shift_backward'])) # Движение назад с клавишей Shift
        keyboard.add_hotkey(hk['shift_left'], lambda: turtle.left(shift['shift_left'])) # Поворот влево с клавишей Shift
        keyboard.add_hotkey(hk['shift_right'], lambda: turtle.right(shift['shift_right'])) # Поворот вправо с клавишей Shift
        keyboard.add_hotkey(hk['ctrl_forward'], lambda: turtle.forward(ctrl['ctrl_forward'])) # Движение вперед с клавишей Ctrl
        keyboard.add_hotkey(hk['ctrl_backward'], lambda: turtle.backward(ctrl['ctrl_backward'])) # Движение назад с клавишей Ctrl
        keyboard.add_hotkey(hk['ctrl_left'], lambda: turtle.left(ctrl['ctrl_left'])) # Поворот влево с клавишей Ctrl
        keyboard.add_hotkey(hk['ctrl_right'], lambda: turtle.right(ctrl['ctrl_right'])) # Поворот вправо с клавишей Ctrl

        keyboard.add_hotkey(hk['exit'], lambda: turtle.bye()) # Завершение работы программы
        keyboard.add_hotkey(hk['reset_heading'], lambda: turtle.setheading(0)) # Сброс поворота
        keyboard.add_hotkey(hk['clear'], lambda: turtle.clear()) # Очистка
        keyboard.add_hotkey(hk['undo'], lambda: turtle.undo()) # Вернуть
        keyboard.add_hotkey(hk['pen'], pen) # Поднятие\опускание 'ручки'
        print('Выполнено') # Вывод информации в консоль

        print('\nЗапуск...') # Вывод информации в консоль
        turtle.mainloop() # Ожидание закрытия окна
        print('Завершение работы программы...') # Вывод информации в консоль
        exit() # Завершение работы программы

    integrity_check() # Проверка целостности программы
    exec(open('figures.py', 'r', encoding='utf-8').read()) # Применение алгоритмов фигур

    def pen(): # Поднять\опустить 'ручку'
        if turtle.isdown(): turtle.penup() # Поднятие 'ручки'
        elif not turtle.isdown(): turtle.pendown() # Опускание 'ручки'

    start() # Если все пути существуют, то запускаем основную программу
except Exception as error: raise_error(causes_keys[3], f'Ошибка: {error}') # Если защита от 102-го сработала, то вызов ошибки