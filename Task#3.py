Salary = int(input("Введите сумму: "))
OneRub = int()
TwFiveRub = int()
TenRub = int()
ThreeRub = int()
if Salary / 25 > 1:
    TwFiveRub = int(Salary / 25)
    Salary %=  25
if Salary / 10 > 1:
    TenRub = int(Salary / 10)
    Salary %= 10
if Salary / 3 > 1:
    ThreeRub = int(Salary / 3)
    Salary %= 3
OneRub = Salary
print("25 рублевых -", TwFiveRub, "  10 рублевых -", TenRub, "  3 рублевых -", ThreeRub, "  1 рублевых -", OneRub)
SumBanknotes = TwFiveRub + TenRub + ThreeRub + OneRub
print("Минимальное количество купюр равно ", SumBanknotes)
