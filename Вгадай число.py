import random

secret_number = random.randint(1, 10)
attempts = 3

print("Спробуйте вгадати число від 1 до 10. У вас 3 спроби.")

for attempt in range(attempts):
    guess = int(input(f"Спроба {attempt + 1}: "))
    
    if guess == secret_number:
        print("Вітаємо! Ви вгадали!")
        break
    elif guess > secret_number:
        print("Менше")
    else:
        print("Більше")
else:
    print(f"Ви програли. Загадане число було {secret_number}.")