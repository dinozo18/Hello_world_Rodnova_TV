operator = input("Введите имя оператора: ")
pressure_value = float(input("Введите текущее значение давления (Па): "))

with open("sensor_log.txt", "w", encoding="utf-8") as file:
    file.write("=" * 40 + "\n")
    file.write("ЖУРНАЛ ДАТЧИКА ДАВЛЕНИЯ\n")
    file.write("=" * 40 + "\n")
    file.write(f"ОПЕРАТОР\t{operator}\n")
    file.write(f"ЗНАЧЕНИЕ\t{pressure_value:.2f} Па\n")
    file.write("=" * 40 + "\n")

print("Данные успешно сохранены в sensor_log.txt")