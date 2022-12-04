X = int(input("Введите Х\n"))
Y = int(input("Введите Y\n"))
sum = 0
if X < Y:
    for i in range(X+1, Y):
        if i % 2 == 0 or i % 3 == 0:
            sum += 1
        print(i, sum)
else:
    for i in range(Y+1, X):
        if i % 2 == 0 or i % 3 == 0:
            sum += 1
print(sum)