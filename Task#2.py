X = int(input("Введите количество чисел\n"))
Number = int(input("Введите число "))
MaxX = Number
TheSecondMaxX = MaxX
for i in range(1, X):
    Number = int(input("Введите число "))
    if Number > MaxX:
        TheSecondMaxX = MaxX
        MaxX = Number
    if Number < MaxX and Number > TheSecondMaxX:
        TheSecondMaxX = Number
print("Первый максимум равен ", MaxX, "Второй максимум равен ", TheSecondMaxX)
