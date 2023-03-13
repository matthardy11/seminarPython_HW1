# Найдите сумму 3х значного числа
# *** Рассмотрите случай числа с плавающей точкой и не обязательно 3-х значного

number = float(input("Введите число: "))
strNumber = str(number)

result = 0
counter = 0

while counter < len(strNumber):
    if strNumber[counter] == '.':
        counter = counter + 1
    else:
        result = result + int(strNumber[counter])
        counter = counter + 1

print(result)

