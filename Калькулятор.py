a = float(input("Введіть перше число (a): "))
b = float(input("Введіть друге число (b): "))
operation = input("Введіть операцію (+, -, *, /): ")

if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b == 0:
        print("Ділення на нуль")
        exit()
    else:
        result = a / b
else:
    print("Невірна операція")
    exit()

print(f"Результат: {result}")