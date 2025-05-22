n = int(input("Введіть число n: "))
for number in range(n, 0, -1):
    if number % 2 == 0:
        print(number, end=' ')
print()  # для переносу рядка