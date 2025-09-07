try:
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    print("Сумма чисел:", a + b)
except ValueError:
    print("Ошибка: введите числа!")
