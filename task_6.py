print('Задача 6. Пирамидка')

# Напишите программу,
# которая выводит на экран равнобедренный треугольник (пирамидку),
# заполненный символами хэштега "#". Пусть высота пирамиды вводится пользователем.

# Подсказка: вспомните, как выводился колонтитул вида -----!!!!!!-----

#
###
#####
#######

max_count_simbols, center = (0, ) * 2

height = int(input('Введите высоту пирамиды: '))
max_count_simbols = (height - 1) * 2 + 1
center = max_count_simbols // 2

print()
for row in range(1, height + 1):
  for col in range(1, max_count_simbols + 1):
    if col <= (center - row + 1):
      print(' ', end='')
  print('#' * (row * 2 - 1), end='')
  print()