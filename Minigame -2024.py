print('Импорт библиотек...')
# Импорт библиотек
import turtle # Для рисования
import keyboard # Для управления
from tkinter import * # Для создания окон ошибок
from os import path # Для проверки существования путей
from sys import exit # Для завершения работы программы
from glob import glob # Для просмотра файлов
print('Библиотеки загружены')

print('Расчет значений...')

data_folder = fr'data' # Основная папка <data>. В ней соддержатся все данные
hotkeys_folder = fr'{data_folder}\hotkeys' # Папка <hotkeys>. Хранит клавиши или сочетание клавиш для управления
values_folder = fr'{data_folder}\values' # Папка <values>. Хранит значения для управления
figures_folder = fr'{data_folder}\figures' # Папка <figures>. Хранит названия фигур и значения для их использования

hotkeys_figures = fr'{hotkeys_folder}\figures' # Папка <hotkeys\figures>. Хранит клавиши или сочетание клавиш для вызова той или иной фигуры
values_figures = fr'{values_folder}\figures' # Папка <values\figures>. Хранит значения, используемые фигурами

base_hotkeys = fr'{hotkeys_folder}\base' # Папка <hotkeys\base>. Хранит клавиши или сочетание клавиш для обычного перемещения
shift_hotkeys = fr'{hotkeys_folder}\shift' # Папка <hotkeys\shift>. Хранит клавиши или сочетание клавиш для перемещения с клавишей Shift
ctrl_hotkeys = fr'{hotkeys_folder}\ctrl' # Папка <hotkeys\ctrl>. Хранит клавиши или сочетание клавиш для перемещения с клавишей Ctrl
other_hotkeys = fr'{hotkeys_folder}\other' # Папка <hotkeys\other>. Хранит клавиши или сочетание клавиш для прочих функций программы

hotkeys = (base_hotkeys, shift_hotkeys, ctrl_hotkeys, other_hotkeys) # Переменная для хранения папок <hotkeys\*>

base_values = fr'{values_folder}\base' # Папка <values\base>. Хранит значения для обычного перемещения
shift_values = fr'{values_folder}\shift' # Папка <values\shift>. Хранит значения для перемещения с клавишей Shift
ctrl_values = fr'{values_folder}\ctrl' # Папка <values\ctrl>. Хранит значения для перемещения с клавишей Ctrl

other_values = fr'{values_folder}\other' # Папка <hotkeys\other>. Хранит значения, отвечающие за вкл.\выкл. прочих функций программы

vls = (base_values, shift_values, ctrl_values) # Переменная для хранения папок <values\*>

base_keys = ('forward', 'backward', 'left', 'right') # Функции обычного перемещения
shift_keys = ('shift_forward', 'shift_backward', 'shift_left', 'shift_right') # Функции для перемещения с клавишей Shift
ctrl_keys = ('ctrl_forward', 'ctrl_backward', 'ctrl_left', 'ctrl_right') # Функции для перемещения с клавишей Ctrl
other_keys = ('exit', 'clear', 'reset_heading', 'pen', 'undo') # Прочие функции программы

keys = (base_keys, shift_keys, ctrl_keys, other_keys) # Переменная для хранения функций

print('Значения расчитаны\n',)

