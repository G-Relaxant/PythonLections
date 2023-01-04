
#help(int)   # help - встроенный помощник-справочник



#  ТИПЫ ДАННЫХ И ПЕРЕМЕННЫЕ

# int, float, boolean, str, list, None

# a = 123
# b = 1.23
# print(type(a))
# print(type(b))

# value = None
# print(type(value))
# value = 12334
# print(type(value))

# s = 'hello world'
# print(s)            # Вывод строки в терминал
# s = '"Fedora" or "Manjaro", that is the question (зэт из зэ квэсчион (vot v chom vopros))'
# print(s)
# s = 'Look at my big and beautiful laptop, he is very big, like my di...'   # like my distribution of Fedora Linux he-he-he-he
# print(a, 'text', b, s)

# t = 'bigStan'
# print('{} - {} - {}'.format(a, b, t))   #\
#                                         # | тоже самое
# print(f'{a} - {b} - {t}')               #/

# print('{2} - {1} - {0}'.format(a, b, t))            #\
#                                                     # | число в фигурных скобках означает индекс задействуемой переменной из круглых скобок после format
# print('{2} - {1} - {0} - {2} - {0}'.format(a, b, t))#/

# f = True
# print(f)
# f = False
# print(f)

# list = [1, 2, 3]    # в Пайтоне отсутствуют массивы, но их заменяют списки
# print(list)
# list = ['1', '2', '3', 'smotri']
# print(list)
# list = [1, 2, 3, 'smotri', '4']     # Python - язык с динамической типизацией, то есть мы можем миксовать различные типы в одном списке
# print(list)

# l = 'love'
# b = True
# list = ['Nasha', l, 'eto', b]
# print(list)



#  ВВОД И ВЫВОД ДАННЫХ

#input, print

# print('Введите a');
# a = input()
# print('Введите b');
# b = input()
# print(a, b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# print('Введите a');
# a = input()
# print('Введите b');
# b = input()
# print(a, '+', b, '=', a+b) # По умолчанию используется строчный тип, поэтому складываются строки, а не числа

# print('Введите a');
# a = int(input())    # Для того, чтобы в переменную записалось число, а не строка, нужно перед input указать числовой тип, например int или float
# print('Введите b');
# b = int(input())
# print(a, '+', b, '=', a+b)

# print('Введите a');
# a = float(input())    # Для того, чтобы в переменную записалось число, а не строка, нужно перед input указать числовой тип, например int или float
# print('Введите b');
# b = float(input())
# print(a, '+', b, '=', a+b)



#  АРИФМЕТИЧЕСКИЕ ОПЕРАЦИИ

# +, -, *, /, %, //, **
# унарные операции
# (), сокращённые операции

# a = 123
# b = 321
# c = -321
# s=a+b-c
# print(s)

# / - деление с вещественным результатом, то есть дробным
# // - деление с сохранением только целой части от результата, дробная часть отбрасывается, но не округляется
# % - деление с сохранением остатка от результата, целая часть отбрасывается
# ** - возведение в степень
# round - округление, например c = round(a * b,3) = 3.9   тройка после запятой означает округлить до 3х знаков после запятой
# a = 1.3
# b = 3
# c = round(a*b,3)
# print(c)

# a = 3
# a = a + 5   #\
#             # |тоже самое, снизу сокращённый вариант
# a += 5      #/

# a = a * 5   #\
#             # |тоже самое, снизу сокращённый вариант
# a *= 5      #/



#  ЛОГИЧЕСКИЕ ОПЕРАЦИИ

# >, >=, <, <=, ==, !=
# not, and, or - не путать с &, |, ^
# is, is not, in, not in
# gen

# a = 1 > 4
# print(a)
# a = 1<4
# print(a)
# a = a
# print(a)
# a == a
# print(a)

# a = 5+2
# b = 10-3
# print(a==b)

# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2
# print(a)

# a = 'string'
# b = 'string'
# c = 'thong'
# print(a == b)
# print(a == c)
# print(a==b==c)

# a = [1,2]
# b = [1,2]
# c = [1,2,3]
# d = [3,2,1]
# print(a == b)
# print(a == c)
# print(a == b == c)
# print(c == d)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 123
# print(func<T<x)
# print(func<T>=x)

# f = 1 > 2 or 4 < 6
# print(f)
# f = [1,2,3,4]
# print(f)
# print(2 in f)
# print(not 2 in f)
# is_odd = f[0] % 2 == 0  #\  f[index]
# print(is_odd)           # | false потому что 1 - число не чётное



#  УПРАВЛЯЮЩИЕ КОНСТРУКЦИИ

# if, if-else, if-elif-else, while, while-else, for-in

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Input name: ')
# if username == 'Masha':
#     print('Ura, eto zhe MASHA!')
# elif username == 'Marina':
#     print('Ya tak zhdala Vas, Marina!')
# elif username == 'Ilnar':
#     print('Ilnar - top)')
# else:
#     print('Privet, ', username)

original = 23
inverted = 0
# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
# print(inverted)

# while original != 0:
#     inverted = inverted * 10 + (original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Pozhaluy')
#     print('hvatit )')
# print(inverted)

# for i in 1,2,3,4,5:
#     print(i**2)

# list = [1,2,3,4,5]
# for i in list:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 5):
#     print(i)

# for i in range(1, 16, 2):
#     print(i)

# for i in 'John Varvatos Artisan':
#     print(i)



#  РАБОТА СО СТРОКАМИ

# text = 'свежие, цитрусовые, фужерные, древесные, сладкие'
# print(text)

# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))
# print(numbers)

# for i in numbers:
#     i *= 2
#     print(i)

# colors = ['red', 'green', 'blue']
# for e in colors:
#     print(e)

# for e in colors:
#     print(e*2)

# colors.append('gray')   # добавить в конец
# print(colors == ['red', 'green', 'blue', 'gray'])
# colors.remove('red')



#  ФУНКЦИИ

def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return

a = 2.3
b = 1
c = 2
print(f(a))
print(f(b))
print(f(c))
print(type(f(a)))
