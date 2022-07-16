# Задание 1. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

def sum_nubber(n: float) -> int:
    s=str(n) 
    s=s.replace('.', '')
    s=int(s)
    sum = 0
    while s != 0:
        sum = sum + s%10
        s //= 10
    return sum


print('Введите вещественное число: ', end=' ')
n = float(input())
sum = sum_nubber(n)
print(sum)



