# """
# Открытие файла
# """
# from tkinter import Tk  # Для предотвращения использования полного GUI (Графического интерфейса пользователя)
# from tkinter.filedialog import askopenfilename  # Для создания диалогового окна для открытия файла
# Tk().withdraw()  # Для предотвращения использования полного GUI не позволяем появиться root окну (НЕОБЯЗАТЕЛЬНО)
# filename = askopenfilename(title='Выбрать файл', initialdir='/', filetypes=(("Любой", "*"),))  # Показ диалогового окна для открытия файла и возврат пути до выбранного файла
# print(filename)  # Вывод пути


# """
# Случайный цвет в HEX
# """
# from string import digits
# from random import choices
#
#
# hex_letters = 'abcdef'
#
# print('#' + ''.join(choices(hex_letters + digits, k = 6)))
# """
# Случайный цвет в HEX с визуализацией
# """
# from string import digits
# from random import choices
# from tkinter import Tk, mainloop
#
# hex_letters = 'abcdef'
#
#
# def switch_color():
#     color = '#' + ''.join(choices(hex_letters + digits, k=6))
#     win.title(color)
#     win['bg'] = color
#     win.after(10, switch_color)
#
#
# win = Tk()
# win.geometry('300x300')
# switch_color()
# mainloop()
