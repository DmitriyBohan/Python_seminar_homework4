""" 
Задайте последовательность чисел. 
Напишите программу, которая выведет список неповторяющихся элементов 
исходной последовательности. 
"""


list_1 = [10, 15, 20, 30, 15, -10, 50]
dict = {}
for i in list_1:
    if i not in dict:
        dict[i] = 1
    else:
        dict[i] += 1
array = []
for i in dict:
    if dict[i] == 1:
        array.append(i)
print(*array)
