print('Задача 5. Наибольшая сумма цифр')

# Вводится N чисел. 
# Среди натуральных чисел, которые были введены, 
# найдите наибольшее по сумме цифр. Выведите на экран это число и сумму его цифр.

count= int(input('Введите количество чисел: '))
summ, max_summ, max_number = (0, )*3
for elem in range(count):
  number = int(input('Введите число: '))
  for elem in range(len(str(number))):
    summ += int(str(number)[elem])
  if summ > max_summ:
    max_summ = summ
    max_number = number
  summ = 0

print('\nЧисло с максимальной сууммой его цифр:', max_number, '\nСумма его цифр составляет:', max_summ)
