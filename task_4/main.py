#Keshko 9
n=int(input("Введите число"))
numbers = [x for x in range(1, n + 1) if x % 5 == 0]
print(f"Числа от 1 до {n}, кратные пяти:{numbers} ")