# Проверка целостности программы
def integrity_check():
    print('Проверка целостности программы...')
    if not path.exists(data_folder): raise_error('Несуществующий путь', f'Отсутствует папка <{data_folder}>')
    print(f'Папка <{data_folder}> проверена')
    if not path.exists('figures.py'): raise_error('Несуществующий путь', 'Отсутствует файл <figures.py>')

    exist = [0] * len(hotkeys)
    for i in range(len(hotkeys)):
        if path.exists(hotkeys[i]): exist[i] = 1
    if 0 in exist:  # Если есть отсутствующие пути
        errors = []  # Объявление массива с ошибками
        for i in range(len(hotkeys)):  # Цикл проверки
            if exist[i] == 0: errors.append('\n' + hotkeys[i])  # Если отсутствует, то записывает отсутствующий путь в массив
        if len(errors) == 1:
            txt = 'Несуществующий путь'
            amount = 'Отсутствует путь: '
        else:
            txt = 'Несуществующие пути'
            amount = 'Отсутствуют пути:\n'
        raise_error(txt, amount + ', '.join(errors) + '\n\nПереустановите программу')

    n = 0
    for i in range(len(keys)):
        for g in range(len(keys[i])): n += 1
    exist = [0] * n

    n = 0
    for i in range(len(keys)):
        for g in range(len(keys[i])):
            if path.exists(f'{hotkeys[i]}\\{keys[i][g]}.txt'): exist[n] = 1
            n += 1
    if 0 in exist: # Если есть отсутствующие пути
        errors = []  # Объявление массива с ошибками
        n = 0
        for i in range(len(keys)):
            for g in range(len(keys[i])):  # Цикл проверки
                if exist[n] == 0: errors.append(f'\n{hotkeys[i]}\\{keys[i][g]}.txt')  # Если отсутствует, то записывает отсутствующий путь в массив
                n += 1
        if len(errors) == 1:
            txt = 'Несуществующий путь'
            amount = 'Отсутствует путь: '
        else:
            txt = 'Несуществующие пути'
            amount = 'Отсутствуют пути:\n'
        raise_error(txt, amount + ', '.join(errors) + '\n\nПереустановите программу')
    print(f'Путь <{hotkeys_folder}> и его содержимое проверено')

    exist = [0] * len(vls)
    for i in range(len(vls)):
        if path.exists(vls[i]): exist[i] = 1
    if 0 in exist:  # Если есть отсутствующие пути
        errors = []  # Объявление массива с ошибками
        for i in range(len(vls)):  # Цикл проверки
            if exist[i] == 0: errors.append('\n' + vls[i])  # Если отсутствует, то записывает отсутствующий путь в массив
        if len(errors) == 1:
            txt = 'Несуществующий путь'
            amount = 'Отсутствует путь: '
        else:
            txt = 'Несуществующие пути'
            amount = 'Отсутствуют пути:\n'
        raise_error(txt, amount + ', '.join(errors) + '\n\nПереустановите программу')
    print(f'Путь <{values_folder}> и его содержимое проверено\n')
# Вызов ошибки
def raise_error(title, txt):
    print('Ошибка:', title)
    win = Tk()  # Создание окна для сообщения о проблеме с целостностью программы
    win['bg'] = 'red'  # Цвет окна
    win.resizable(False, False)  # Отключение возможности изменения размера
    win.title(title)  # Имя окна
    Label(win, text=txt, font='Arial 15', bg='black', fg='red').pack()  # Создание и отрисовка лейбла с найденными ошибками и призыву к переустановке программы
    win.mainloop()  # Ждем закрытия окна
    exit()

def add_hotkey(x, figures_keys, values): keyboard.add_hotkey(figures_keys[x], lambda: exec(f'{x}({values[x]})')) # Добавление горячей клавиши для управления

# Поднять\опустить 'ручку'
def pen():
    if turtle.isdown():
        print('Поднимаю ручку...')
        turtle.penup()
    elif not turtle.isdown():
        print('Опускаю ручку...')
        turtle.pendown()

