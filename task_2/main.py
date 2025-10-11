numstr = input("Введите числа через пробел: ") #ввод чисел
nums = [int(x) for x in numstr.split()] #генератор списка
sqrnum = [x**2 for x in nums] #генератор списка
print("Введенные числа в квадрате: ", sqrnum) #вывод