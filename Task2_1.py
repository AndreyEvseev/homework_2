# Задание 1. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

from re import S


def sum_nubber(n: float) -> int:
    s=str(n) 
    s=s.replace('.', '')
    s=int(s)
    print(s)
    sum = 0
    while s != 0:
        sum = sum + s%10
        print(s)
    print(sum)
    return


print('Введите вещественное число: ', end=' ')
n = float(input())
sum_nubber(n)
#print(n)



