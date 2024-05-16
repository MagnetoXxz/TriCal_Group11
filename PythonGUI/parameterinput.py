from tkinter import *
import tkinter.messagebox
import Interaction
import Interaction_arc

'''第二个界面的数据信息'''
def valueget():
    Interaction.BeginSimulation(setting1, var1_1.get(), angle.get(), radian.get())

def valueget_arc():
    Interaction_arc.BeginSimulation_arc(setting1, inputnum.get())

def confirmcalculate():
    if  setting1 == 1 or setting1 == 2 :
        answer = tkinter.messagebox.askokcancel('确认/取消','数据已经成功保存，请选择确定或者取消！')
        if answer:
            valueget()
            root.destroy()
            Interaction.Show3()

    if setting1 == 3 :

        if float(angle.get()) == 90  or float(angle.get()) == -90 :
            tkinter.messagebox.showwarning('注意!', '输入值范围有误，请重新输入！')
            
        else :
            answer = tkinter.messagebox.askokcancel('确认/取消','数据已经成功保存，请选择确定或者取消！')
            if answer:
                valueget()
                root.destroy()
                Interaction.Show3()

    if setting1 == 4 :
        while float(inputnum.get()) > 1 or float(inputnum.get()) < -1:
            tkinter.messagebox.showwarning('注意!', '计算值需在[-1,1]，请重新输入！')
            break

        while float(inputnum.get()) <= 1 and float(inputnum.get()) >= -1:
            answer = tkinter.messagebox.askokcancel('确认/取消','数据已经成功保存，请选择确定或者取消！')
            if answer:
                valueget_arc()
                root.destroy()
                Interaction_arc.Show4()
            break

    if setting1 == 5:
        answer = tkinter.messagebox.askokcancel('确认/取消', '数据已经成功保存，请选择确定或者取消！')
        if answer:
            valueget_arc()
            root.destroy()
            Interaction_arc.Show4()

    if setting1 == 6:
        while float(inputnum.get()) > 1 or float(inputnum.get()) < -1:
            tkinter.messagebox.showwarning('注意!', '计算值需在[-1,1]，请重新输入！')
            break

        while float(inputnum.get()) <= 1 and float(inputnum.get()) >= -1:
            answer = tkinter.messagebox.askokcancel('确认/取消','数据已经成功保存，请选择确定或者取消！')
            if answer:
                valueget_arc()
                root.destroy()
                Interaction_arc.Show4()
            break


def choicejudge():
    global angle
    global number
    global radian
    choice = var1_1.get()
    if choice == 1:
        angle = Entry(width=50)
        angle.place(relx=0.22, y=100, relheight=0.05, width=200)
        radian = Entry(state='disable')
        print(radian)
        radian.place(relx=0.22, y=180, relheight=0.05, width=200)
    if choice == 2:
        angle = Entry(state='disable')
        angle.place(relx=0.22, y=100, relheight=0.05, width=200)
        radian = Entry(width=50)
        radian.place(relx=0.22, y=180, relheight=0.05, width=200)

def Show2(window2,set1):
    global root
    global setting1
    global var1_1
    global inputnum
    setting1 = set1
    root = window2
    root.title('输入')#标题
    root.geometry('350x350')  # 设置窗口大小
    var1_1 = IntVar()
    '''标题'''
    lb1 = Label(root, text='参数输入', font=('Times', 15), bg='#ADD8E6',relief=SUNKEN,anchor='center')
    lb1.place(relx=0, y=0, relwidth=1, relheight=0.1)

    if setting1 == 1 or  setting1 == 2 or setting1 == 3:
        btn1 = Radiobutton(root, text='角度', bg="#ADD8E6", activebackground='gray', variable=var1_1,
                             value=1, command = choicejudge)
        btn1.place(relx=0.22, y=80, relheight=0.05, width=200)

        btn2 = Radiobutton(root, text='弧度', bg="#ADD8E6", activebackground='gray', variable=var1_1,
                            value=2, command = choicejudge)
        btn2.place(relx=0.22, y=160, relheight=0.05, width=200)

    if setting1 == 4 or setting1 == 5 or setting1 == 6:
        msg = Label(root, text='计算值',bg='#ADD8E6', font=('微软雅黑', 10))
        msg.place(relx=0.22, y=120, relheight=0.05, width=200)
        inputnum = Entry(width=50)
        inputnum.place(relx=0.22, y=140, relheight=0.05, width=200)

    '''设置计算任务按钮'''
    perform = Label(root, text='Calculate', font=('微软雅黑', 10), bg='#ADD8E6')
    perform.place(relx=0.22, y=240, relheight=0.05, width=200)
    performbtn = Button(root, text='计算', activebackground='gray', command=confirmcalculate)
    performbtn.place(relx=0.22, y=260, relheight=0.05, width=200)
    root.mainloop()




