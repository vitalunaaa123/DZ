score = int(input("Введіть кількість балів: "))

if 0 <= score <= 49:
    print("незадовільно")
elif 50 <= score <= 69:
    print("задовільно")
elif 70 <= score <= 89:
    print("добре")
elif 90 <= score <= 100:
    print("відмінно")
else:
    print("Невірний бал (має бути 0-100)")