# Types of data and Variable
# int, float, boolean, str, list, None

a = 123
b = 1.23
print(type(a))
print(type(b))

value = None
print(type(value))
value = 12334
print(type(value))

s = 'hello world'
print(s)            # Вывод строки в терминал
s = '"Fedora" or "Manjaro", that is the question (зэт из зэ квэсчион (vot v chom vopros))'
print(s)
s = 'Look at my big and beautiful laptop, he is very big, like my di...'   # like my distribution of Fedora Linux he-he-he-he
print(a, 'text', b, s)

t = 'bigStan'
print('{} - {} - {}'.format(a, b, t))   #\
                                        # | тоже самое
print(f'{a} - {b} - {t}')               #/

print('{2} - {1} - {0}'.format(a, b, t))            #\
                                                    # | число в фигурных скобках означает индекс задействуемой переменной из круглых скобок после format
print('{2} - {1} - {0} - {2} - {0}'.format(a, b, t))#/

f = True
print(f)
f = False
print(f)

list = [1, 2, 3]    # в Пайтоне отсутствуют массивы, но их заменяют списки
print(list)
list = ['1', '2', '3', 'smotri']
print(list)
list = [1, 2, 3, 'smotri', '4']     # Python - язык с динамической типизацией, то есть мы можем миксовать различные типы в одном списке
print(list)

l = 'love'
b = True
list = ['Nasha', l, 'eto', b]
print(list)

#Ввод и вывод данных
#input, print

#print('Введите a');
#a = input()
#print('Введите b');
#b = input()
print(a, b)
print('{} {}'.format(a, b))
print(f'{a} {b}')

print('Введите a');
a = input()
print('Введите b');
b = input()
print(a, '+', b, '=', a+b) # По умолчанию используется строчный тип, поэтому складываются строки, а не числа

print('Введите a');
a = int(input())    # Для того, чтобы в переменную записалось число, а не строка, нужно перед input указать числовой тип, например int или float
print('Введите b');
b = int(input())
print(a, '+', b, '=', a+b)

print('Введите a');
a = float(input())    # Для того, чтобы в переменную записалось число, а не строка, нужно перед input указать числовой тип, например int или float
print('Введите b');
b = float(input())
print(a, '+', b, '=', a+b)

