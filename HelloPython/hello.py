
# help(int)   # help - встроенный помощник-справочник
# print(dir(tuple)) - показать доступные методы объекта(в данном случае кортежа(tuple))
# print(dir(list)) - показать доступные методы объекта для списка

# Быстрое коментирование строк: 1) Ctrl + /   2) Ctrl + K + C - закоментить,   Ctrl + K + U - раскоментить

# Чтобы запустить консоль питона (интерпретатор) в терминале, нужно в терминале ввести команду "python3"
# В интерпретаторе можно просматривать подсказки по методам и другое без команды печати в коде, например просто вввести запрос dir(set) или dir(list)

#___________________________________________________________________________________________________________________________________________________________________

#  ТИПЫ ДАННЫХ И ПЕРЕМЕННЫЕ

# int, float, boolean, str, list, tuple, dict, None

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

# list1 = [1, 2, 3]                    # в Пайтоне отсутствуют массивы, но их заменяют СПИСКИ, оформляются квадратными скобками
# print(list1)
# list1 = ['1', '2', '3', 'smotri']
# print(list1)
# list1 = [1, 2, 3, 'smotri', '4']     # Python - язык с динамической типизацией, то есть мы можем миксовать различные типы в одном списке, и python сам определяет какой тип использовать для данной переменной (что влияет на производительность, поэтому япы со статической типизацией производительнее и более предпочтительны, но это не точно)
# print(list1)

# l = 'love'
# b = True
# list1 = ['Nasha', l, 'eto', b]
# print(list1)

# tupl1 = 1,2,3                # КОРТЕЖ не позволяет изменять(перезаписывать элементы(ячейки))
# tupl2 = (1,2,3)             # КОРТЕЖ также можно записать в круглых скобках, разницы нет
# внутри КОРТЕЖА может быть СПИСОК, а список можно изменять(перезаписывать), но тогда это будет являться ВЛОЖЕННОЙ СТРУКТУРОЙ

# dict1 = {1:"12", "2":12221, 767:9909, example:111}     # СЛОВАРИ оформляются фигурными скобками, а содержимое ячейки представляет собой пару ключ:значение
# запрос к словарю выполняется не по индексу, а по ключу, с соблюдением типа ключа, например: print(dict1["2"]) или print(dict1[example])
# for el in dict1:
#     print(el)



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
# print(a, '+', b, '=', a+b)    # По умолчанию используется строчный тип, поэтому складываются строки, а не числа

# print('Введите a');
# a = int(input())              # Для того, чтобы в переменную записалось число, а не строка, нужно перед input указать числовой тип, например int или float
# print('Введите b');
# b = int(input())
# print(a, '+', b, '=', a+b)

# print('Введите a');
# a = float(input())            # Для того, чтобы в переменную записалось число, а не строка, нужно перед input указать числовой тип, например int или float
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

# count1 = man1 // 2 if man1 % 2 == 0 else man1 // 2 + 1  #\
# count2 = man1 // 2 if man1 % 2 == 0 else man1 // 2 + 1  # | ТЕРНАРНЫЙ ОПЕРАТОР - запись ветвления if-else в одну строку, если код каждой ветки занимает не более 1 строки
# count3 = man1 // 2 if man1 % 2 == 0 else man1 // 2 + 1  #/

# year = int(input('Введите год: '))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:    # Если есть несколько условий, то приоритет будет у and, затем or.
#     print('YES')                                            # Можно менять приоритетность выделяя скобками более приоритетное условие, например if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
# else:
#     print('NO')

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

# idx = 0
# while idx <= 9:
#     idx += 1
#     if idx == 7:
#         break       #оператор Break останавливает цикл
#     if idx == 2:
#         continue    #оператор Continue останавливает(пропускает) текущий виток
#     print(idx)

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

# for idx in range(3, 10, 2):
#     print(idx)

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
