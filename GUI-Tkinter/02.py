
import  tkinter


def showLabel():
    global base
    lb2 = tkinter.Label(base,text='蓝色背景',background='blue')
    lb2.pack()
    lb3 = tkinter.Label(base,text='绿色背景',background='green')
    lb3.pack()


base = tkinter.Tk()
base.wm_title("GUI study")

#属性支持background，font，underline
lb1 = tkinter.Label(base,text='Python Label')
lb1.pack()

#Button属性：
#anchor     文字对齐方式
# background（bg）    背景颜色
#foreground（fg）     前景（文字）颜色
#borderwidth（bd）    边框宽带
#cursor               鼠标在按钮上的样式
#command              点击触发的函数
#bitmap               显示的位图
#font                 字体
#width，height        宽，高
#state                按钮状态
#text，image          文字，图片
btn = tkinter.Button(base, text="Show Label", command=showLabel)
btn.pack()

base.mainloop()