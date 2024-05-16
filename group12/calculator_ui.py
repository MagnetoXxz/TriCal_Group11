# -*- coding: utf-8 -*-
# Do not edit this file unless you know what you are doing.


import sys

from PyQt5.QtWidgets import (QWidget, QApplication,
                             QLineEdit, QPushButton, QGridLayout, QTextEdit, QSizePolicy)
from PyQt5.QtGui import QRegExpValidator, QFont
from PyQt5.QtCore import Qt, QRegExp
from SE import *


class Calculator(QWidget):
    """
    计算器的基本页面的基本界面, 完成基本的计算
    """

    def __init__(self):
        super(Calculator, self).__init__()
        self.ui()
        self.char_stack = []  # 操作符号的栈
        self.num_stack = []  # 操作数的栈
        self.nums = [chr(i) for i in range(48, 58)]  # 用于判断按钮的值是不是数字
        self.operators = ['sin', 'cos', 'tan', 'arcsin', 'arccos', 'arctan']  # 用于判断按钮的值是不是操作符

        self.empty_flag = True  # 这个flag的含义是来判断计算器是不是第一次启动，在显示屏幕中无数据
        self.after_operator = False  # 看了计算器的计算，比如1+2在输入+后，1海显示在屏幕上，输入了2之后，1就被替换了， 这个flag的作用就是这样的
        self.num_operator = False
        self.operators_way = None
        self.calCompleted = False
        self.num = ""

    def ui(self):
        # 这个函数主要适用于初始化界面
        super(Calculator, self).__init__()
        reg = QRegExp("^$")  # 把键盘禁用了, 仅可以按钮的输入
        validator = QRegExpValidator(reg, self)

        # 这个line_edit就是显示屏....
        self.line_edit = QLineEdit('0', self)
        self.line_edit.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.line_edit.setAlignment(Qt.AlignRight)
        self.line_edit.setValidator(validator)
        self.line_edit.setReadOnly(True)
        #历史记录
        self.history = []
        self.history_capacity = 5

        #  使用girdlayout进行界面布局
        grid = QGridLayout()
        self.setLayout(grid)

        btn_names = [
            'C', 'sin', 'cos', 'tan',
            '7', '8', '9', 'arcsin',
            '4', '5', '6', 'arccos',
            '1', '2', '3', 'arctan',
            '0', '-', '.', '='
        ]

        grid.addWidget(self.line_edit, 0, 0, 1, 4)
        positions = [(i, j) for i in range(1, 6) for j in range(4)]
        self.buttons = []
        style = """
            QPushButton {
                background-color: #f0f0f0;
                border: 1px solid #dcdcdc;
                border-radius: 5px;
                padding: 5px;
            }
            QPushButton:hover {
                background-color: #e0e0e0;
            }
        """
        self.setStyleSheet(style)

        # 设置文本框的字体大小
        self.line_edit.setFont(QFont("Arial", 18))

        # 创建一个文本区域用于显示历史记录
        self.history_text = QTextEdit(self)
        self.history_text.setReadOnly(True)  # 设置为只读
        self.history_text.setMaximumHeight(80)  # 设置最大高度
        grid.addWidget(self.history_text, 7, 0, 1, 4)  # 添加到布局中
        # 由于我们设置了统一的样式，可以简化addWidget的循环
        for pos, name in zip(positions, btn_names):
            if name == '':
                continue
            btn = QPushButton(name)
            btn.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
            btn.clicked.connect(self.show_msg)
            self.buttons.append(btn)
            grid.addWidget(btn, *pos)
        self.numEnabled(False)
        self.setFocusPolicy(Qt.StrongFocus)
        self.setWindowTitle('Calculator')
        self.setGeometry(300, 150, 600, 700)  # Set initial size and position
        self.show()

    def raiseError(self):
        self.line_edit.setText('Error')
        for button in self.buttons:
            button.setEnabled(False)
        self.buttons[0].setEnabled(True)

    def numEnabled(self, enabled: bool):
        self.buttons[4].setEnabled(enabled)
        self.buttons[5].setEnabled(enabled)
        self.buttons[6].setEnabled(enabled)
        self.buttons[8].setEnabled(enabled)
        self.buttons[9].setEnabled(enabled)
        self.buttons[10].setEnabled(enabled)
        self.buttons[12].setEnabled(enabled)
        self.buttons[13].setEnabled(enabled)
        self.buttons[14].setEnabled(enabled)
        self.buttons[16].setEnabled(enabled)
        self.buttons[17].setEnabled(enabled)

    def resizeEvent(self, event):
        # Adjust font size based on the widget size
        self.adjust_font_size()
        super().resizeEvent(event)

    def adjust_font_size(self):
        width = self.width()
        height = self.height()

        # Calculate a font size based on the window size
        font_size = max(min(width // 15, height // 15), 10)

        font = self.line_edit.font()
        font.setPointSize(font_size)
        self.line_edit.setFont(font)

        for btn in self.buttons:
            btn.setFont(font)

    def clear_line_edit(self):
        for button in self.buttons:
            button.setEnabled(True)
        self.line_edit.clear()
        self.line_edit.setText('0')
        self.res = 0
        self.num = ""
        # 清空，就相当于刚打开计算器一样
        self.empty_flag = True
        self.numEnabled(False)
        self.after_operator = False
        self.num_operator = False
        self.operators_way = None

    def deal_negative_btn(self):
        if self.operators_way and not self.num_operator:
            self.num += '-'
            self.line_edit.setText(self.operators_way + '(' + self.num + ')')
            self.num_operator = True

    def deal_num_btn(self, sender_text):
        _str = self.line_edit.text()
        if _str == '0' or self.empty_flag:
            self.line_edit.clear()
            self.raiseError()
        elif self.after_operator:
            _num = self.num
            self.num += sender_text
            if self.operators_way in ["arcsin", "arccos"]:
                if float(self.num) < -1 or float(self.num) > 1:
                    self.num = _num
                else:
                    self.num_operator = True
            else:
                self.num_operator = True
            if self.operators_way in ["sin", "cos", "tan"]:
                self.line_edit.setText(self.operators_way + '(' + self.num + '°' + ')')
            else:
                self.line_edit.setText(self.operators_way + '(' + self.num + ')')
        else:
            self.raiseError()
            self.empty_flag = True
            self.num_operator = False

    def deal_operator_btn(self, sender_text):
        # 操作符号
        if self.empty_flag and not self.after_operator:
            self.line_edit.clear()
            self.line_edit.setText(sender_text)
            self.after_operator = True
            self.operators_way = sender_text
            self.empty_flag = False
            self.numEnabled(True)
        elif not self.empty_flag and self.after_operator and not self.num_operator:
            self.line_edit.clear()
            self.line_edit.setText(sender_text)
            self.operators_way = sender_text
        else:
            self.raiseError()
            self.after_operator = False

    def deal_point_btn(self):
        if self.after_operator and not self.num_operator:
            self.raiseError()
        elif self.after_operator and self.num != '-':
            # 计算line_edit中有多少小数点
            point_count = self.line_edit.text().count('.')
            if point_count == 0:
                self.num += "."
            if self.operators_way in ["sin", "cos", "tan"]:
                self.line_edit.setText(self.operators_way + '(' + self.num + '°' + ')')
            else:
                self.line_edit.setText(self.operators_way + '(' + self.num + ')')
        else:
            self.raiseError()

    def deal_equal_btn(self):
        _str = self.line_edit.text()
        if self.after_operator and self.num_operator:
            result = self.compute()
            if self.operators_way in ["arcsin", "arccos", "arctan"]:
                self.line_edit.setText(f"{result:.2f}" + '°')
            else:
                if type(result) == str:
                    self.line_edit.setText(result)
                else:
                    self.line_edit.setText(f"{result:.2f}")
            _str = self.line_edit.text()
            self.clear_line_edit()
            self.line_edit.setText(_str)

    def compute(self):
        try:
            result = None
            if 'sin' == self.operators_way:
                result = sin_taylor(float(self.num))
            if 'cos' == self.operators_way:
                result = cos_taylor(float(self.num))
            if 'tan' == self.operators_way:
                if (float(self.num) + 90) % 180 == 0:
                    result = "inf"
                else:
                    result = tan_taylor(float(self.num))
            if 'arcsin' == self.operators_way:
                if float(self.num) == -1:
                    result = -90
                elif float(self.num) == 1:
                    result = 90
                else:
                    if -1 < float(self.num) < -0.99999:
                        c_9 = arcsin_taylor(-0.99999)
                        result = -90 + (float(self.num) - (-1)) * (c_9 - (-90)) / (-0.99999 - (-1))
                    elif 0.99999 < float(self.num) < 1:
                        c9 = arcsin_taylor(0.99999)
                        result = c9 + (float(self.num) - 0.99999) * (90 - c9) / (1 - 0.99999)
                    else:
                        result = arcsin_taylor(float(self.num))
            if 'arccos' == self.operators_way:
                if float(self.num) == -1:
                    result = 180
                elif float(self.num) == 1:
                    result = 0
                else:
                    if -1 < float(self.num) < -0.99999:
                        c_9 = arccos_taylor(-0.99999)
                        result = 180 + (float(self.num) - (-1)) * (c_9 - 180) / (-0.99999 - (-1))
                    elif 0.99999 < float(self.num) < 1:
                        c9 = arccos_taylor(0.99999)
                        result = c9 + (float(self.num) - 0.99999) * (0 - c9) / (1 - 0.99999)
                    else:
                        result = arccos_taylor(float(self.num))
            if 'arctan' == self.operators_way:
                result = atan_taylor(float(self.num))
            else:
                self.raiseError()
            self.add_to_history(self.operators_way, result)
        except ValueError as e:
            # 处理值错误，例如字符串到数字的转换失败
            self.handle_error("输入的值无效。")
        except OverflowError as e:
            # 处理数值溢出错误
            self.handle_error("数值太大，无法计算。")
        except Exception as e:
            # 处理其他类型的异常
            self.handle_error(str(e))
        return result
    
    def add_to_history(self, operation, result):
        # 将操作和结果格式化为字符串
        history_entry = f"{operation} = {result}"

        # 如果历史记录达到容量上限，则移除最早的记录
        if len(self.history) >= self.history_capacity:
            self.history.pop(0)

        # 将新记录添加到历史记录列表的末尾
        self.history.append(history_entry)

        # 更新历史显示
        self.update_history_display()
    def update_history_display(self):
        # 更新历史显示
        self.history_text.setPlainText("\n".join(self.history))

    def handle_error(self, message):
        # 显示错误信息
        self.line_edit.setText("Error")
        self.numEnabled(False)  # 禁用数字按钮
        self.raiseError()  # 可能需要根据实际情况调整或添加这个方法

    def show_msg(self):
        # 看ui函数，每个按钮都连接了show_msg的点击事件
        sender = self.sender()
        sender_text = sender.text()

        if sender_text == 'C':
            self.clear_line_edit()
        elif sender_text in self.nums:
            self.deal_num_btn(sender_text)
        elif sender_text == '.':
            self.deal_point_btn()
        elif sender_text in self.operators:
            self.deal_operator_btn(sender_text)
        elif sender_text == '=':
            self.deal_equal_btn()
        elif sender_text == '-':
            self.deal_negative_btn()
        else:
            self.raiseError()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    cal = Calculator()
    sys.exit(app.exec_())
