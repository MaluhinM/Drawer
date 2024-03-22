print('Запуск программы...')
print('Импорт библиотек: ', end='') # Вывод информации в консоль
# Импорт библиотек
import turtle # Для рисования
import keyboard # Для управления
from tkinter import * # Для создания окон ошибок
from os import path # Для проверки существования путей
from sys import exit # Для завершения работы программы
from glob import glob # Для просмотра файлов
print('Выполнено') # Вывод информации в консоль

print('Расчет значений: ', end='') # Вывод информации в консоль

causes = {'Несуществующий путь': 'Отсутствует необходимый для работы программы файл',
          'Несуществующие пути': 'Отсутствуют необходимые для работы программы файлы',
          'Неверное значение': 'Программа получила недопустимое значение на вход из определенного файла'}
causes_keys = tuple(causes.keys())

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

print('Выполнено') # Вывод информации в консоль

# Проверка целостности программы
def integrity_check():
    print('\nПроверка целостности программы...') # Вывод информации в консоль

    print(f'Проверка папки <{data_folder}>: ', end='')
    if not path.exists(data_folder): raise_error(causes_keys[0], f'Отсутствует папка <{data_folder}>') # Проверка наличия папки. В случае ее отсутствия - вызывается ошибка
    print('Выполнено') # Вывод информации в консоль

    print(f'Проверка файла <figures.py>: ', end='')
    if not path.exists('figures.py'): raise_error(causes_keys[0], 'Отсутствует файл <figures.py>') # Проверка наличия папки. В случае ее отсутствия - вызывается ошибка
    print('Выполнено')

    print(f'Проверка папки <{hotkeys_folder}>: ', end='')
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
            txt = causes_keys[0]
            amount = 'Отсутствует путь: '
        else:
            txt = causes_keys[1]
            amount = 'Отсутствуют пути:\n'
        raise_error(txt, amount + ', '.join(errors))
    print('Выполнено') # Вывод информации в консоль

    print(f'Проверка папки <{values_folder}>: ', end='')
    exist = [0] * len(vls)
    for i in range(len(vls)):
        if path.exists(vls[i]): exist[i] = 1
    if 0 in exist:  # Если есть отсутствующие пути
        errors = []  # Объявление массива с ошибками
        for i in range(len(vls)):  # Цикл проверки
            if exist[i] == 0: errors.append('\n' + vls[i])  # Если отсутствует, то записывает отсутствующий путь в массив
        if len(errors) == 1:
            txt = causes_keys[0]
            amount = 'Отсутствует путь: '
        else:
            txt = causes_keys[1]
            amount = 'Отсутствуют пути:\n'
        raise_error(txt, amount + ', '.join(errors))
    print('Выполнено') # Вывод информации в консоль
def FindPossibleCause(error):
    if error in causes: return causes[error] + '\nЕсли Вы не трогали файлы, содержащиеся в директории программы, то единственным выходом будет переустановка программы.\nВ противном случае, попробуйте откатить совершенные изменения. Если ошибка все равно остается - также переустановите программу'
    return 'Не удалось определить причину'
# Вызов ошибки
def raise_error(title, txt):
    print('Программа столкнулась с ошибкой\nОшибка:', title) # Вывод информации в консоль
    print('Возможная причина:', FindPossibleCause(title))
    win = Tk()  # Создание окна для сообщения о проблеме с целостностью программы
    win.resizable(False, False)  # Отключение возможности изменения размера
    win.title(title)  # Имя окна
    Label(win, text=f'{txt}\n\nПереустановите программу', font='Arial 15', bg='black', fg='red').pack()  # Создание и отрисовка лейбла с найденными ошибками и призыву к переустановке программы
    keyboard.add_hotkey('Esc', lambda: win.destroy())
    win.mainloop()  # Ждем закрытия окна
    exit()

def add_hotkey(x, figures_keys, values): keyboard.add_hotkey(figures_keys[x], lambda: eval(f'{x}({values[x]})')) # Добавление горячей клавиши для управления

