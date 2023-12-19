print('Задача 7. Пирамидка 2')

# Напишите программу,
# которая получает на вход количество уровней пирамиды и выводит их на экран, заполняя нечётными числами:

# Пример:
#
#             1
#          3     5
#       7     9     11
#    13    15    17    19
# 21    23    25    27    29

max_count, center = (0, ) * 2
number = 1

height = int(input('Введите количество уровней пирамииды: '))
max_count = (height - 1) * 2 + 1
center = max_count // 2

print()
for row in range(1, height + 1):
  for col in range(1, max_count + 1):
    if col <= (center - row + 1):
      print('\t', end='')
  for col in range((row * 2 + 1) // 2):
    print(number, end='\t\t')
    number += 2
  print()