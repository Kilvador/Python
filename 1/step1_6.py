#6 Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который общий результат спортсмена составить не менее b километров.
# Программа должна принимать значения параметров a и b и выводить одно натуральное число — номер дня.

a = int(input('Введите текущую дистанцию (км): '))
b = int(input('Введите желаемую дистанцию (км): '))

days = 1

while a < b:
    a = a + a /10
    days += 1

print(f'Вам понадобится {days} дней!')