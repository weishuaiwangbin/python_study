import tkinter

def baseLabel(event):
    global base
    print("被点击了")
    lb = tkinter.Label(base,text="谢谢点击")
    lb.pack()

base = tkinter.Tk()

lb = tkinter.Label(base,text="模拟按钮")
lb.bind("<Button-1>",baseLabel)
lb.pack()

base.mainloop()