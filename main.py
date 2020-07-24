from tkinter import *
import tkinter.messagebox
from tkinter.ttk import Frame, Label, Entry
from ruby_parser import validate
from ruby_lex import test
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

        # entry1 = Entry(frame1,textvariable=expr)
        # entry1.pack(fill=X, padx=5, expand=True)
        self.expr = Text(frame1)
        self.expr.pack(fill=X, padx=5, pady=5)

        frame3 = Frame(self)
        frame3.pack(fill=X)

        btnlex = Button(frame3, text="Analisis Lexico ", width=12, command=self.validate_lex)
        btnlex.pack(side=LEFT, anchor=N, padx=5, pady=5)

        btnsyntax = Button(frame3, text="Analisis Sintactico", width=12, command=self.validate_syntax)
        btnsyntax.pack(side=LEFT, anchor=N, padx=12, pady=5)

        btnclear = Button(frame3, text="Limpiar", width=8, command=self.clear)
        btnclear.pack(side=LEFT, anchor=N, padx=20, pady=5)

        frame4 = Frame(self)
        frame4.pack(fill=X)

        lbl3 = Label(frame4, text="Analisis Lexico :", width=70)
        lbl3.pack(side=LEFT, padx=5, pady=5)
        lbl4 = Label(frame4, text="Analisis Sintactico :", width=20)
        lbl4.pack(side=LEFT, padx=25, pady=5)

        frame5 = Frame(self)
        frame5.pack(fill=X)
        self.tbox = Text(frame5)
        self.tbox.pack(padx=5, pady=5, side=LEFT)
        self.tbox2 = Text(frame5)
        self.tbox2.pack(after=self.tbox,padx=5, pady=10, side=LEFT)

    def errorMsg(self,msg):
        if msg == 'error':
            tkinter.messagebox.showerror('Error!', 'Coloque una expresion')

    def clear(self):
        self.expr.delete('1.0', END)
        self.tbox.delete('1.0', END)
        self.tbox2.delete('1.0', END)

    def validate_syntax(self):
        self.tbox2.delete('1.0', END)
        if len(self.expr.get("1.0", END)) == 1:
            self.errorMsg('error')
        else:
            result = validate(self.expr.get("1.0", END))
            file = open('res_sin', 'r')
            last_line = file.read().splitlines()[-1] + '\n' 
            self.tbox2.insert(END,last_line)

    def validate_lex(self):
        self.tbox.delete('1.0', END)
        if len(self.expr.get("1.0", END)) == 1:
            self.errorMsg('error')
        else:
            result = test(self.expr.get("1.0", END))
            for r in result:
                self.tbox.insert(END, r + '\n')


def main():
    root = Tk()
    root.geometry("1000x800")
    app = App(root)
    root.mainloop()

if __name__ == '__main__':
    main()