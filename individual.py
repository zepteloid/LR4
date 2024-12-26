import math

a = float(input("First number: "))
b = float(input("First number: "))

mean = (a+b)/2

result = math.sqrt(abs(a) * abs(b))


# Двузначное число
two_digit = 56

# Однозначное число
one_digit = 7

# Извлекаем цифры двузначного числа
tens = two_digit // 10
units = two_digit % 10

# Суммируем числа
result = two_digit + one_digit

# Извлекаем цифры результата
result_tens = result // 10
result_units = result % 10

# Выводим результат
print("Десятки результата:", result_tens)
print("Единицы результата:", result_units)
