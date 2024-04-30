print('Запуск программы...') # Вывод информации в консоль
print('Импорт библиотек: ', end='') # Вывод информации в консоль
from glob import glob
from sys import exit # Завершение работы программы
from os import path, remove # Проверка наличия путей и удаление файлов
from shutil import rmtree # Удаление папок
from tkinter.messagebox import showerror  # Создание окон ошибок
from keyboard import add_hotkey # Управление
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


def CleanUp():
    print('\nПросмотр файлов...')
    for file in glob(f'{values_figures}\*'):
        if path.isfile(file): remove(file)
    figures = [x.replace(f'{figures_folder}\\', '') for x in glob(f'{figures_folder}\*')]
    figures_hk = [x.replace(f'{hotkeys_figures}\\', '') for x in glob(f'{hotkeys_figures}\*')]
    figures_vls = [x.replace(f'{values_figures}\\', '') for x in glob(f'{values_figures}\*')]
    if not [x.replace('.txt', '') for x in figures] == [x.replace('.txt', '') for x in figures_hk] == figures_vls:
        print('Очистка мусора: ', end='')
        junk = set(figures + figures_hk + figures_vls)
        for i in figures:
            for g in figures_hk:
                if g in i: junk.discard(g)
            for g in figures_vls:
                if g in i: junk.discard(g)
        print(f'{junk}; ', end='')
        for i in junk:
            delete(fr'{figures_folder}\{i}')
            delete(fr'{hotkeys_figures}\{i}')
            delete(fr'{values_figures}\{i}')
        print('Выполнено')


def delete(x):
    if path.isfile(x): remove(x)
    elif path.isdir(x): rmtree(x)


def start():
    figures = [x.replace(f'{figures_folder}\\', '').replace('.txt', '') for x in glob(f'{figures_folder}\*')]
    length = len(figures)
    if length == 0: print('Фигуры не были обнаружены')
    for i in range(length):
        while True:
            figures = [x.replace(f'{figures_folder}\\', '').replace('.txt', '') for x in glob(f'{figures_folder}\*')]
            print('\nСписок имеющихся фигур:\n%s' % '\n'.join([f'{figures.index(x) + 1}. {x.replace("figure_", "")}' for x in figures]))
            if (a := input(fr'Удалить фигуру ({i+1}/{length}): ')) == '': break
            elif a.isdigit():
                if int(a) < 1 or int(a) > len(figures): print(f'Номер <{a}> не в допустимом диапазоне <1-{len(figures)}> фигур')
                else:
                    if input(f'Нажмите <Enter>, чтобы подтвердить удаление фигуры <{figures[int(a)-1].replace("figure_", "")}>: ') == '':
                        delete(fr'{figures_folder}\{figures[int(a)-1]}.txt')
                        delete(fr'{hotkeys_figures}\{figures[int(a)-1]}.txt')
                        delete(fr'{values_figures}\{figures[int(a)-1]}')
                        print(f'Фигура <{figures[int(a)-1].replace("figure_", "")}> была удалена')
                        break
                    else: print('Отменено')
            elif not a.isdigit():
                if a in figures or 'figure_' + a in figures:
                    if a[:7] != 'figure_': a = 'figure_' + a
                    if input(f'Нажмите <Enter>, чтобы подтвердить удаление фигуры <{a.replace("figure_", "")}>: ') == '':
                        delete(fr'{figures_folder}\{a}.txt')
                        delete(fr'{hotkeys_figures}\{a}.txt')
                        delete(fr'{values_figures}\{a}')
                        print(f'Фигура <{a.replace("figure_", "")}> была удалена')
                        break
                    else: print('Отменено')
                else: print(f'Фигуры <{a}> нет в списке')
        if a == '': break
    print('\nЗавершение работы программы...')

if __name__ == '__main__':
    IntegrityCheck()
    CleanUp()
    start()
