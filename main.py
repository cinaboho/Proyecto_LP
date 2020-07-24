from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry
from ruby_parser import validate
import sys
import os

if os.environ.get('DISPLAY','') == '':
    print('no display found. Using :0.0')
    os.environ.__setitem__('DISPLAY', ':0.0')

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()

    def initUI(self):
        self.parent.title("Validador Lexico y Sintacto de Ruby")
        self.pack(fill=BOTH, expand=True)
        global value
        value = 0
        global expr
        expr = StringVar()
        global res
        res = StringVar()

        frame1 = Frame(self)
        frame1.pack(fill=X)

        lbl1 = Label(frame1, text="Expresion :", width=18)
        lbl1.pack(side=LEFT, padx=5, pady=5)

        entry1 = Entry(frame1,textvariable=expr)
        entry1.pack(fill=X, padx=5, expand=True)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        btnplus = Button(frame3, text="Validar", width=8, command=self.validate)
        btnplus.pack(side=LEFT, anchor=N, padx=5, pady=5)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        lbl3 = Label(frame4, text="Resultado :", width=10)
        lbl3.pack(side=LEFT, padx=5, pady=5)

        result = Entry(frame4,textvariable=res)
        result.pack(fill=X, padx=5, expand=True)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Coloque otra expresion')

    def validate(self):
        if expr.get() == '':
            self.errorMsg('error')
        else:
            result = validate(expr.get())
            file = open('res', 'r')
            last_line = file.read().splitlines()[-1]
            res.set(last_line)


def main():
    root = Tk()
    root.geometry("500x140")
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()