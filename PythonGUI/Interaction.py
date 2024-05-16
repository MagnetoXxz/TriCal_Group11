from tkinter import *
# import Calculate_arctan
# import Arcsin_calc
import tkinter.messagebox
import math
import main
import ctypes


lib1 = ctypes.CDLL(r'.\\PythonGUI.so') # so文件路径

lib1.C_taylor_tan.argtypes=[ctypes.c_double ,ctypes.c_int, ctypes.c_double]
lib1.C_taylor_tan.restype = ctypes.c_double

lib1.C_taylor_cos.argtypes=[ctypes.c_double ,ctypes.c_int, ctypes.c_double]
lib1.C_taylor_cos.restype = ctypes.c_double

lib1.C_taylor_sin.argtypes=[ctypes.c_double ,ctypes.c_int, ctypes.c_double]
lib1.C_taylor_sin.restype = ctypes.c_double

lib1.C_taylor_arcs.argtypes=[ctypes.c_double ,ctypes.c_int]
lib1.C_taylor_arcs.restype = ctypes.c_double

lib1.C_cmp_arcc.argtypes=[ctypes.c_double ,ctypes.c_int, ctypes.c_double,ctypes.c_double]
lib1.C_cmp_arcc.restype = ctypes.c_double

lib1.C_cmp_arct.argtypes=[ctypes.c_double ,ctypes.c_int, ctypes.c_double,ctypes.c_double]
lib1.C_cmp_arct.restype = ctypes.c_double
'''将用户设置下发至交互模块'''

def BeginSimulation(set1, set2_1, set2_2, set2_3):
    global Function,choice1,Angle,Num,Rad
    Function = set1
    choice1 = set2_1
    Angle = set2_2
    Rad = set2_3


def confirm():
    answer = tkinter.messagebox.askokcancel('确认/取消',
                                            '请选择是否重新输入计算')
    if answer:
        root.destroy()
        main.init_functionchoose()
        
n=15
accu = 0.0000001


def Show3():
    global root
    root = Tk()
    root.title('计算信息')  # 标题
    lb = Label(root, text=' 计算结果', \
                        bg='#ADD8E6', \
                       fg='black', \
                        font=('Times', 15), \
                        width=60, \
                        height=1, \
                        relief=SUNKEN)
    lb.pack()
    root.geometry('400x400')
    '''显示选择函数'''
    dic = {1: 'sin',
           2: 'cos',
           3: 'tan',
           4: 'arcsin',
           5: 'arctan',
           6: 'arccos',
           }
    setting1 = dic.get(Function)
    
    if choice1 == 1:
        if Function == 1:
            Xxxx=float(Angle)
            Num = Xxxx/180*math.pi
            sin_result = lib1.C_taylor_sin(float(Num),n,math.pi)
            # sin_result_Rad = arcsin_result[0]
            lb1 = Label(root, text='弧度制：' + setting1 + '(' + str(Num) + ')' + ' = ' + str(sin_result),
                            font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)

        if Function == 2:
            Xxxx=float(Angle)
            Num = Xxxx/180*math.pi
            cos_result = lib1.C_taylor_cos(float(Num),n,math.pi)
            # cos_result_Rad = arcsin_result[0]
            lb1 = Label(root, text='弧度制：' + setting1 + '(' + str(Num) + ')' + ' = ' + str(cos_result),
                        font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)

        if Function == 3:
            Xxxx=float(Angle)
            Num = Xxxx/180*math.pi
            tan_result = lib1.C_taylor_tan(float(Num),n,math.pi)
            # tan_result_Rad = arcsin_result[0]
            lb1 = Label(root, text='弧度制：' + setting1 + '(' + str(Num) + ')' + ' = ' + str(tan_result),
                        font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)
    if choice1 == 2:
        if Function == 1:
                sin_result = lib1.C_taylor_sin(float(Rad),n,math.pi)
                # sin_result_Rad = arcsin_result[0]
                lb1 = Label(root, text='弧度制：' + setting1 + '(' + str(Rad) + ')' + ' = ' + str(sin_result),
                                font=('微软雅黑', 10), bg='LightGrey')
                lb1.place(relx=0, y=50, relheight=0.3, width=400)

        if Function == 2:
                cos_result = lib1.C_taylor_cos(float(Rad),n,math.pi)
                # cos_result_Rad = arcsin_result[0]
                lb1 = Label(root, text='弧度制：' + setting1 + '(' + str(Rad) + ')' + ' = ' + str(cos_result),
                            font=('微软雅黑', 10), bg='LightGrey')
                lb1.place(relx=0, y=50, relheight=0.3, width=400)

        if Function == 3:
                tan_result = lib1.C_taylor_tan(float(Rad),n,math.pi)
                # tan_result_Rad = arcsin_result[0]
                lb1 = Label(root, text='弧度制：' + setting1 + '(' + str(Rad) + ')' + ' = ' + str(tan_result),
                            font=('微软雅黑', 10), bg='LightGrey')
                lb1.place(relx=0, y=50, relheight=0.3, width=400)



       

    '''设置回退任务按钮'''
    performbtn = Button(root, text='确定', activebackground='gray',command = confirm)
    performbtn.place(relx=0.25, y=380, relheight=0.04, width=200)
    root.mainloop()