# Основная программа
def start():
    print('Загрузка и распределение значений...')
    title_path = fr'{data_folder}\title.txt'
    if path.exists(title_path):
        with open(title_path, 'r', encoding='utf-8') as f: title_name = f.read().strip()
    if not path.exists(title_path) or title_name in {''}:
        title_name = 'The Minigame by Malukhin Miron -2024 ©️'
        with open(title_path, 'w', encoding='utf-8') as f: f.write(title_name)
    turtle.title(title_name)
    print('Имя окна:', title_name)

    speed_path = fr'{data_folder}\speed.txt'
    if path.exists(speed_path):
        with open(speed_path, 'r', encoding='utf-8') as f: speed = f.read()
    if not path.exists(speed_path) or speed in {''}:
        speed = '6'
        with open(speed_path, 'w', encoding='utf-8') as f: f.write(speed)
    if speed.isdigit(): turtle.speed(int(speed))
    else: raise_error('Неверное значение', f'Значение по пути <{data_folder}\speed.txt> не является натуральным числом')
    print('Установлена скорость:', speed)

    v = {}
    for i in vls:
        v[i.replace(f'{values_folder}\\', '')] = {}
        for file in glob(f'{i}\*'):
            f = open(file, 'r', encoding='utf-8')
            v[i.replace(f'{values_folder}\\', '')][file.replace(f'{i}\\', '').replace('.txt', '')] = int(f.read())
    base = v['base']
    shift = v['shift']
    ctrl = v['ctrl']
    print('Значения движения распределены')

    hk = {}
    for i in range(len(hotkeys)):
        if list(hotkeys)[i].replace(f'{hotkeys_folder}\\', '') == 'other':
            for g in keys[i]:
                if path.exists(f'{other_values}\\{g}.txt'):
                    f = open(f'{other_values}\\{g}.txt', 'r', encoding='utf-8')
                    if f.read() == '1':
                        with open(f'{hotkeys[i]}\\{g}.txt', 'r', encoding='utf-8') as f: hk[g] = f.read()
                        continue
                print(f'Функция {g} отключена')
                hk[g] = ''
            continue
        for g in keys[i]:
            with open(f'{hotkeys[i]}\\{g}.txt', 'r', encoding='utf-8') as f: hk[g] = f.read()
    print('Клавиши движения и прочих функций распределены')

    figures = []
    for file in glob(f'{figures_folder}\*'):
        f = open(file, 'r', encoding='utf-8')
        if f.read() == '1': figures.append(file.replace(f'{figures_folder}\\', '').replace('.txt', ''))
        else: print('Фигура', file.replace(f'{figures_folder}\\', '').replace('.txt', ''), 'отключена')
    print('Фигуры записаны')

    figures_keys = {}
    for file in glob(f'{hotkeys_figures}\*'):
        f = open(file, 'r', encoding='utf-8')
        figures_keys[file.replace(f'{hotkeys_figures}\\', '').replace('.txt', '')] = f.read()
    print('Клавиши для вызова фигур распределены')

    values = {}
    for file in glob(fr'{values_figures}\*'):
        a = {}
        for n in glob(f'{file}\*'):
            f = open(n, 'r', encoding='utf-8')
            a[n.replace(f'{file}\\', '').replace('.txt', '')] = int(f.read())
        else: values[file.replace(f'{values_figures}\\', '')] = a
    print('Значения фигур распределены')

    for i in figures: add_hotkey(i, figures_keys, values)
    print('Значения фигур применены')

    keyboard.add_hotkey(hk['forward'], lambda: turtle.forward(base['forward']))
    keyboard.add_hotkey(hk['backward'], lambda: turtle.backward(base['backward']))
    keyboard.add_hotkey(hk['left'], lambda: turtle.left(base['left']))
    keyboard.add_hotkey(hk['right'], lambda: turtle.right(base['right']))
    keyboard.add_hotkey(hk['shift_forward'], lambda: turtle.forward(shift['shift_forward']))
    keyboard.add_hotkey(hk['shift_backward'], lambda: turtle.backward(shift['shift_backward']))
    keyboard.add_hotkey(hk['shift_left'], lambda: turtle.left(shift['shift_left']))
    keyboard.add_hotkey(hk['shift_right'], lambda: turtle.right(shift['shift_right']))
    keyboard.add_hotkey(hk['ctrl_forward'], lambda: turtle.forward(ctrl['ctrl_forward']))
    keyboard.add_hotkey(hk['ctrl_backward'], lambda: turtle.backward(ctrl['ctrl_backward']))
    keyboard.add_hotkey(hk['ctrl_left'], lambda: turtle.left(ctrl['ctrl_left']))
    keyboard.add_hotkey(hk['ctrl_right'], lambda: turtle.right(ctrl['ctrl_right']))

    if hk['exit'] != '':
        keyboard.add_hotkey(hk['exit'], lambda: turtle.bye())
    if hk['reset_heading'] != '':
        keyboard.add_hotkey(hk['reset_heading'], lambda: turtle.setheading(0))
    if hk['clear'] != '':
        keyboard.add_hotkey(hk['clear'], lambda: turtle.clear())
    if hk['undo'] != '':
        keyboard.add_hotkey(hk['undo'], lambda: turtle.undo())
    if hk['pen'] != '':
        keyboard.add_hotkey(hk['pen'], pen)
    print('Функции настроены\n')

    print('Запуск...')
    turtle.mainloop()
    print('Завершение работы программы...')
    exit()

integrity_check() # Проверка целостности программы
from figures import * # Для просмотра алгоритмов фигур в файле <figures.py>
start() # Если все пути существуют, то запускаем основную программу
