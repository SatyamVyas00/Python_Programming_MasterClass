import tkinter
# print(tkinter.TkVersion)
# print(tkinter.TclVersion)
#tkinter._test()

#Pack Geomtery Manager
# mainWindow = tkinter.Tk()
# mainWindow.title("Hello World")
# mainWindow.geometry('640x480+8+400')
#
# label = tkinter.Label(mainWindow,text="Hello World")
# label.pack(side='top')
#
# leftFrame = tkinter.Frame(mainWindow)
# leftFrame.pack(side='left',anchor='n',fill=tkinter.Y,expand=False)
#
# canvas = tkinter.Canvas(leftFrame,relief='raised',borderwidth=1)
# canvas.pack(side='left',fill=tkinter.X,expand=True)
# canvas.pack(side='top',fill=tkinter.Y,expand=True)
# canvas.pack(side='left',fill=tkinter.BOTH,expand=True)
# canvas.pack(side='left',anchor='n')
#
# rightFrame = tkinter.Frame(mainWindow)
# rightFrame.pack(side='right',anchor='n',expand=True)
#
# button1 = tkinter.Button(rightFrame,text='Button1')
# button2 = tkinter.Button(rightFrame,text='Button2')
# button3 = tkinter.Button(rightFrame,text='Button3')
# button1.pack(side='top')
# button2.pack(side='top')
# button3.pack(side='top')
#
# mainWindow.mainloop()

#Grid Geomerty Manager
mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry('640x480-8-200')

label = tkinter.Label(mainWindow,text="Hello World")
label.grid(row=0,column=0)

leftFrame = tkinter.Frame(mainWindow)
leftFrame.grid(row=1,column=1)

canvas = tkinter.Canvas(leftFrame,relief='raised',borderwidth=1)
canvas.grid(row=1,column=0)

rightFrame = tkinter.Frame(mainWindow)
rightFrame.grid(row=1,column=2,sticky='n')

button1 = tkinter.Button(rightFrame,text='Button1')
button2 = tkinter.Button(rightFrame,text='Button2')
button3 = tkinter.Button(rightFrame,text='Button3')
button1.grid(row=0,column=0)
button2.grid(row=1,column=0)
button3.grid(row=2,column=0)
#configure the column
mainWindow.columnconfigure(0,weight=1)
mainWindow.columnconfigure(1,weight=1)
mainWindow.grid_columnconfigure(2,weight=1)
leftFrame.config(relief='sunken',borderwidth=1)
rightFrame.config(relief='sunken',borderwidth=1)
leftFrame.grid(sticky='ns')
rightFrame.grid(sticky='new')
rightFrame.columnconfigure(0,weight=1)
button2.grid(sticky='ew')
mainWindow.mainloop()