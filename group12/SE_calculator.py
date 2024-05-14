#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   SE_calculator.py
@Contact :   zhu1956318525@163.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/4/6 17:15   浛颖      1.0         None
2024/4/13  17:09  唐晨曦    1.0plus    完成了基本功能
'''

import math
from SE import *

def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error: 除数不能为0"
    return x / y



def main():
    print("欢迎使用计算器！")
    while True:
        print("请选择要进行的操作：")
        print("1. 加法")
        print("2. 减法")
        print("3. 乘法")
        print("4. 除法")
        print("5. 正弦函数")
        print("6. 余弦函数")
        print("7. 正切函数")
        print("8. 反正弦函数")
        print("9. 反余弦函数")
        print("10. 反正切函数")
        print("11. 退出")

        choice = input("请输入选项：")

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("请输入第一个数字："))
            num2 = float(input("请输入第二个数字："))

            if choice == '1':
                result = add(num1, num2)
                print(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(f"{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(f"{num1} / {num2} = {result}")
        elif choice in ['5', '6', '7']:
            angle = float(input("请输入角度（度）："))
            if choice == '5':
                result = sin_taylor(angle)
                print(f"sin({angle}) = {result}")
            elif choice == '6':
                result = cos_taylor(angle)
                print(f"cos({angle}) = {result}")
            elif choice == '7':
                result = tan_taylor(angle)
                print(f"tan({angle}) = {result}")

        elif choice in ['8', '9', '10']:
            angle = float(input("请输入弧度："))
            if choice == '8':
                result = arcsin_taylor(angle)
                print(f"asin({angle}) = {result}")
            elif choice == '9':
                result = arccos_taylor(angle)
                print(f"acos({angle}) = {result}")
            elif choice == '10':
                result = atan_taylor(angle)
                print(f"atan({angle}) = {result}")
        elif choice == '11':
            print("感谢使用计算器！")
            break
        else:
            print("无效选项，请重新输入！")




if __name__ == "__main__":
    main()
