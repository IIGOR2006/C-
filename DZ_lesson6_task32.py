
# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума).
# Список можно задавать рандомно

import random

def rand(n):
    random_list = []
    list_2 = []
    for i in range(0, n):
        n = random.randint(1, 100)
        random_list.append(n)
    print(random_list)
    return random_list
    

def res_index(a, b,koko):
    list_rez = []
    for i in range(len(koko)):
        if koko[i] >= a and koko[i] <= b:
            list_rez.append(i)
    return print(list_rez)
    
# rand(n = int(input("введите размер списка = ")))
res_index(int(input("введите начало диапозона = ")),int(input("введите конец диапозона = ")),rand(int(input("введите размер списка = "))))