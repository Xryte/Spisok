from tkinter import *
from tkinter import ttk, Variable

from pyexpat.errors import messages


from tkinter import *

def add():
    zam.insert(END, entry.get())
    entry.delete(0, END)

def delete():
    select = list(zam.curselection())
    select.reverse()
    for i in select:
        zam.delete(i)

def save():
    f = open('list000.txt', 'w')
    f.writelines('.join(zam.get(0, END))')
    f.close();

def filter():
    fil = sorted(key=str.lower)

root = Tk();
root.title("Список")
root.geometry("250x250")

zam = Listbox(selectmode=EXTENDED);
zam.pack(side=LEFT);
scroll = Scrollbar(command=zam.yview);
scroll.pack(side=LEFT, fill=Y);
zam.config(yscrollcommand=scroll.set);

f = Frame();
f.pack(side=LEFT, padx=10);
entry = Entry(f);
entry.pack(anchor=N);
Button(f, text='Добавить', command=add).pack(fill=X);
Button(f, text='Удалить', command=delete).pack(fill=X);
Button(f, text='Сохранить', command=save).pack(fill=X);
Button(f, text="Фильтр", command=filter).pack(fill=X);

root.mainloop()