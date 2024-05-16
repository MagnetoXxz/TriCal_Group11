from tkinter import *
import tkinter.messagebox
import parameterinput

def init_functionchoose():
    root = Tk()
    root.title("三角函数计算")
    lb = Label(root, text="函数选择", bg="#ADD8E6", fg="black", font=("Times", 25), width=60, height=1, relief=SUNKEN)
    lb.pack()
    root.geometry("350x350")  # 设置窗口大小

    var = IntVar()  # 选择项

    btn1 = Radiobutton(root, text="sin(正弦)", bg="#ADD8E6", activebackground="gray", variable=var, value=1)
    btn1.place(relx=0.22, y=80, relheight=0.05, width=200)

    btn2 = Radiobutton(root, text='cos(余弦)', bg="#ADD8E6", activebackground='gray', variable=var,
                       value=2)
    btn2.place(relx=0.22, y=120, relheight=0.05, width=200)

    btn3 = Radiobutton(root, text='tan(正切)', bg="#ADD8E6", activebackground='gray', variable=var,
                       value=3)
    btn3.place(relx=0.22, y=160, relheight=0.05, width=200)

    btn4 = Radiobutton(root, text='arcsin(反正弦)', bg="#ADD8E6", activebackground='gray', variable=var,
                       value=4)
    btn4.place(relx=0.22, y=200, relheight=0.05, width=200)

    btn5 = Radiobutton(root, text='arctan(反正切)', bg="#ADD8E6", activebackground='gray', variable=var,
                       value=5)
    btn5.place(relx=0.22, y=240, relheight=0.05, width=200)

    btn6 = Radiobutton(root, text='arccos(反余弦)', bg="#ADD8E6", activebackground='gray', variable=var,
                       value=6)
    btn6.place(relx=0.22, y=280, relheight=0.05, width=200)

    def confirm():
        dic = {1: 'sin(正弦)',
               2: 'cos(余弦)',
               3: 'tan(正切)',
               4: 'arcsin(反正弦)',
               5: 'arctan(反正切)',
               6: 'arccos(反余弦)',
               }
        setting1 = dic.get(var.get())
        answer = tkinter.messagebox.askokcancel('确定/取消',
                                                '你的选择是 ' + setting1 + ',''请选择确定/取消.')
        if answer:
            if var.get() == 1 or var.get() == 2 or \
                    var.get() == 3 or var.get() == 4 or var.get() == 5 or var.get() == 6:
                root.destroy()
                window2 = Tk()
                parameterinput.Show2(window2, var.get())

    btn8 = Button(root, text='确认', activebackground='gray', command=confirm)
    btn8.place(relx=0.22, y=310, relheight=0.05, width=200)

    root.mainloop()

if __name__ == "__main__":
    init_functionchoose()





