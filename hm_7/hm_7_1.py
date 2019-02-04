import random

'''
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).
'''

def bubble(array):

    lvl = 0

    for i in range(len(array) - 1):
        for j in range(len(array) - 1 - lvl):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
        lvl += 1

array = []

n = int(input("Пожалуйста, введите размер массива: "))

for i in range(n):
    array.append(random.randint(-100, 99))

random.shuffle(array)

print("\nИсходный массив\n" ,array)

bubble(array)

print("Отсортированный массив\n", array)
