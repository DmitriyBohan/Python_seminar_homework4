""" 
Вычислить число c заданной точностью d

Пример:

- при d = 3, π = 3.141 
"""

number = int(input('Задайте точность: '))
pi = 0
for k in range(number):
    pi += (1/16**k) * (4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print(round(pi, number))
