try:
    a = float(input("Введите ЧЕТНОЕ число a: "))
    b = float(input("Введите ЧЕТНОЕ число b: "))
    if a % 2 == 0 and b % 2 == 0:
        print("Сумма чисел:", a + b)
    else:
        print("Числа нечетные!")
except ValueError:
    print("Ошибка: введите числа!")
