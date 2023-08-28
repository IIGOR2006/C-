


s = int(input("введите сумму загаданных чисел = "))
p = int(input("введите прозведение загаданных чисел"))

for i in range(1,1000):
    for j in range(1,1000):
        if i + j == s and i * j == p:
            print(i,j)