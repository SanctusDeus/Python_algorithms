'''
3. Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите в массиве медиану.
Медианой называется элемент ряда, делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива.
Но если это слишком сложно, то используйте метод сортировки, который не рассматривался на уроках
'''

import random

def median(array):
    if len(array) <= 1:
        print("Нулевое значение")
        return array[0]
    i = 0
    j = 0
    count_left = 0
    count_right = 0
    result = []

    for i in range(len(array)):

        for j in range(len(array)):

            if j != i:
            
                if array[i] < array[j]:
                    count_right += 1
                if array[i] > array[j]:
                    count_left += 1

        result.append(abs(count_right - count_left))

                      
        count_left = 0
        count_right = 0
    
    return result.index(min(result))

        
array = []

n = int(input("Пожалуйста, введите размер массива 2n + 1: "))

for i in range(2 * n + 1):
    array.append(random.randint(1, 100))

print(array)

result = median(array)

print("Индекс медианного значения", result)
print("Медианное значение: ", array[result])
