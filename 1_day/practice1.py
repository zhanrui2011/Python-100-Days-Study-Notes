"""
占位符格式化数据输出字符串

Version: 0.1
Author: 余漪
"""

# a = int(input('a = '))
# b = int(input('b = '))
# print('%d %% %d = %d' % (a, b, a % b))


"""
and or not 的使用

Version: 0.1
Author: 余漪
"""

# flag1 = True and False
# flag2 = True or False
# print('flag1 = ', flag1)
# print('flag2 = ', flag2) 

# print('flag1:false',flag1 is True)
# print('flag1:false',flag1 is not False

"""
输入年份 如果是闰年输出True 否则输出False
> 普通闰年:能被4整除但不能被100整除的年份为普通闰年。（如2004年就是闰年，1900年不是闰年）
> 世纪闰年:能被400整除的为世纪闰年。（如2000年是世纪闰年，1900年不是世纪闰年）


"""

# year = int(input('请输入年份: '))
# is_leap = (year // 4 and year // 100 != 0 or year // 400)
# print(is_leap)


"""
输入月收入和五险一金计算个人所得税

"""

# salary = float(input('本月收入: '))
# insurance = float(input('五险一金: '))
# diff = salary - insurance - 3500
# if diff <= 0:
# 	rate = 0
# 	deduction = 0
# elif diff < 1500:
# 	rate = 0.03
# 	deduction = 0
# elif diff < 4500:
# 	rate = 0.1
# 	deduction = 105
# elif diff < 9000:
# 	rate = 0.2
# 	deduction = 555
# elif diff < 35000:
# 	rate = 0.25
# 	deduction = 1005
# elif diff < 55000:
# 	rate = 0.3
# 	deduction = 2755
# elif diff < 80000:
# 	rate = 0.35
# 	deduction = 5505
# else:
# 	rate = 0.45
# 	deduction = 13505
# tax = abs(diff * rate - deduction)
# print('个人所得税: ￥%.2f元' % tax)
# print('实际到手收入: ￥%.2f元' % (diff + 3500 - tax))



"""
打印乘法口诀表

"""
# for i in range(1,10):
#     for j in range(1, i + 1):
#         print('%d * %d = %d' % (i, j, i * j),  end = '\t')
#     print()


"""
输入一个正整数判断它是不是素数

Date: 2019-04-25 12:30
"""

# from math import sqrt

# num = int(input('请输入一个正整数: '))
# end = int(sqrt(num))  # 平方跟函数 sqrt
# is_prime = True
# for i in range(2, end + 1):
#     if num % i == 0:
#         is_prime = False
# if is_prime and num != 1:
#     print('%d 是素数' % num)
# else:
#     print('%d 不是素数' % num)

"""
输入两个正整数,计算最大公约数和最小公倍数

Date: 2019-4-25 12:50
"""

# x = int(input('x = '))
# y = int(input('y = '))
# if x > y:
#     (x, y) = (y, x)
# for factor in range(x, 0, -1):
#     if x % factor == 0 and y % factor == 0:
#         print('%d 和 %d 的最大公约数是 %d' % (x, y, factor))
#         print('%d 和 %d 的最小公倍数是 %d' % (x, y, x * y // factor))
#         break

"""
打印三角形图案
*
**
***
****
*****

    *
   **
  ***
 ****
*****

    *
   ***
  *****
 *******
*********

Date: 2019-4-25 1: 20
"""

# row = int(input('请输入打印星的行数'))
# for i in range(row):
#     # print('*' * (i + 1), end = '/n') end 默认为'/n'
#     print('*' * (i + 1))

# for i in range(row):
#     print(' ' * (row - i - 1) + '*' * (i + 1))

# for i in range(row):
#     print(' ' * (row - i - 1)  + '*' * (2 * i + 1))

"""
寻找水仙花数
判断规则: 一个三位自幂数(1**3 + 5**3 + 3**3 = 153)
寻找范围: 三位数(100~999)

Date: 2019-4-25 10:10
"""

# for i in range(99, 1000):
#     one = i // 100
#     two = i // 10 % 10
#     three = i % 10
#     if (one**3 + two**3 + three**3 == i):
#         print("水仙数! >>>" + str(i))


"""
寻找完美数
判断规则: 一个恰好等于它自身的真因子(除了自身以外的所有约数)之和
        > 约数: 余为零

Date: 2019-4-25 10:40
"""
# from functools import reduce
# def add(x, y):
    # return x + y
# 
# lists = []
# n = int(input('请输入一个数来判断...(例如:6;28;496;8128;33550336)'))
# for factor in range(1, n-1):
    # if n % factor == 0:
        # lists.append(factor)
# if reduce(add, lists) == n:
    # print("完美数!" + str(n))
# else:
    # print('正常数  -_-`')
    

"""

"""
    

