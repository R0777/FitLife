# Проект FitLife - MVP версия 1.0
WATER_AMOUNT_ML = 30
WATER_ONE_LITER_ML = 1000

print("Приветствую, как вас зовут?")

try:
    user_name = input("Меня зовут: ")
    # без title т.к. у пользователя должен быть выбор как себя именовать
except EOFError:
    user_name = "xXx"
    print(f"Чтож, будем тогда называть вас {user_name}")

print(f"Приветствую вас {user_name}!")

print(f"\n{user_name}, сколько вам полных лет?")
try:
    user_age = int(input("Мне "))
except (ValueError, EOFError):
    print("Используй только цифры (например: 25). Попробуйте еще раз...")
    user_age = int(input("Мне "))

print("\nУкажите ваш вес в килограммах")
try:
    user_weight = float(input("Мой вес: ").replace(",", "."))
except (ValueError, EOFError):
    print("Укажите вес, через точку (например: 70.5 или просто 70)")
    user_weight = float(input("Я вешу: "))

print("\nИ последний вопрос. Какой у вас рост в метрах? (например: 1.75)")
try:
    user_height = float(input("Мой рост: ").replace(",", "."))
except (ValueError, EOFError):
    print("Укажите рост, через точку (например: 1.75 или просто 1.7)")
    user_height = float(input("Мой рост: "))

WATER_AMOUNT_NEEDED = WATER_AMOUNT_ML / WATER_ONE_LITER_ML

bmi = round(user_weight / (user_height ** 2), 1)
water_needed = round(user_weight * WATER_AMOUNT_NEEDED, 1)

print("\nВАШИ ДАННЫЕ:")
print(f"Имя: {user_name}")
print(f"Возраст: {user_age} лет")
print(f"Рост: {user_height} м.")
print(f"Индекс массы тела: {bmi}")
print(f"Норма воды: {water_needed} л.")

print("\nРасчет окончен. Будьте здоровы!")
