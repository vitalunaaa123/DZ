start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))

for number in range(start, end + 1):
    print(number, end=' ')
print()  # для переносу рядка