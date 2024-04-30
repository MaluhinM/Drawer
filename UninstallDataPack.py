print('Запуск программы...')  # Вывод информации в консоль
print('Импорт библиотек: ', end='')  # Вывод информации в консоль
# Импорт библиотек
from keyboard import add_hotkey  # Управление
from tkinter.messagebox import showerror  # Создание окон ошибок
from os import path, mkdir, rename, remove  # Проверка наличия путей, создание папок, переименование файлов и их удаление
from shutil import rmtree  # Удаление папок
import sys  # Взаимодействие интерпретатора языка Python и операционной системы. Используется для мгновенного завершения работы, нахождения пути исполняемого файла и определения места запуска
from glob import glob  # Просмотр файлов
from itertools import zip_longest  # Создание словарей из элементов списков попарно
print('Выполнено')  # Вывод информации в консоль

print('Расчет значений: ', end='')  # Вывод информации в консоль
# Ошибки и их возможные причины
causes: 'Ошибки' = {'Несуществующий путь': 'Отсутствует необходимый для работы программы файл',
                    'Несуществующие пути': 'Отсутствуют необходимые для работы программы файлы',
                    'Неверное значение': 'Программа получила недопустимое значение на вход из определенного файла',
                    'Непредвиденная ошибка': 'В работе программы произошел сбой',
                    'Недопустимое имя файла': 'Имя необходимого файла не соответствует критериям для корректной работы программы'}
causes_keys: 'Оглавления ошибок' = tuple(causes.keys())  # Названия ошибок

if getattr(sys, 'frozen', False):
    loc = path.dirname(sys.executable)
    data_folder: 'data' = loc + '\data'  # Основная папка <data>. В ней содержится большинство данных
    figures_py = loc + r'\figures.py'
elif __file__:
    data_folder: 'data' = 'data'  # Основная папка <data>. В ней содержится большинство данных
    figures_py = 'figures.py'

hotkeys_folder: 'data/hotkeys' = f'{data_folder}\hotkeys'  # Папка <hotkeys>. Хранит клавиши или сочетание клавиш для управления
values_folder: 'data/values' = fr'{data_folder}\values'  # Папка <values>. Хранит значения для управления
figures_folder: 'data/figures' = fr'{data_folder}\figures'  # Папка <figures>. Хранит названия фигур и значения для их использования
datapacks_folder: 'data/DataPacks' = f'{data_folder}\DataPacks'

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
other_keys: tuple = ('exit', 'clear', 'reset_heading', 'pen', 'undo')  # Прочие функции программы
keys: tuple = (base_keys, shift_keys, ctrl_keys, other_keys)  # Переменная для хранения функций

print('Выполнено')  # Вывод информации в консоль

def IntegrityCheck() -> 'Проверка целостности системы':  # Проверка целостности программы
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
    sys.exit()  # Завершение работы программы

def CheckDataPacks():
    if not path.exists(datapacks_folder):
        mkdir(datapacks_folder)
        print(f'\nПапка пакетов данных <{datapacks_folder}> создана')
        sys.exit()
    data = set({file for file in glob(f'{datapacks_folder}\#dp_*.txt')} | {file for file in glob(f'{datapacks_folder}\#datapack_*.txt')})
    if len(data) == 0: print(f'\nПакеты данных не обнаружены по пути <{datapacks_folder}>')
    else:
        print('\nПроверка... ')
        FilesToDiscard = set()
        # for i in data:
        #     try: parse(open(i, 'r', encoding='utf-8').read())
        #     except: FilesToDiscard.add(i)
        # for i in FilesToDiscard: data.discard(i)
        if len(FilesToDiscard) == 0:
            print('Обнаружен пакет данных:', [x.replace(f'{datapacks_folder}\#dp_', '').replace(f'{datapacks_folder}\#datapack_', '').replace('.txt', '') for x in data]) if len(data) == 1 else print(f'Обнаружены пакеты данных ({len(data)}):', [x.replace(f'{datapacks_folder}\#dp_', '').replace(f'{datapacks_folder}\#datapack_', '').replace('.txt', '') for x in data])
        else:
            if len(data) == 0: print('Исправных пакетов данных не обнаружено')
            elif len(data) == 1: print('Обнаружен исправный пакет данных:', [x.replace(f'{datapacks_folder}\#dp_', '').replace(f'{datapacks_folder}\#datapack_', '').replace('.txt', '') for x in data])
            else: print(f'Обнаружены исправные пакеты данных ({len(data)}):', [x.replace(f'{datapacks_folder}\#dp_', '').replace(f'{datapacks_folder}\#datapack_', '').replace('.txt', '') for x in data])
            print(f'Неисправных ({len(FilesToDiscard)}):', [x.replace(f'{datapacks_folder}\#dp_', '').replace(f'{datapacks_folder}\#datapack_', '').replace('.txt', '') for x in FilesToDiscard])

