# Проект FitLife - MVP версия 1.0
try:
    print("Приветствую, как вас зовут?")

    try:
        user_name = input("Меня зовут: ")
    except EOFError:
        user_name = "xXx"
        print(f"Чтож, будем тогда называть вас {user_name}")

    print(f"Приветствую вас {user_name}!")

    print(f"\n{user_name}, сколько вам полных лет?")
    try:
        user_age = int(input("Мне "))
    except (ValueError, EOFError):
        print("Допускается указывать только число (например: 25)."
        "Попробуйте еще раз.")
        user_age = int(input("Мне "))

    print("\nУкажите ваш вес в килограммах")
    try:
        user_weight = float(input("Мой вес: "))
    except (ValueError, EOFError):
        print("Укажите вес, через точку (например: 70.5 или просто 70)")
        user_weight = float(input("Я вешу: "))

    print("\nИ последний вопрос. Какой у вас рост в метрах? (например: 1.75)")
    try:
        user_height = float(input("Мой рост: "))
    except (ValueError, EOFError):
        print("Укажите рост, через точку (например: 1.75 или просто 1.7)")
        user_height = float(input("Мой рост: "))

    bmi = round(user_weight / (user_height ** 2), 1)
    water_needed = round(user_weight * 0.03, 1)

    print(f"\n{user_name}, ваши показатели:")
    print(f"Индекс массы тела: {bmi}")
    print(f"Водный баланс: {water_needed} литра")

    print("\nРасчет окончен. Будьте здоровы!")

except KeyboardInterrupt:
    print("\nУспехов, сделаем новый расчет в другой раз ;)")