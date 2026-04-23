history = []
result = None

while True:
    try:
        a = float(input("\nВведите первое число: "))
        operator = input("Выберите операцию (+, -, *, /): ").strip()
        b = float(input("Введите второе число: "))
    except ValueError:
        print("Ошибка! Недопустимое значение переменной.")

    if operator == "+":
        result = a + b
    elif operator == "-":
        result = a - b
    elif operator == "*":
        result = a * b
    elif operator == "/":
        if b != 0:
            result = a / b
        else:
            print("Ошибка! Деление на ноль.")
    else:
        print("Ошибка. Проверьте, верно ли введён символ операции.")

    if result != None:
        print("Результат:", result)
        history.append(f"{a} {operator} {b} = {result}")
        result = None

    exit = input("\nХотите продолжить? (да/нет): ").strip().lower()

    if exit == "нет":
        if history:
            print("\nИстория вычислений: ")
            for example in history:
                print(example)
        else:
            print("История вычислений пуста.")
        break
