import tkinter

prev_func = ''


def value_updation(v):
    val = value.get()
    val = val*10 + v
    if val - int (val) > 0:
        val = float(val)
    else:
        val = int(val)
    value.set(val)


def function(arg):
    global prev_func
    if arg == '/10':
        value.set(float(value.get()))
    if prev_func == '':
        total.set(total.get()+value.get())
        value.set(0)
    if prev_func == '+':
        total.set(total.get()+value.get())
        value.set(0)
    elif prev_func == '-':
        total.set(total.get()-value.get())
        value.set(0)
    elif prev_func == '*':
        total.set(total.get()*value.get())
        value.set(0)
    elif prev_func == '/':
        total.set(total.get()/value.get())
        value.set(0)
    prev_func = arg


def b9():
    value_updation(9)


def b8():
    value_updation(8)


def b7():
    value_updation(7)


def b6():
    value_updation(6)


def b5():
    value_updation(5)


def b4():
    value_updation(4)


def b3():
    value_updation(3)


def b2():
    value_updation(2)


def b1():
    value_updation(1)


def b0():
    value_updation(0)


def b_add():
    function('+')


def b_sub():
    function('-')


def b_multi():
    function('*')


def b_div():
    function('/')


def b_c():
    total.set(0)
    value.set(0)
    prev_func = ''


def b_ce():
    value.set(0)
    prev_func = ''


def b_dot():
    function('/10')


def b_equal():
    global prev_func
    function(prev_func)
    value.set(total.get())
    total.set(0)
    prev_func = ''



mainWindowPadding = 7
mainWindow = tkinter.Tk()
mainWindow.title("Calculator")
mainWindow.geometry('640x485')

total = tkinter.DoubleVar(mainWindow, value=0)
value = tkinter.DoubleVar(mainWindow, value=0)

result = tkinter.Entry(mainWindow, width=40, textvariable=value)
result.grid(row=0, column=0, sticky='ew')

# Keypad Frame
keypad = tkinter.Frame(mainWindow)
keypad.grid(row=1, column=0, sticky='nsew')

# Buttons
C = tkinter.Button(keypad, text="C", height=3, width=8,command=b_c)
CE = tkinter.Button(keypad, text="CE", height=3, width=8,command=b_ce)
C.grid(row=0, column=0, sticky='nw')
CE.grid(row=0, column=3, sticky='nw')

b7 = tkinter.Button(keypad, text="7", height=3, width=8,command=b7)
b8 = tkinter.Button(keypad, text="8", height=3, width=8,command=b8)
b9 = tkinter.Button(keypad, text="9", height=3, width=8,command=b9)
b_add = tkinter.Button(keypad, text="+", height=3, width=8,command=b_add)

b7.grid(row=1, column=0, sticky='nw')
b8.grid(row=1, column=1, sticky='nw')
b9.grid(row=1, column=2, sticky='nw')
b_add.grid(row=1, column=3, sticky='nw')

b4 = tkinter.Button(keypad, text="4", height=3, width=8,command=b4)
b5 = tkinter.Button(keypad, text="5", height=3, width=8,command=b5)
b6 = tkinter.Button(keypad, text="6", height=3, width=8,command=b6)
b_sub = tkinter.Button(keypad, text="-", height=3, width=8,command=b_sub)
b4.grid(row=2, column=0, sticky='nw')
b5.grid(row=2, column=1, sticky='nw')
b6.grid(row=2, column=2, sticky='nw')
b_sub.grid(row=2, column=3, sticky='nw')

b1 = tkinter.Button(keypad, text="1", height=3, width=8,command=b1)
b2 = tkinter.Button(keypad, text="2", height=3, width=8,command=b2)
b3 = tkinter.Button(keypad, text="3", height=3, width=8,command=b3)
b_multi = tkinter.Button(keypad, text="*", height=3, width=8,command=b_multi)
b1.grid(row=3, column=0, sticky='nw',columnspan=1)
b2.grid(row=3, column=1, sticky='nw',columnspan=1)
b3.grid(row=3, column=2, sticky='nw',columnspan=1)
b_multi.grid(row=3, column=3, sticky='nw',columnspan=1)

b0 = tkinter.Button(keypad, text="0", height=3, width=8 ,command=b0)
b_dot = tkinter.Button(keypad, text=".", height=3, width=8, command=b_dot)
b_equal = tkinter.Button(keypad, text="=", height=3, width=8, command=b_equal)
b_div = tkinter.Button(keypad, text="/", height=3, width=8, command=b_div)
b0.grid(row=4, column=0, sticky='nw', columnspan=1)
b_dot.grid(row=4, column=1, sticky='nwe', columnspan=1)
b_equal.grid(row=4, column=2, sticky='nwe', columnspan=1)
b_div.grid(row=4, column=3, sticky='nw', columnspan=1)

mainWindow.update()
mainWindow.minsize(263, 370)
mainWindow.maxsize(263, 370)
mainWindow.mainloop()