# Основная программа
def start():
    print('\nЗагрузка и распределение значений...') # Вывод информации в консоль
    title_path = fr'{data_folder}\title.txt'
    if path.exists(title_path):
        with open(title_path, 'r', encoding='utf-8') as f: title_name = f.read().strip()
    if not path.exists(title_path) or title_name in {''}:
        title_name = 'The Minigame by Malukhin Miron -2024 ©️'
        with open(title_path, 'w', encoding='utf-8') as f: f.write(title_name)
    turtle.title(title_name)
    print('Имя окна:', title_name) # Вывод информации в консоль

    speed_path = fr'{data_folder}\speed.txt'
    if path.exists(speed_path):
        with open(speed_path, 'r', encoding='utf-8') as f: speed = f.read()
    if not path.exists(speed_path) or speed in {''}:
        speed = '6'
        with open(speed_path, 'w', encoding='utf-8') as f: f.write(speed)
    if speed.isdigit(): turtle.speed(int(speed))
    else: raise_error(causes_keys[2], f'Значение <{speed}> по пути <{data_folder}\speed.txt> не является натуральным числом')
    print('Установлена скорость:', speed) # Вывод информации в консоль

    print(f'Распределение значений движения: ', end='')
    v = {}
    for i in vls:
        v[i.replace(f'{values_folder}\\', '')] = {}
        for file in glob(f'{i}\*'):
            f = open(file, 'r', encoding='utf-8')
            v[i.replace(f'{values_folder}\\', '')][file.replace(f'{i}\\', '').replace('.txt', '')] = int(f.read())
    base = v['base']
    shift = v['shift']
    ctrl = v['ctrl']
    print('Выполнено') # Вывод информации в консоль

    print(f'Распределение клавиш: ', end='')
    hk = {}
    for i in range(len(hotkeys)):
        if list(hotkeys)[i].replace(f'{hotkeys_folder}\\', '') == 'other':
            for g in keys[i]:
                if path.exists(f'{other_values}\\{g}.txt'):
                    f = open(f'{other_values}\\{g}.txt', 'r', encoding='utf-8')
                    if f.read() == '1':
                        with open(f'{hotkeys[i]}\\{g}.txt', 'r', encoding='utf-8') as f: hk[g] = f.read()
                        continue
                hk[g] = ''
                print(f'Функция {g} отключена') # Вывод информации в консоль
            continue
        for g in keys[i]:
            with open(f'{hotkeys[i]}\\{g}.txt', 'r', encoding='utf-8') as f: hk[g] = f.read()
    print('Выполнено') # Вывод информации в консоль

    print(f'Запись фигур: ', end='')
    figures = []
    for file in glob(f'{figures_folder}\*'):
        f = open(file, 'r', encoding='utf-8')
        if f.read() == '1': figures.append(file.replace(f'{figures_folder}\\', '').replace('.txt', ''))
        else: print('Фигура', file.replace(f'{figures_folder}\\', '').replace('.txt', ''), 'отключена')
    print('Выполнено') # Вывод информации в консоль

    print(f'Распределение клавиш вызова фигур: ', end='')
    figures_keys = {}
    for file in glob(f'{hotkeys_figures}\*'):
        f = open(file, 'r', encoding='utf-8')
        figures_keys[file.replace(f'{hotkeys_figures}\\', '').replace('.txt', '')] = f.read()
    print('Выполнено') # Вывод информации в консоль

    print(f'Распределение значений фигур: ', end='')
    values = {}
    for file in glob(fr'{values_figures}\*'):
        a = {}
        for n in glob(f'{file}\*'):
            f = open(n, 'r', encoding='utf-8')
            a[n.replace(f'{file}\\', '').replace('.txt', '')] = int(f.read())
        else: values[file.replace(f'{values_figures}\\', '')] = a
    print('Выполнено') # Вывод информации в консоль

    print(f'Применение значений фигур: ', end='')
    for i in figures: add_hotkey(i, figures_keys, values)
    print('Выполнено') # Вывод информации в консоль

    print(f'Настройка функций: ', end='')
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
    print('Выполнено') # Вывод информации в консоль

    print('\nЗапуск...') # Вывод информации в консоль
    turtle.mainloop()
    print('Завершение работы программы...') # Вывод информации в консоль
    exit()

integrity_check() # Проверка целостности программы
from figures import * # Для просмотра алгоритмов фигур в файле <figures.py>

# Поднять\опустить 'ручку'
def pen():
    if turtle.isdown(): turtle.penup()
    elif not turtle.isdown(): turtle.pendown()

start() # Если все пути существуют, то запускаем основную программу