def DeleteDataPack(dp):
    folder = path.dirname(dp) if path.basename(dp)[:4] == '#dp_' or path.basename(dp)[:10] == '#datapack_' else RaiseError(causes_keys[4], f'Имя пакета данных по пути <{dp}>\nне начинается с <#dp_> или <#datapack_>', NeedReinstall=False)
    print('\nУдаляю пакет данных <%s>...' % dp.replace(f'{folder}\#dp_', '').replace(f'{folder}\#datapack_', '').replace('.txt', ''))
    com = dict(zip_longest(*[iter([x.strip() for x in open(dp, 'r', encoding='utf-8').read().split('#') if x not in {''}])] * 2, fillvalue=""))

    info = 'Отсутствует'
    if 'info' in com.keys(): info = com['info']

    if 'code' in com.keys():
        if info == 'Отсутствует':
            ToWrite = open(figures_py, 'r', encoding='utf-8').read().replace(f'\n{com["code"]}\n', '')
            open(figures_py, 'w', encoding='utf-8').write(ToWrite)
        else:
            if '\n' in info:
                ToWrite = open(figures_py, 'r', encoding='utf-8').read().replace(f'\n"""\n{info}\n"""\n{com["code"]}\n', '')
                open(figures_py, 'w', encoding='utf-8').write(ToWrite)
            else:
                ToWrite = open(figures_py, 'r', encoding='utf-8').read().replace(f'\n# {info}\n{com["code"]}\n', '')
                open(figures_py, 'w', encoding='utf-8').write(ToWrite)

    if 'type' in com.keys():
        try:
            if com['type'].split()[0].lower() == 'figure':
                if path.exists('{}\{}.txt'.format(figures_folder, 'figure_' + com['type'].split()[1])): remove('{}\{}.txt'.format(figures_folder, 'figure_' + com['type'].split()[1]))
                if path.exists('{}\{}.txt'.format(hotkeys_figures, 'figure_' + com['type'].split()[1])): remove('{}\{}.txt'.format(hotkeys_figures, 'figure_' + com['type'].split()[1]))
                if path.exists('{}\{}'.format(values_figures, 'figure_' + com['type'].split()[1])): rmtree('{}\{}'.format(values_figures, 'figure_' + com['type'].split()[1]))
        except Exception as error:
            print(f'ВНИМАНИЕ! Произошла ошибка при удалении фигуры: {error=}, {type(error)=}\nВозможная причина: ', end='')
            if type(error) in {IndexError, ValueError, TypeError, NameError, ZeroDivisionError}: print('Неполадка в пакете данных')
            elif type(error) in {WindowsError}: print('Конфликт пакета с текущими данными')
            else: print('Неизвестна')
            input('Нажмите <Enter> для вызова ошибки (остановка программы): ')
            raise

    rename(dp, dp.replace(folder + '\#', folder + '\\'))

    print('Пакет данных <%s> удален' % dp.replace(f'{folder}\#dp_', '').replace(f'{folder}\#datapack_', '').replace('.txt', ''))

def start():
    CheckDataPacks()
    data = [file for file in glob(f'{datapacks_folder}\#dp_*.txt')] + [file for file in glob(f'{datapacks_folder}\#datapack_*.txt')]
    length = len(data)
    for i in range(length):
        while True:
            data = [file for file in glob(f'{datapacks_folder}\#dp_*.txt')] + [file for file in glob(f'{datapacks_folder}\#datapack_*.txt')]
            if len(data) == 0: return
            print('\nДоступные пакеты для удаления:\n' + '\n'.join(['{}. {}'.format(data.index(x)+1, x.replace(f'{datapacks_folder}\#dp_', '').replace(f'{datapacks_folder}\#datapack_', '').replace('.txt', '')) for x in data]))
            if (a := input(f'Удалить пакет ({i+1}/{length}): ')) == '': return
            if a.isdigit():
                if int(a) < 1 or int(a) > len(data): print(f'Номер <{a}> не в допустимом диапазоне <1-{len(data)}> пакетов')
                else:
                    print(f'\nСодержимое пакета <%s>:\n{open(data[int(a) - 1], "r", encoding="utf-8").read()}' % data[int(a) - 1].replace(f'{datapacks_folder}\#dp_', '').replace(f'{datapacks_folder}\#datapack_', '').replace('.txt', ''))
                    if input('Нажмите <Enter>, чтобы подтвердить удаление пакета <%s>: ' % data[int(a) - 1].replace(f'{datapacks_folder}\#dp_', '').replace(f'{datapacks_folder}\#datapack_', '').replace('.txt', '')) == '':
                        DeleteDataPack(data[int(a) - 1])
                        break
                    else: print('Отменено')
            elif not a.isdigit():
                if a in [x.replace(f'{datapacks_folder}\#dp_', '').replace(f'{datapacks_folder}\#datapack_', '').replace('.txt', '') for x in data]:
                    print('\nСодержимое пакета <%s>:\n%s' % (a, open(glob(f'{datapacks_folder}\*{a}.txt')[0], "r", encoding="utf-8").read()))
                    if input(f'Нажмите <Enter>, чтобы подтвердить удаление пакета <{a}>: ') == '':
                        DeleteDataPack(glob(f'{datapacks_folder}\*{a}.txt')[0])
                        break
                    else: print('Отменено')
                else: print(f'Пакета <{a}> нет в списке')

if __name__ == '__main__':
    IntegrityCheck()
    if len(sys.argv) == 1: start()
    else: [DeleteDataPack(x) for x in sys.argv[1:]]
    input('\nНажмите <Enter> для завершения работы программы: ')
    print('Завершение работы программы...')
