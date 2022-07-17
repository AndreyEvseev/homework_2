# Задание 1. Напишите программу, которая принимает на вход вещественное число и 
# показывает сумму его цифр.

def sum_number(n: float) -> int:
    s=str(n) 
    s=s.replace('.', '')
    s=int(s)
    sum = 0
    while s != 0:
        sum = sum + s%10
        s //= 10
    return sum


n = float(input('Введите вещественное число: '))
sum = sum_number(n)
print(sum)
