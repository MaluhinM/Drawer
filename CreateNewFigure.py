from os import path, mkdir
from glob import glob
from keyboard import add_hotkey


def write(name, key):
    with open(fr'data\figures\{name}.txt', 'w', encoding='utf-8') as f: f.write('1')
    with open(fr'data\hotkeys\figures\{name}.txt', 'w', encoding='utf-8') as f: f.write(key)
    mkdir(fr'data\values\figures\{name.replace("data/figures/", "")}')
    print('\nОсновные файлы для фигуры были созданы.'
          f'\nОстается написать код для нее в файле <figures.py> в виде функции '
          f'и задать необходимые значения в созданной папке <data\\values\\figures\\{name.replace("data/figures/", "")}>')
    input('Enter для завершения работы программы: ')

while True:
    name = input('Название новой фигуры (желательно на английском): ')
    if path.exists(fr'data\figures\{name}.txt') or path.exists(fr'data\figures\figure_{name}.txt'):
        print(f'\nФигура <{name.replace("figure_", "")}> уже существует. Придумайте что-то новое')
        continue
    if name[:7] != 'figure_': name = 'figure_' + name
    break
while True:
    key = input('Клавиша для использования фигуры (возможно сочетание): ')

    try: add_hotkey(key, lambda: print(end=''))
    except:
        print(f'\nКажется, Вы ввели несуществующую клавишу или комбинацию клавиш: <{key}>. Попробуйте еще раз')
        continue

    CannotBeUsed = []
    for file in glob('data\hotkeys\*'):
        for n in glob(f'{file}\*.txt'):
            f = open(n, 'r', encoding='utf-8')
            CannotBeUsed.append(f.read())
    if key in CannotBeUsed:
        print(f'\nКлавиша или сочетание клавиш <{key}> уже используется.'
              f'\nВозможности программы позволяют это сделать, однако ее работа может стать некорректной.'
              f'\nВы хотите продолжить?\n')
        if input('Enter для продолжения: ') == '': break
        continue
    break

write(name, key)
