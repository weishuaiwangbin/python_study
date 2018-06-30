#grid布局案例
import tkinter

base = tkinter.Tk()

lb1 = tkinter.Label(base,text='账号：').grid(row=0,sticky=tkinter.W)
entry1 = tkinter.Entry(base)
entry1.grid(row=0,column=1,sticky=tkinter.E)

lb2 = tkinter.Label(base,text='密码:')
lb2.grid(row=1,sticky=tkinter.W)
tkinter.Entry(base).grid(row=1,column=1,sticky=tkinter.E)

btn = tkinter.Button(base,text='登录').grid(row=2,column=1,sticky=tkinter.W)

base.mainloop()