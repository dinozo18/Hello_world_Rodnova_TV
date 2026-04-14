medium_name = input("Введите название питательной среды: ")
agar_concentration = float(input("Введите концентрацию агара (%): "))
sterilization_temp = float(input("Введите температуру стерилизации (°C): "))

with open("recipe.txt", "w", encoding="utf-8") as file:
    file.write(f"{medium_name}\n")
    file.write("-" * 30 + "\n")
    file.write(f"- Концентрация агара: {agar_concentration:.1f}%\n")
    file.write(f"- Температура стерилизации: {sterilization_temp:.0f}°C\n")

print("Файл 'recipe.txt' успешно сформирован!")