import unittest
import math
from SE import *



class TestFunc(unittest.TestCase):         # 测试类

    def test_arcsin(self):                 # 测试arcsin函数
        self.assertEqual(math.degrees(math.asin(0)), arcsin_taylor(0))
        self.assertEqual(math.degrees(math.asin(0.7071)), arcsin_taylor(0.7071))
        self.assertEqual(math.degrees(math.asin(0.8660)), arcsin_taylor(0.8660))
        self.assertEqual(math.degrees(math.asin(1)), arcsin_taylor(1))
        self.assertEqual(math.degrees(math.asin(-1)), arcsin_taylor(-1))
        self.assertEqual(math.degrees(math.asin(-0.8660)), arcsin_taylor(-0.8660))

    def test_arccos(self):                  # 测试arccos函数
        self.assertEqual(math.degrees(math.acos(0)), arccos_taylor(0))
        self.assertEqual(math.degrees(math.acos(0.7071)), arccos_taylor(0.7071))
        self.assertEqual(math.degrees(math.acos(1)), arccos_taylor(1))
        self.assertEqual(math.degrees(math.acos(-0.7071)), arccos_taylor(-0.7071))
        self.assertEqual(math.degrees(math.acos(-1)), arccos_taylor(-1))
        self.assertEqual(math.degrees(math.acos(-0.8660)), arccos_taylor(-0.8660))

    def test_arctan(self):                 # 测试arctan函数
        self.assertEqual(math.degrees(math.atan(0)), atan_taylor(0))
        self.assertEqual(math.degrees(math.atan(0.5773)), atan_taylor(0.5773))
        self.assertEqual(math.degrees(math.atan(1)), atan_taylor(1))
        self.assertEqual(math.degrees(math.atan(1.732)), atan_taylor(1.732))
        self.assertEqual(math.degrees(math.atan(0)),atan_taylor(0))
        self.assertEqual(math.degrees(math.atan(-0.5773)), atan_taylor(-0.5773))
        self.assertEqual(math.degrees(math.atan(-1)), atan_taylor(-1))
        self.assertEqual(math.degrees(math.atan(-1.732)), atan_taylor(-1.732))

    def test_cos(self):                    # 测试cos函数
        self.assertEqual(math.cos(math.radians(30)), cos_taylor(30))
        self.assertEqual(math.cos(math.radians(60)), cos_taylor(60))
        self.assertEqual(math.cos(math.radians(90)),cos_taylor(90))
        self.assertEqual(math.cos(math.radians(120)), cos_taylor(120))
        self.assertEqual(math.cos(math.radians(180)), cos_taylor(180))


    def test_sin(self):                    # 测试sin函数
        self.assertEqual(math.sin(math.radians(30)), sin_taylor(30))
        self.assertEqual(math.sin(math.radians(60)), sin_taylor(60))
        self.assertEqual(math.sin(math.radians(90)), sin_taylor(90))
        self.assertEqual(math.sin(math.radians(120)), sin_taylor(120))
        self.assertEqual(math.sin(math.radians(180)), sin_taylor(180))


    def test_tan(self):                     # 测试tan函数
        self.assertEqual(math.tan(math.radians(30)), tan_taylor(30))
        self.assertEqual(math.tan(math.radians(60)), tan_taylor(60))
        self.assertEqual(math.tan(math.radians(120)), tan_taylor(120))
        self.assertEqual(math.tan(math.radians(180)), tan_taylor(180))


if __name__ == '__main__':
    unittest.main()