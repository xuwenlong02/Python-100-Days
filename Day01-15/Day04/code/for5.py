"""
输入两个正整数计算最大公约数和最小公倍数

Version: 0.1
Author: 骆昊
Date: 2018-03-01
"""

x = int(input('x = '))
y = int(input('y = '))
a = x
b = y
while a != b:
    if a > b:
        a = a-b
    else:
        b = b - a
print('%d和%d的最大公约数是%d' % (x, y, a))
print('%d和%d的最小公倍数是%d' % (x, y, x * y // a))
