#Программа для расчета объема сферы. Важно разобраться с тем, как работает tkinter

import tkinter
import math
from tkinter import ttk
from tkinter import messagebox

window = tkinter.Tk()
window.geometry('800x300')

#Введем переменную для хранения результата
varRes = tkinter.StringVar()


#Наше приложение будет составлено из нескольких блоков по примеру блочной верстки HTML. В качестве блоков будут выспупать фреймы
#Внутри фреймов создадим гриды. 
labelTop = tkinter.Label(window, text='Программа для вычисления объема сферы', font=('Arial bold', 18))
labelTop.pack()

#Верхний фрейм, внутри которого у нас будут 2 поля для ввода
frameTop = tkinter.Frame(window)
frameTop.pack()

labelEntryTop = tkinter.Label(frameTop, text='Введите радиус: ')
labelEntryTop.grid(row=0, column=0)

entryTop = tkinter.Entry(frameTop, width=25)
entryTop.grid(row=0, column=1)

labelEntryBottom = tkinter.Label(frameTop, text='Результат: ') #Результат будет лейблом т.к. в него ничего вводить не надо 
labelEntryBottom.grid(row=1, column=0)

entryBottom = tkinter.Label(frameTop)
entryBottom.grid(row=1, column=1)

def calcFunc():
    #Выводим объем сферы
    global varRes
    varRes = (4/3 * math.pi * int(entryTop.get()))
    entryBottom.config(text=varRes )

#Кнопка для расчета
button = tkinter.Button(window, text='Вычислить', command=calcFunc, bg='green', fg='white')
button.pack()

#Лейбл, где мы будем выводить сообщение о чтении/записи файлов
labelSaver = tkinter.Label(window)
labelSaver.pack()

#Теперь займемся сохранением данных в файл. Создадим фрейм, внутри него будет кнопка и выпадающее меню
#Плюс внизу мы будем сообщать пользователю, сохранен файл успешно или нет
frameBottom = tkinter.Frame(window)
frameBottom.pack()

def saveData():
    
    global varRes
    try:
        f = open('file_exsamples/sph.' + comboSaver.get(), 'w')
        f.write(repr(varRes))
        #labelSaver.config(text='Сохранение успешно!')
        messagebox.showinfo('Состояние сохранения', 'Сохранение успешно!')
    except:
        #labelSaver.config(text='Сохранения не произошло')
        messagebox.showinfo('Состояние сохранения', 'Файл не сохранен')

#Кнопка сохранения
buttonSaver = tkinter.Button(frameBottom, text='Сохранить', command=saveData)
buttonSaver.grid(row=0, column=0)


#Выпадающий список. По умолчанию значение TXT
comboSaver = ttk.Combobox(frameBottom, values=["HTML", "TXT"]) 
comboSaver.current(1)
comboSaver.grid(row=0, column=1)




window.mainloop()