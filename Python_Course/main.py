# print("Input first number: ")
# a = int(input())
# b = int(input("Input second number: "))
# print(a, ' + ', b, ' = ', a+b)


# p = 3.1416
# f = 1.6180
# print(round(p*f, 3))


# a = 'qwerty'
# print(a[4], a[1], a[2], a[3], a[0])

# for i in a:
#     print(i)            #Вертикальная распечатка строки посимвольно


# line = ""
# for i in range(9):
#     line = ""
#     for j in range(3):
#         line += "*"
#     print(line)           #Заполнение строки и распечатка в несколько строк


text = 'Съешь ещё этих мягких французских булочек'
print(len(text))            #len это функция вывода длины строки в символах
print('булочек' in text)    #проверка наличия указанного слова в указанной строке
print(text.lower())         #перевод всей строки в нижний регистр
print(text.upper())         #в верхний
print(text.replace('булочек', 'кексиков')) #замена всех указанных слов в 1м аргументе на другое указанное слово во 2м аргументе
print(text[:])              #вывод всей строки
print(text[:2])             #вывод символов с индексами от 0 до 1вкл
print(text[2:])             #вывод символов с индексами от 2 до конца
print(text[2:9])            #вывод символов с индексами от 2 до 8вкл
print(text[6:-18])          #вывод символов с индексами от 6 до 22вкл (т.к. 40 - 18 = 22, т.е. от последнего индекса уменьшаемся на 18 позиций; длина строки 41, т.е. последний индекс = 40)
print(text[0:len(text):6])  #вывод от 0 до конца с шагом 6
print(text[::6])            #то же стр38
text = text[2:9] + text[-5] + text[:2] #-херня, шинимахерня   -херня, ващехерня, ващехерня
# Forever young, i wanna be forever young, do you really wanna live forever, forever, and ever (Daniil, Daniel, Danila)