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

def BeginSimulation_arc(set1, set2):
    global Function,Num
    Function = set1
    Num = set2

def confirm():
    answer = tkinter.messagebox.askokcancel('确认/取消',
                                            '请选择是否重新输入计算')
    if answer:
        root.destroy()
        main.init_functionchoose()


n=15
accu = 0.0000001

def Show4():
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

    if Function == 4:
            arcsin_result = lib1.C_taylor_arcs(float(Num),n)
            # arcsin_result_Rad = arcsin_result[0]
            lb1 = Label(root, text='弧度制：' + setting1 + '(' + str(Num) + ')' + ' = ' + str(arcsin_result),
                        font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)

    if Function ==5:
            arctan_result = lib1.C_cmp_arct(float(Num),n,accu,math.pi)
            # arctan_result_Rad = arctan_result[0]
            lb1 = Label(root, text='弧度制：' + setting1 + '(' + str(Num) + ')' + ' = ' + str(arctan_result),
                        font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)

    if Function == 6:
            arccos_result = lib1.C_cmp_arcc(float(Num),n,accu,math.pi)
            # arccos_result_Rad = arcsin_result[0]
            lb1 = Label(root, text='弧度制：' + setting1 + '(' + str(Num) + ')' + ' = ' + str(arccos_result),
                        font=('微软雅黑', 10), bg='LightGrey')
            lb1.place(relx=0, y=50, relheight=0.3, width=400)




    '''设置回退任务按钮'''
    performbtn = Button(root, text='确认', activebackground='gray',command = confirm)
    performbtn.place(relx=0.25, y=350, relheight=0.1, width=200)
    root.mainloop()
