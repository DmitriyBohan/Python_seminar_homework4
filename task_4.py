""" 
Задана натуральная степень k. 
Сформировать случайным образом список коэффициентов 
(значения от 0 до 100) многочлена и вывести на экран.

Пример:

- k=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0 
"""

from random import randint

k = int(input('Задайте натуральная степень k: '))
array = []
for i in range(k, 0, -1):
    print(f'{randint(0,100)}x^{i}+', end='')
print(randint(0, 100), end='')
