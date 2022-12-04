Numbers = int(input("Введите число: "))
flag = 0
LastChar = Numbers % 10
Numbers = int(Numbers / 10)
while Numbers > 0:
    TheSecondLastChar = Numbers % 10
    Numbers = int(Numbers / 10)
    if LastChar >= TheSecondLastChar:
        LastChar = TheSecondLastChar
    else:
        flag += 1
if flag > 0:
    print("Нет")
else:
    print("Да")

