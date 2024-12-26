twoDigit = int(input("Введите двузначное число: "))
oneDigit = int(input("Введите однозначное число: "))

tens = twoDigit // 10
units = twoDigit % 10

result = twoDigit + oneDigit

resultTens = result // 10
resultUnits = result % 10

print("Десятки результата:", resultTens)
print("Единицы результата:", resultUnits)
