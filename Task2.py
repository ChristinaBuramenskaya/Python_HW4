# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def Factor(n):
    a = []
    b = 2
    while b * b <= n:
        if n % b == 0:
            a.append(b)
            n //= b
        else:
            b += 1
    if n > 1:
        a.append(n)
    return a
print(Factor(int(input())))