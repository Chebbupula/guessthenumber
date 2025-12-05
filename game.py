import time
import random
print("Приветствую в игре угадай число")
print("Выбери сложность")
print("1.Легкий 1-10")
print("2.Средний 1-50")
print("3.Сложность 1-100")
choice = input("Выбери (1/2/3): ")

# Инициализируем переменные по умолчанию на случай некорректного ввода
lower_bound = 1
upper_bound = 100 # Максимальный диапазон
secret_number = 0
att = 0

if choice == '1':
    print("Вы выбрали сложность: легкое")
    upper_bound = 10
elif choice == '2':
    print("Вы выбрали сложность: среднее")
    upper_bound = 50
elif choice == '3':
    print("Вы выбрали сложность: сложное")
    upper_bound = 100
else:
    print("Неверный выбор. Установлена максимальная сложность по умолчанию.")
    # Код продолжит работу с upper_bound = 100

print("Подождите пока программа придумает число")
time.sleep(2)

# Определяем загаданное число один раз после выбора диапазона
secret_number = random.randint(lower_bound, upper_bound)
print(f"Наша программа придумала число в диапазоне от {lower_bound} до {upper_bound}")

while True:
    y_str = input("Введите ваше число: ")

    try:
        y = int(y_str)
        att += 1

        if y > secret_number:
            print("Меньше")
        elif y < secret_number:
            print("Больше")
        else:
            print(f"Победа! Загаданное число {secret_number} Попыток: {att}")
            break 
    except ValueError:
        print("Неверный ввод. Пожалуйста, введите целое число.")
        continue # Продолжаем цикл, не засчитывая ошибку как попытку

print("Игра окончена.")

