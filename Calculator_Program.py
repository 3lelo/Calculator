from tkinter import *
from tkinter import ttk

def press(num):
    global equ_text
    equ_text += str(num)
    equ_label.set(equ_text)

def equals():
    global equ_text
    try:
        equ_label.set(str(eval(equ_text)))
        equ_text = str(eval(equ_text))
    except ZeroDivisionError:
        equ_label.set("Error, division by 'zero'")
        equ_text = ''
    except SyntaxError:
        equ_label.set("Error, enter numbers please")
        equ_text = ''

def clear():
    global equ_text
    equ_label.set('')
    equ_text = ''

def delete():
    global del_text
    global equ_text
    del_text = equ_text[:-1]
    equ_text = del_text
    equ_label.set(del_text)

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
          foreground=[('active', '#333333')],
          background=[('active', '#727272')])


style.configure('o.TButton',
                font=(35),
                foreground='white',
                background='orange',
                borderwidth=0,
                width=5,
                padding=10)

style.map('o.TButton',
          foreground=[('active', 'orange')],
          background=[('active', 'white')])

del_text = ''
equ_text = ''
equ_label = StringVar()

label = Label(w,textvariable=equ_label,font=('Helvetica'),width=29,height=2)
label.pack()

frame = Frame(w)
frame.config(bg='black')
frame.pack()

b1 = ttk.Button(frame,text=1,style='TButton',command= lambda:press(1))
b1.grid(row=0,column=0)

b2 = ttk.Button(frame,text=2,style='TButton',command= lambda:press(2))
b2.grid(row=0,column=1)

b3 = ttk.Button(frame,text=3,style='TButton',command= lambda:press(3))
b3.grid(row=0,column=2)

b4 = ttk.Button(frame,text=4,style='TButton',command= lambda:press(4))
b4.grid(row=1,column=0)

b5 = ttk.Button(frame,text=5,style='TButton',command= lambda:press(5))
b5.grid(row=1,column=1)

b6 = ttk.Button(frame,text=6,style='TButton',command= lambda:press(6))
b6.grid(row=1,column=2)

b7 = ttk.Button(frame,text=7,style='TButton',command= lambda:press(7))
b7.grid(row=2,column=0)

b8 = ttk.Button(frame,text=8,style='TButton',command= lambda:press(8))
b8.grid(row=2,column=1)

b9 = ttk.Button(frame,text=9,style='TButton',command= lambda:press(9))
b9.grid(row=2,column=2)

b0 = ttk.Button(frame,text=0,style='TButton',command= lambda:press(0))
b0.grid(row=3,column=0)

dot = ttk.Button(frame,text='.',style='TButton',command= lambda:press('.'))
dot.grid(row=3,column=1)

clr = ttk.Button(text='clear',style='TButton',width=13,command= lambda:clear())
clr.pack(side=LEFT)

dlt = ttk.Button(text='delete',style='TButton',width=12,command= lambda:delete())
dlt.pack(side=LEFT)

plus = ttk.Button(frame,text='+',style='o.TButton',command= lambda:press('+'))
plus.grid(row=0,column=3)

minus = ttk.Button(frame,text='-',style='o.TButton',command= lambda:press('-'))
minus.grid(row=1,column=3)

mult = ttk.Button(frame,text='*',style='o.TButton',command= lambda:press('*'))
mult.grid(row=2,column=3)

div = ttk.Button(frame,text='/',style='o.TButton',command= lambda:press('/'))
div.grid(row=3,column=3)

equ = ttk.Button(frame,text='=',style='o.TButton',command=equals)
equ.grid(row=3,column=2)


w.mainloop()