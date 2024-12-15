from tkinter import *
from tkinter import ttk

def buttons(text : any , style : str , command : any):
    return ttk.Button(frame,text=text,style=style,command= command)


def press(num):
    global equ_text
    equ_text += str(num)
    equ_label.set(equ_text)

def equals():
    global equ_text
    try:
        equ_text = str(f"{eval(equ_text):.6f}") if (float(eval(equ_text)) - int(eval(equ_text))) != 0 else str(f"{eval(equ_text):.0f}")
        equ_label.set(equ_text)
    except ZeroDivisionError:
        equ_label.set("Error, division by 'zero'")
        equ_text = ''
    except SyntaxError:
        equ_label.set("Error, enter numbers please")
        equ_text = ''

def clear():
    global equ_text
    equ_text = ''
    equ_label.set(equ_text)

def delete():
    global equ_text
    equ_text = equ_text[:-1]
    equ_label.set(equ_text)

w = Tk()
w.title('Calculator')
w.configure(bg='black')
w.resizable(False, False)

style = ttk.Style()
style.theme_use('clam')

style.configure('TButton',
                font=(35),
                foreground='white',
                background='#333333',
                borderwidth=0,
                width=5,
                padding=10)

style.map('TButton',
          foreground=[('active', 'white')],
          background=[('active', '#727272')])


style.configure('o.TButton',
                font=(35),
                foreground='white',
                background='orange',
                borderwidth=0,
                width=5,
                padding=10)

style.map('o.TButton',
          foreground=[('active', 'white')],
          background=[('active', '#FCCB80')])

equ_text = ''
equ_label = StringVar()

label = Label(w,textvariable=equ_label,font=('Helvetica'),width=29,height=2,bg='black',fg='white')
label.pack()

frame = Frame(w)
frame.config(bg='black')
frame.pack()

b1 = buttons(1,'TButton',lambda:press(1))
b1.grid(row=2,column=0)

b2 = buttons(2,'TButton',lambda:press(2))
b2.grid(row=2,column=1)

b3 = buttons(3,'TButton',lambda:press(3))
b3.grid(row=2,column=2)

b4 = buttons(4,'TButton',lambda:press(4))
b4.grid(row=1,column=0)

b5 = buttons(5,'TButton',lambda:press(5))
b5.grid(row=1,column=1)

b6 = buttons(6,'TButton',lambda:press(6))
b6.grid(row=1,column=2)

b7 = buttons(7,'TButton',lambda:press(7))
b7.grid(row=0,column=0)

b8 = buttons(8,'TButton',lambda:press(8))
b8.grid(row=0,column=1)

b9 = buttons(9,'TButton',lambda:press(9))
b9.grid(row=0,column=2)

b0 = buttons(0,'TButton',lambda:press(0))
b0.grid(row=3,column=1)

dot = buttons('.','TButton',lambda:press('.'))
dot.grid(row=3,column=0)

clr = ttk.Button(text='Clear',style='TButton',width=13,command= clear)
clr.pack(side=LEFT)

dlt = ttk.Button(text='Delete',style='TButton',width=12,command= delete)
dlt.pack(side=LEFT)

plus = buttons('+','o.TButton',lambda:press(' + '))
plus.grid(row=0,column=3)

minus = buttons('-','o.TButton',lambda:press(' - '))
minus.grid(row=1,column=3)

mult = buttons('x','o.TButton',lambda:press(' * '))
mult.grid(row=2,column=3)

div = buttons('÷','o.TButton',lambda:press(' / '))
div.grid(row=3,column=3)

equ = buttons('=','o.TButton',equals)
equ.grid(row=3,column=2)

w.mainloop()