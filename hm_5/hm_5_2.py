a = input("Введите первое число: ")
b = input("Введите второе число: ")

_dex = {"1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15, "10": 16}

size_a = len(a)
rank = size_a - 1
a_int = 0


for i in range(size_a):
    a_int += _dex[a[i]] * 16 ** rank
    rank -= 1

size_b = len(b)
rank = size_b - 1
b_int = 0

for i in range(size_b):
    b_int += _dex[b[i]] * 16 ** rank
    rank -= 1

_sum = a_int + b_int
_mult = a_int * b_int

print("Сумма чисел равна: ", hex(_sum))
print("Произведение чисел равно: ", hex(_mult))
