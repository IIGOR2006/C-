def ar_posl(a1, d, n):
    list_1 = []
    for i in range(n):
        num = (a1 + i * d)
        list_1.append(num)
    return print(list_1)


# ar_posl(7,2,5)
ar_posl(a1 = int(input("введите первый элемент =")),d = int(input("введите разность последовательности =")),n = int(input("введите колличество элементов =" )))

# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.