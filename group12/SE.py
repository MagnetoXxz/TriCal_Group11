#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   SE.py    
@Contact :   zhu1956318525@163.com
@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2024/4/6 17:23   浛颖      1.0         这段代码实现了自定义的正弦、余弦和正切函数的计算，采用泰勒级数展开的方式进行近似计算。你可以根据需要调整精度和展开项数。
2024/4/13  17:09  唐晨曦    1.0plus    修改了部分函数，添加了反三角函数部分
'''

PI = 3.141592653589793238462643383279502884
def sin_taylor(angle_in_degrees, precision=10**-15):
    """
    :param x: 输入参数为角度值
    :return: 输出为弧度值
    """
    angle_in_radians = angle_in_degrees * PI  / 180  # 将角度转换为弧度
    result = 0
    term = angle_in_radians
    n = 1
    while abs(term) >= precision:
        result += term
        term *= (-1) * angle_in_radians**2 / ((2*n) * (2*n + 1))
        n += 1
    return result



def cos_taylor(angle_in_degrees, precision=10**-15):
    """
    :param x: 输入参数为角度值
    :return: 输出为弧度值
    """
    angle_in_radians = angle_in_degrees * PI / 180  # 将角度转换为弧度
    result = 0
    term = 1
    n = 0
    while abs(term) >= precision:
        result += term
        term *= (-1) * angle_in_radians**2 / ((2*n + 2) * (2*n + 1))
        n += 1
    return result



def tan_taylor(angle_in_degrees):
    """
    :param x: 输入参数为角度值
    :return: 输出为弧度值
    """
    result =  sin_taylor(angle_in_degrees)/cos_taylor(angle_in_degrees);
    return result

def arcsin_taylor(angle_in_radian):
    """
     :param x: 输入参数为弧度值
     :return: 输出为角度值
    """
    if -1 <= angle_in_radian <= 1:  # 判断输入数值是否在定义域内
        result= angle_in_radian
        t = angle_in_radian
        n = 1
        while abs(t) >= 1e-25:  # 采用泰勒级数展开进行计算逼近函数值
            t = t * (2 * n - 1) * (2 * n - 1) * angle_in_radian * angle_in_radian / ((2 * n) * (2 * n + 1))
            n += 1
            result += t
        result = round(result / math.pi * 180, 10)
        return result
    else:
        print(" 请输入[-1 ，1]之间的数:")
        exit(0)

def arccos_taylor(angle_in_radian):
    """
    :param x: 输入参数为弧度值
    :return: 输出为角度值或返回异常
    """
    if -1 <= angle_in_radian<= 1:  # 判断输入数值是否在定义域内
        result = 90 - arcsin_taylor(angle_in_radian)
        return result
    else:
        # 实现异常处理，当输入超出定义域范围，推出
        print(" 请输入[-1 ，1]之间的数:")
        exit(0)


def atan_taylor(x):
    """
    :param x: 输入参数为数值
    :return: 输出为角度值
    """
    if abs(x) < 1:  # 输入值绝对值小于1时，采用泰勒级数展开
        g = x
        # t = x
        n = 1
        while n < 999999:
            t = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
            g += t
            n += 1
    else:  # 输入值绝对值大于1，用 pi/2 - atan(x)
        x = 1 / x
        g = x
        # t = x
        n = 1
        while n < 999999:
            t = ((-1) ** n) * (x ** (2 * n + 1)) / (2 * n + 1)
            g += t
            n += 1
        g = PI / 2 - g

    if x >= 0:
        g = round(g / PI * 180, 10)

    elif x < 0:
        if g >= 0:
            g = round((g - PI) / PI * 180, 10)
        else:
            g = g + pi
            g = round((g - PI) / PI * 180, 10)

    return g




# 测试自定义三角函数计算
# import math
# angle = 0.7


# print(f"sin({angle}) = {sin_taylor(angle)}")
# print("test",math.sin(hu))
# print(f"cos({angle}) = {cos_taylor(angle)}")
# print("test",math.cos(hu))
# print(f"tan({angle}) = {tan_taylor(angle)}")
# # print("test",math.tan(hu))
# # 使用库函数计算作为基准
# reference = math.acos(angle)
# reference=math.acos(angle)/ math.pi* 180
# approximation = acos(angle)
# print("Reference (library function):", reference)
# print("Approximation (Taylor series):", approximation)
# print("Absolute Error:", abs(reference - approximation))