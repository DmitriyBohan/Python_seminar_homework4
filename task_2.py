""" 
Задайте натуральное число N. 
Напишите программу, которая составит список простых делителей числа N. 
(1 - составное число) 
"""

number = int(input())
for i in range(2, number+1):
    if number % i == 0:
        count = 0
        for j in range(1, i+1):
            if i % j == 0:
                count += 1
                if count > 2:
                    break
        if count == 2:
            print(i, end=' ')
