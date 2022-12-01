# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

def Function(a):
    print(a)
    list = []
    for i in a:
        if i in list:
            i+=1
        else:
            list.append(i)
    print(list)
x = list(map(int, input('Введите числа через пробел: ').split()))
Function(x)