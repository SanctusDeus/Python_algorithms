companys = {}

n = int(input("Количество компаний: "))

s = 0
full_profit = 0

for i in range(n):
    name = input(str(i + 1) + "-ая компания: ")
    for j in range(4):
        profit_i = int(input("Прибыль за квартал №" + str(j + 1) + " "))
        full_profit += profit_i
    companys[name] = full_profit
    s += full_profit
    full_profit = 0

    
avrg = s / n

print(companys, s, avrg, sep="\n")
   




print("\nСреднияя прибыль: %.0f \nКомпании с прибылью выше среднего:" % avrg)
for i in companys:
    if companys[i] > avrg:
        print(i)
