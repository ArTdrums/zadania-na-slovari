'''
Создать словарь, в котором в качестве ключа содержится номер студенческого билета (номер билета трехзначный
т.е. от 0 до 999), а в качестве значения содержится строка с именем и фамилией.
Заполняется словарь вводом с клавиатуры, номер билета генерируется случайно, но проверяется чтобы
он не использовался в словаре.
Заполнить словарь 10 элементами

'''

import random  # позключаем модуль рандом

sp = []  # создаем пустой список
s = []  # создаем пустой список
for x in range(10):  # запускаем цикл
    if x not in sp:  # делаем проверку на содержание эл в списке
        sp.append((random.randint(0, 1000)))  # заполняем список случайными элементами
print(sp)  # выводим поулчившийся список

for i in range(10):  # запускем цикл
    s.append(input())  # добавляем в список элементы, введенные пользователем
# print(s)
slovar = dict(zip(sp, s))  # создаем словарь склеинный из двух списков, где элементы первого списка ключи,
# а элементы вротого значения
print(slovar)  # выводим получившийся словрь
