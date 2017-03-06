# -*- coding: utf-8 -*-

import Tkinter
import tkMessageBox
import random

def generator():

    lucky_set = []
    while len(lucky_set) < int(vnos.get()):
        lottery_num = random.randint(1, 50)
        if lottery_num not in lucky_set:
            lucky_set.append(lottery_num)
            lucky_set.sort()

    tkMessageBox.showinfo("Izbrana števila za današnji žreb so: ", lucky_set)


glavno_okno = Tkinter.Tk()
glavno_okno.title("Generator loterijskih števil")
glavno_okno.configure(background="darkgrey")

loto = Tkinter.Frame(glavno_okno)
loto.configure(background="dark grey")
loto.pack()

oznaka = Tkinter.Label(loto, text="Pozdravljeni v generatorju loterijskih številk,\nvnesite željeno število loterijskih številk.")
oznaka.config(font=("Helvetica", 20), bg="dark grey", fg="white")
oznaka.pack(padx=20, pady=40)

vnosno_polje = Tkinter.Frame(glavno_okno)
vnosno_polje.configure(background="dark grey")
vnosno_polje.pack()

vnos = Tkinter.Entry(vnosno_polje)
vnos.configure(background="dark grey", fg="white")
vnos.pack()

gumb = Tkinter.Button(vnosno_polje, text="Izberi števila", command=generator)
gumb.config(bg="dark grey", fg="white")
gumb.pack(padx= 50, pady=20)






glavno_okno.mainloop()

