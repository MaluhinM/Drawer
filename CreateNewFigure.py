print('Запуск программы...') # Вывод информации в консоль
print('Импорт библиотек: ', end='') # Вывод информации в консоль
from turtle import *
from os import path, mkdir
from glob import glob
from keyboard import add_hotkey
from tkinter.messagebox import showerror  # Создание окон ошибок
from sys import exit # Завершение работы программы
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

def IntegrityCheck(): # Проверка целостности программы
    print('\nПроверка целостности программы...') # Вывод информации в консоль

    print(f'Проверка папки <{data_folder}>: ', end='') # Вывод информации в консоль
    if not path.exists(data_folder): RaiseError(causes_keys[0], f'Отсутствует папка <{data_folder}>') # Проверка наличия папки. В случае ее отсутствия - вызывается ошибка
    print('Выполнено') # Вывод информации в консоль

    print('Проверка файла <figures.py>: ', end='')  # Вывод информации в консоль
    if not path.exists('figures.py'):
        print('Файл <figures.py> не найден. Создание нового: ', end='')  # Вывод информации в консоль
        open('figures.py', 'w', encoding='utf-8').write('from turtle import *\n\n')  # Проверка наличия файла. В случае его отсутствия - записывается
    print('Выполнено')  # Вывод информации в консоль

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
        RaiseError(txt, amount + ', '.join(errors)) # Вызов соответствующей ошибки

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
        RaiseError(txt, amount + ', '.join(errors)) # Вызов ошибки
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
        RaiseError(txt, amount + ', '.join(errors)) # Вызов ошибки
    print('Выполнено') # Вывод информации в консоль
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


def write(name, key):
    if input(f'Нажмите <Enter>, чтобы подтвердить создание фигуры <{name}>: ') == '':
        with open(fr'{figures_folder}\{name}.txt', 'w', encoding='utf-8') as f: f.write('1')
        with open(fr'{hotkeys_figures}\{name}.txt', 'w', encoding='utf-8') as f: f.write(key)
        mkdir(fr'{values_figures}\{name.replace(f"{figures_folder}/", "")}')
        print('\nОсновные файлы для фигуры были созданы.'
              '\nОстается написать код для нее в файле <figures.py> в виде функции '
              fr'и задать необходимые значения в созданной папке <{values_figures}\{name.replace(f"{figures_folder}/", "")}>')
        if input('Нажмите <Enter> для перехода к написанию алгоритма: ') == '': algorithm(name)
    else: print('Отменено')
    input('Нажмите <Enter> для завершения работы программы: ')


def algorithm(name):
    alg = f'\ndef {name}(x):\n\t'
    test = alg
    n = 1
    while True:
        check, croissant = 1, 1
        print(test, end='')
        try:
            if (a := input().strip()) == '': break
            if a[-1] == ':':
                n += 1
                check = 0
            if a == 'cd..':
                if n > 1: n -= 1
                alg = alg[::-1].replace('\t', '', 1)[::-1]
                test = test[::-1].replace('\t', '', 1)[::-1]
                check = 0
                continue
            if 'x' in a:
                croissant = 0
                check = 0
            if check == 1:
                print('Проверка... ', end='')
                exec(a)
                print()
            if croissant == 1: alg += a + '\n' + '\t'*n
            test += a + '\n' + '\t'*n
            if check == 1: exec(test)
        except Exception as error: print(error)
    try:
        exec(test)
        open('figures.py', 'a', encoding='utf-8').write(test)
        print('Алгоритм был записан в файл <figures.py>')
    except Exception as error: print('Кажется, алгоритм задан неверно. Ошибка:', error)


def start():
    CannotBeUsed = ' \\/:*?"<>|'
    while True:
        symbols = []
        name = input('\nНазвание новой фигуры (желательно на английском): ').strip()
        if name in {''}:
            print('Недопустимое имя фигуры')
            continue
        if path.exists(fr'{figures_folder}\{name}.txt') or path.exists(fr'{figures_folder}\figure_{name}.txt'):
            print(f'\nФигура <{name.replace("figure_", "")}> уже существует. Придумайте что-то новое')
            continue
        for i in name:
            if i not in symbols and i in CannotBeUsed: symbols.append(i)
        if symbols != []:
            if len(symbols) == 1:
                print(f'В названии присутствует недопустимый символ: {symbols}')
                continue
            elif len(symbols) > 1:
                print(f'В названии присутствуют недопустимые символы: {symbols}')
                continue
        if name[:7] != 'figure_': name = 'figure_' + name
        break
    while True:
        key = input('Клавиша для использования фигуры (возможно сочетание): ').strip()

        try: add_hotkey(key, lambda: print(end=''))
        except:
            print(f'\nКажется, Вы ввели несуществующую клавишу или комбинацию клавиш: <{key}>. Попробуйте еще раз')
            continue

        CannotBeUsed = []
        for file in glob(f'{hotkeys_folder}\*'):
            for n in glob(f'{file}\*.txt'):
                f = open(n, 'r', encoding='utf-8')
                CannotBeUsed.append(f.read())
        if key in CannotBeUsed:
            print(f'\nКлавиша или сочетание клавиш <{key}> уже используется.'
                  f'\nВозможности программы позволяют это сделать, однако ее работа может стать некорректной.'
                  f'\nВы хотите продолжить?\n')
            if input('<Enter> для продолжения: ') == '': break
            continue
        break
    write(name, key)

if __name__ == '__main__':
    IntegrityCheck()
    start()
