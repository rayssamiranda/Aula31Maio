from tkinter import *

janela = Tk()

# Tamanhos dos botões(Button)
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(0, weight=1)
janela.grid_columnconfigure(0, weight=1)
janela.grid_rowconfigure(0, weight=1)

#widgets
bt1 = Button(janela, text='Bt 1', font='Arial 30')
bt2 = Button(janela, text='Bt 1', font='Arial 30')
bt3 = Button(janela, text='Bt 1', font='Arial 30')
bt4 = Button(janela, text='Bt 1', font='Arial 30')
bt5 = Button(janela, text='Bt 1', font='Arial 30')
bt6 = Button(janela, text='Bt 1', font='Arial 30')

#layout
bt1.grid(row=0, column=0, sticky=NSEW)
bt2.grid(row=0, column=1, sticky=NSEW)
bt3.grid(row=0, column=2, sticky=NSEW)
bt4.grid(row=1, column=0, sticky=NSEW)
bt5.grid(row=1, column=1, sticky=NSEW)
bt6.grid(row=1, column=2, sticky=NSEW)

#run
janela.mainloop()